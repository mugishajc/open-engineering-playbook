# Database changes

Make every schema change backward compatible with the version of the application that is already running, using the expand and contract pattern, so that deploys and rollbacks need no downtime. Run migrations as a separate, reviewed step, never as a side effect of application start-up. Treat destructive changes (dropping columns or tables) as a final, separately approved step after a backup.

## Outcomes

Starting targets. Tune them to your data volume.

| Signal | Starting target |
|---|---|
| Deploys that need planned downtime for a schema change | Zero for services you run |
| Migrations that hold an exclusive lock on a large table | Zero; lock timeout set on every migration |
| Migrations tested against a production-sized dataset before release | 100% for tables over 1 million rows |
| Destructive migrations shipped in the same release as the code change that needs them | Zero |
| Application rollback possible after a migration | 100% of releases |

## Expand and contract

Also called parallel change. Example: rename `customer.fullname` to `customer.display_name`.

| Step | Release | Schema | Application |
|---|---|---|---|
| 1. Expand | N | Add `display_name`, nullable | Writes both columns, reads `fullname` |
| 2. Backfill | N (background job, started only after release N is fully rolled out) | Copy `fullname` into `display_name` in batches | No change |
| 3. Switch reads | N+1 | Add constraints if needed (`NOT NULL`) once backfill is complete | Reads `display_name`, still writes both |
| 4. Stop old writes | N+2 | No change | Writes only `display_name` |
| 5. Contract | N+3, after a backup | Drop `fullname` | No change |

At every step, the previous application version still works against the current schema. That is what makes rollback safe.

## Practice

### Foundation

- **Migrations are code.** They live in the repository, run in order, are versioned by a migration tool (Flyway, Liquibase, Alembic, Django, Rails, Atlas, Sqitch or your framework's tool) and are reviewed in pull requests.
- **Backward compatible by default.**
  - Add columns as nullable or with a default the database applies without rewriting the table (check this for your engine and version).
  - Never rename or drop a column or table in the same release as the code that stops using it.
  - Never change a column type in place on a large table. Add a new column and migrate.
- **Separate step.** Run migrations from a pipeline job or a one-off task before the new application version starts. Applications do not run migrations on start-up. A long migration blocks start-up and fails health checks, a failed one puts every instance in a crash loop, and rolling back the application cannot undo a migration that ran as a side effect.
- **Back up before destructive steps** and test that the backup restores. See [backup and recovery](../reliability/backup-and-recovery.md).
- **Small changes.** One logical change per migration.

### Standard

- **Locking rules.**
  - Set a lock timeout on every migration (PostgreSQL: `SET lock_timeout = '5s';`) so a blocked migration fails fast instead of queuing all traffic behind it. Retry later.
  - Create indexes without blocking writes (PostgreSQL: `CREATE INDEX CONCURRENTLY`; MySQL: online DDL with `ALGORITHM=INPLACE, LOCK=NONE` where supported). Note that `CONCURRENTLY` cannot run inside a transaction.
  - Add foreign keys and check constraints in two steps where the engine allows it (PostgreSQL: `NOT VALID`, then `VALIDATE CONSTRAINT`).
  - For large MySQL table changes, use an online schema change tool such as gh-ost or pt-online-schema-change.
- **Batched backfills.** Update rows in batches (starting point: 1,000 to 10,000 rows), commit each batch, pause between batches, and make the job restartable. Watch replication lag and stop if it grows.
- **Test on production-sized data.** Run each migration against a masked or synthetic dataset of production size and record duration and locks. See [environments](environments.md#production-data-rules).
- **CI checks.** Lint migrations for dangerous operations (for example squawk for PostgreSQL, or your tool's built-in checks). Apply all migrations to an empty database and to a copy of the current schema in CI.
- **Rollback plan.** For each migration, write how to undo it: a tested down migration, or a forward fix, or restore from backup for destructive steps. Releases keep the application rollback independent of the schema rollback.

#### Review rules

| Migration touches | Reviewer |
|---|---|
| Any schema change | Code owner of the service |
| Tables over 1 million rows, or hot tables | Plus a database specialist (DBA or data platform team) |
| Drops, truncates, type changes, data deletes | Plus a second approver, and a recorded backup check |
| Personal data columns (add, move, copy) | Plus privacy review: purpose, retention, access |

Reviewers check: backward compatibility with the running version, lock behaviour, run time on production-sized data, index use, rollback path, and whether the change belongs in this release or a later contract step. See [code review](code-review.md).

### Assured

- **Change records** for production schema changes, with the migration, its review, test results on production-sized data and the backup reference. This supports ISO/IEC 27001:2022 Annex A 8.32 and 8.13, and SOC 2 CC8.1.
- **Separation of duties.** Engineers do not run ad hoc DDL in production. Migrations run only through the pipeline, under a service identity, with the run logged.
- **Data fixes** (one-off updates to production data) go through the same review as migrations: written as a script, reviewed, run by the pipeline, logged.
- **Retention and deletion.** Dropping a column that held personal data must follow your retention schedule, including backups.

## Cloud, on-premises and air-gapped

- Managed databases in the cloud may block some operations or add their own locking. Test on the same managed service and version you run in production.
- For software customers install, migrations run during customer upgrades without your engineers present. Make them idempotent, safe to re-run after a failure, and tested on upgrade from every supported version. Ship a pre-upgrade check that reports disk space, version and long-running locks.
- In air-gapped networks, migration tools and their plugins come from the internal package mirror. Pin their versions.

## Anti-patterns

| Anti-pattern | Fix |
|---|---|
| Rename a column and deploy the code in one release | Expand and contract over several releases. |
| Migrations run on application start-up | Separate pipeline step before the new version starts. |
| `CREATE INDEX` on a large, busy table | `CONCURRENTLY` or online DDL, with a lock timeout. |
| One `UPDATE` across 50 million rows | Batched, restartable backfill job. |
| Drop column without a backup check | Separate contract release, backup verified first. |
| Hand-run SQL in production to "fix data" | Scripted, reviewed data fix run through the pipeline. |

## Templates

- [Pull request template (risk and rollback section)](../../templates/github/PULL_REQUEST_TEMPLATE.md)
- [Release checklist (migration steps)](../../templates/docs/release-checklist.md)
- [CODEOWNERS (migration paths)](../../templates/github/CODEOWNERS)

## Sources

- Danilo Sato, Parallel Change: https://martinfowler.com/bliki/ParallelChange.html
- PostgreSQL, CREATE INDEX: https://www.postgresql.org/docs/current/sql-createindex.html
- PostgreSQL, ALTER TABLE: https://www.postgresql.org/docs/current/sql-altertable.html
- PostgreSQL, lock_timeout: https://www.postgresql.org/docs/current/runtime-config-client.html
- MySQL 8.4 LTS, InnoDB online DDL: https://dev.mysql.com/doc/refman/8.4/en/innodb-online-ddl.html
- gh-ost: https://github.com/github/gh-ost
- squawk: https://squawkhq.com/
