# Kata: review this pull request

Review a realistic pull request in 30 minutes and decide whether it can merge. The diff is short, but it hides seven problems that reach production every week somewhere: two security flaws, two migration risks, a missing test, unclear naming and a change far too large to review. Write your comments first, then open the answers.

| | |
|---|---|
| Who | One engineer, or a pair who compare notes after 20 minutes |
| Time | 30 minutes: 20 to review, 10 to compare with the answers |
| Practice it teaches | [Code review](../../playbook/delivery/code-review.md), [database changes](../../playbook/delivery/database-changes.md), [secure development](../../playbook/security/secure-development.md) |

## How to do it

1. Read the description, then the tests, then the code, in that order. That is the order [code review](../../playbook/delivery/code-review.md#reviewer-responsibilities) recommends.
2. Write each comment with a label: `blocking:`, `question:`, `suggestion:`, `nit:`, `praise:` or `follow-up:`.
3. Decide: approve, approve with comments, or request changes.
4. Open the answers and count how many of the seven seeded problems you found. Then read the bonus findings.

## The pull request

> **feat(finance): CSV export of invoices for accountants**
>
> Accountants keep asking support for invoice exports, so this adds `GET /invoices/export?tenant=<id>&from=<date>` which returns a CSV. Also added an index to make the export fast and dropped the old `legacy_ref` column, which nothing uses any more.
>
> While I was in there I renamed the `billing` package to `finance` and upgraded SQLAlchemy from 1.4 to 2.0, so the full PR is 1,912 lines across 58 files. The diff below is the part that needs eyes; the rest is mostly mechanical.
>
> **Testing:** ran the existing suite, all green. Tried the endpoint locally with my tenant.
> **Risk:** low. **Rollback:** revert the PR.

```diff
diff --git a/migrations/0042_invoice_export.sql b/migrations/0042_invoice_export.sql
new file mode 100644
--- /dev/null
+++ b/migrations/0042_invoice_export.sql
@@ -0,0 +1,3 @@
+-- invoices has about 38 million rows in production
+CREATE INDEX idx_invoices_tenant_created ON invoices (tenant_id, created_at);
+ALTER TABLE invoices DROP COLUMN legacy_ref;
diff --git a/finance/export.py b/finance/export.py
new file mode 100644
--- /dev/null
+++ b/finance/export.py
@@ -0,0 +1,31 @@
+import csv
+import io
+import logging
+
+from flask import Blueprint, Response, request
+
+from finance.db import engine
+
+log = logging.getLogger(__name__)
+bp = Blueprint("export", __name__)
+
+
+@bp.route("/invoices/export")
+def do_it():
+    t = request.args["tenant"]
+    f = request.args.get("from", "2000-01-01")
+    user = request.headers.get("X-User-Email")
+    log.info("export requested by %s for tenant %s", user, t)
+
+    q = (f"SELECT id, number, customer_name, customer_email, total, created_at "
+         f"FROM invoices WHERE tenant_id = '{t}' AND created_at >= '{f}'")
+    with engine.connect() as conn:
+        rows = conn.exec_driver_sql(q).fetchall()
+
+    data2 = io.StringIO()
+    w = csv.writer(data2)
+    w.writerow(["id", "number", "customer", "email", "total", "date"])
+    for r in rows:
+        w.writerow(r)
+
+    return Response(data2.getvalue(), mimetype="text/csv")
diff --git a/finance/invoices.py b/finance/invoices.py
--- a/finance/invoices.py
+++ b/finance/invoices.py
@@ -88,6 +88,5 @@ def to_dict(invoice):
         "id": invoice.id,
         "number": invoice.number,
         "total": invoice.total,
-        "legacy_ref": invoice.legacy_ref,
         "created_at": invoice.created_at.isoformat(),
     }
diff --git a/tests/test_invoices.py b/tests/test_invoices.py
--- a/tests/test_invoices.py
+++ b/tests/test_invoices.py
@@ -12,2 +12,2 @@ def test_invoice_total_includes_tax(invoice_factory):
     inv = invoice_factory(net=100, tax_rate=0.18)
-    assert inv.total == 118
+    assert inv.total == 118.0
```

Write your review before you read on.

<details>
<summary>Answers: the seven seeded problems</summary>

**1. SQL injection (security).** `t` and `f` come straight from the query string and are pasted into the SQL with an f-string. `?tenant=x' OR '1'='1` returns every tenant's invoices.

> `blocking:` The query is built by string formatting from request parameters, so any caller can inject SQL. Use bound parameters, for example `conn.execute(text("... WHERE tenant_id = :tenant AND created_at >= :from_date"), {...})`, and parse `from` as a date first.

**2. Broken access control (security).** The tenant comes from the URL and the user's identity from a header the client sets. Nothing checks that the caller belongs to the tenant. Any signed-in user, or anyone who can reach the service and set a header, can export any tenant's invoices.

> `blocking:` Take the user and tenant from the authenticated session, not from `X-User-Email` or `?tenant=`, and check the user may export this tenant's invoices. Please add a test that a user from tenant A gets 403 for tenant B.

**3. Missing tests.** The only test change turns `118` into `118.0`. Nothing tests the new endpoint, the CSV format, the date filter or authorisation. "Ran the existing suite" proves only that nothing old broke.

> `blocking:` Please add tests for the endpoint: happy path, `from` filter, empty result, and the cross-tenant 403. Each should fail without this change. See [testing](../../playbook/delivery/testing.md).

**4. Blocking index on a large table (migration risk).** In PostgreSQL, a plain `CREATE INDEX` blocks writes to the table until it finishes. On 38 million rows that can be minutes of failed invoice writes. There is no lock timeout either.

> `blocking:` Use `CREATE INDEX CONCURRENTLY` (outside a transaction) and set `lock_timeout`. Please share the run time on a production-sized copy. See [database changes](../../playbook/delivery/database-changes.md).

**5. Destructive change in the same release (migration risk).** `legacy_ref` is dropped in the same release as the code that stops reading it. During a rolling deployment the old pods still read the column and fail. "Rollback: revert the PR" no longer works, because the old code needs a column that is gone, and the data in it is lost.

> `blocking:` Split this out. Ship the code that stops reading `legacy_ref` first; drop the column in a later release, after a backup, with separate approval. This is the contract step of expand and contract.

**6. Unclear naming.** `do_it`, `t`, `f`, `data2`, `w` and `r` tell the next reader nothing. A blueprint called `export` will collide with the next export.

> `nit:` Suggest `export_invoices_csv`, `tenant_id`, `from_date`, `buffer`, `writer`, `row`, and blueprint `invoice_export`.

**7. Oversized, mixed change.** A new feature, a package rename and a major ORM upgrade in one pull request of 1,912 lines across 58 files. The author asks for review of a slice; the risk is in the rest. A major SQLAlchemy upgrade changes behaviour, and a rename hides real changes in a sea of moved lines.

> `blocking:` Please split into three pull requests: the package rename alone (mechanical, quick to approve), the SQLAlchemy 2.0 upgrade alone (with its own test run and rollout), and this feature. I cannot approve 1,912 lines I have not reviewed. See [code review: keep it small](../../playbook/delivery/code-review.md#author-responsibilities).

**Decision:** request changes. Problems 1, 2 and 5 can each cause a serious incident on their own.

**Your score:** 6 or 7 found is a strong review. 4 or 5 is typical. Under 4, re-read the "what to look for" table in [code review](../../playbook/delivery/code-review.md#what-to-look-for-in-priority-order) and try again next week.

</details>

<details>
<summary>Bonus findings</summary>

- **Personal data in logs.** The user's email address is written to the log on every export. Log a user ID instead ([data security and privacy](../../playbook/data/data-security-and-privacy.md)).
- **Unbounded query.** `fetchall()` loads every matching row into memory. A tenant with 2 million invoices can take the process down. Stream rows, or paginate, or run large exports as a background job.
- **CSV formula injection.** A customer name starting with `=`, `+`, `-` or `@` runs as a formula when an accountant opens the file in a spreadsheet. Prefix such values with a single quote.
- **Risk and rollback in the description.** "Low" and "revert the PR" are not true for this change. The [pull request template](../../templates/github/PULL_REQUEST_TEMPLATE.md) asks for a real rollback plan.
- **Praise is part of review.** The author solved a real support problem and wrote a clear description of why. Say so.

</details>

## Variations

- **Pair version:** one person reviews, the other plays the author and must respond to each comment with a fix or a reason.
- **Team version:** everyone reviews alone for 15 minutes, then the team merges comments and agrees which are blocking. Compare how many `nit:` comments each person wrote.
- **Your own code:** take the last pull request you approved and review it again with this checklist.
