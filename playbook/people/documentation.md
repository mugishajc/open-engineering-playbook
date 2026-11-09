# Documentation

Keep documentation in the same repository as the code, write it in plain text, review it in the same pull request, and give every page an owner and a review date. Sort pages by what the reader needs, using the Diátaxis framework: tutorials, how-to guides, reference and explanation. Docs written this way stay close to the truth, and docs that are wrong get fixed or deleted instead of misleading people.

## Outcomes

Starting points. Tune them to your organisation.

- 100% of repositories have a README that meets the standard below.
- 100% of production services have a runbook linked from the service catalogue.
- At least 90% of pages have a named owner and were reviewed in the last 12 months.
- Zero broken internal links on the docs site, checked in CI.
- A new engineer gets from clone to running tests using only the README in under 1 hour.

## Docs as code

- Write docs in Markdown (or AsciiDoc or reStructuredText) in the repository, next to the code they describe.
- Changes go through pull requests. A code change that changes behaviour updates the docs in the same pull request. Reviewers check this.
- Build a docs site from the repositories with a static site generator such as MkDocs, Sphinx, Docusaurus or Backstage TechDocs.
- Run checks in CI: link checking, spelling, and the plain-language lint from this playbook (`tools/plain_lint.py`).
- Diagrams are text where possible (Mermaid, PlantUML, Structurizr), so they can be reviewed and diffed.

## Diátaxis: four kinds of page

| Kind | Reader's need | Example | Rule of thumb |
|---|---|---|---|
| Tutorial | Learning, by doing something with a guide | "Build and deploy your first service on the platform" | Guaranteed to work. One path, no choices. |
| How-to guide | Doing a specific task | "Rotate the database credentials" | Steps, prerequisites, expected result. Assumes some knowledge. |
| Reference | Looking something up | API reference, configuration options, CLI flags | Complete and accurate. Generated from code where possible. |
| Explanation | Understanding why | Architecture overview, ADRs, design trade-offs | Context and reasons. No step-by-step. |

Most bad docs mix the four kinds. A tutorial that stops to explain history, or a reference page full of opinion, serves no reader well. Label each page with its kind.

Runbooks are how-to guides for operations. ADRs and RFCs are explanation. API contracts are reference.

## README standard

Every repository README answers these questions, in this order:

1. What is this and who is it for? (two sentences)
2. How do I run it locally and run the tests? (copy-paste commands)
3. How is it deployed, and where does it run?
4. Who owns it and how do I get help? (team, channel, on-call link)
5. Where are the runbook, dashboards, SLOs, ADRs and API contract?
6. How do I contribute? (link to `CONTRIBUTING.md`)

Keep the README under about 200 lines. Move depth into `docs/`.

## Ownership and freshness

- Every page has an owner (a team, not a person) through `CODEOWNERS` or front matter.
- Every page has a `last_reviewed` date in front matter. A CI job lists pages older than 12 months and opens one issue per owning team each quarter.
- Pages older than 18 months with no review get a visible banner: "This page may be out of date."
- Deleting a wrong page is a valid fix. A missing page is better than a page that sends someone in the wrong direction.

## Practice

### Foundation

- README to the standard above. `docs/` folder for anything longer. Runbook for anything in production.
- Docs change in the same pull request as the behaviour they describe.

### Standard

- One internal docs site built from all repositories, searchable, with pages labelled by Diátaxis kind.
- Link checking and the plain-language lint in CI for every repository with docs.
- Ownership and freshness automation as described above.
- Reference docs generated from code and contracts (OpenAPI, AsyncAPI, CLI help, configuration schemas).
- A technical writer or documentation lead for every 50 to 100 engineers, if you can fund one, who owns the standards and the site, not every page.

### Assured

- Controlled documents (policies, procedures, runbooks used as evidence) have version history, an approver and an effective date. Git history and pull request approvals provide this.
- Retention of documents follows your records policy. Public sector bodies usually have statutory records duties.
- Public-facing documentation meets WCAG 2.2 level AA, which the European Accessibility Act and many public sector rules expect.
- Documentation of the system is part of the [production readiness review](../reliability/production-readiness.md) and of release sign-off.

## Cloud, on-premises and air-gapped

- Host the docs site internally. Build it from internal mirrors of the generator and its plugins.
- Copy external references that engineers need (vendor manuals, standards, library docs) into the internal site with version and date. On an isolated network a link to the internet is a dead link.
- Ship offline documentation with software delivered to disconnected customers.

## Anti-patterns

| Anti-pattern | Fix |
|---|---|
| Docs in a wiki nobody owns | Docs in the repository, owned through `CODEOWNERS`. |
| One huge page that tries to teach, explain and list everything | Split by Diátaxis kind. |
| Docs updated "later" | Same pull request as the code. Reviewers block otherwise. |
| Screenshots of terminals | Copyable text commands. |
| Every page kept forever | Review dates, banners and deletion. |

## Templates

- [Runbook](../../templates/docs/runbook.md)
- [ADR template](../../templates/docs/adr.md)
- [Contributing guide](../../templates/repo/CONTRIBUTING.md)

## Sources

- Diátaxis, a systematic approach to technical documentation: https://diataxis.fr/
- Write the Docs, Docs as Code: https://www.writethedocs.org/guide/docs-as-code/
- Backstage TechDocs: https://backstage.io/docs/features/techdocs/
- WCAG 2.2, W3C Recommendation: https://www.w3.org/TR/WCAG22/
- DORA capability, documentation quality: https://dora.dev/capabilities/documentation-quality/
