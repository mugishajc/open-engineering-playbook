# Maturity model

Use the table below to see, in one place, what Foundation, Standard and Assured look like in each of the sixteen practice areas, then run the self-assessment to find where you are. The levels are not grades. Foundation is the right target for a Solo engineer or a Startup, and Assured is only worth its cost where regulation, public accountability or real risk demands evidence. Pick the level your profile needs, close the biggest gaps first, and reassess every quarter.

## Outcomes

Starting points. Tune them to your organisation.

- The self-assessment is completed and committed to a repository at least once a quarter.
- Every area is at or above the target level for your profile within 4 quarters of adopting the playbook.
- Each quarter, the team or leadership group picks at most 3 gaps to close and names an owner for each.
- Every "true" answer can be backed by evidence someone can open in under 5 minutes.

## How the levels work

| Level | Meaning | Default for |
|---|---|---|
| Foundation | The minimum that pays for itself immediately | Solo, Startup |
| Standard | Shared, automated and owned across teams | Scale-up, Enterprise |
| Assured | Adds evidence, separation of duties and audit trails | Regulated, Public sector |

An area reaches a level only when every criterion at that level and at every level below it is met. Being Assured in security and below Foundation in reliability is a common and dangerous pattern: fix the floor first.

## The model

| Area | Foundation | Standard | Assured |
|---|---|---|---|
| Strategy | A one-page written strategy with no more than five actions. Build, buy or adopt reasoning written down. ([strategy](../strategy/technical-strategy.md)) | Strategy reviewed quarterly with a horizon scan. Business cases for major investments. | Strategy linked to risk appetite and regulatory obligations. Exit plans for critical suppliers. |
| Operating model | Clear owner for every system. Small, stable teams. ([team topology](../operating-model/team-topology.md)) | Written decision rights. Team types and interaction modes chosen on purpose. | Separation of duties defined and enforced. Governance with recorded decisions. |
| Product | A one-page product strategy with outcomes. The product trio talks with users every week. ([product strategy](../product/product-strategy.md)) | Outcome roadmaps in Now, Next and Later with forecast ranges. Experiments with written briefs. Launches with success and stop criteria. ([product metrics and experiments](../product/product-metrics-and-experiments.md)) | No experiments on rights, prices or entitlements without legal review. Pricing and launch decisions recorded. Outcomes reported for groups who struggle. |
| Project management | A one-page charter for work with an external date or real money. Dates and costs given as ranges. ([projects and products](../project-management/projects-and-products.md)) | RAID log reviewed weekly, status colours set by rule, stage gates that can stop work. ([risks, RAID logs and stage gates](../project-management/risks-raid-and-stage-gates.md)) | A method tailored from a recognised standard. Independent assurance at major gates. Gate decisions and re-baselines kept for audit. |
| Ways of working | Visible work, small batches, a regular team retrospective. ([agile and Scrum](../ways-of-working/agile-and-scrum.md)) | Forecasts from throughput data. Product and engineering plan together. | Planning records and traceability from requirement to release where required. |
| Delivery | Protected main branch, code review on every change, CI on every pull request. ([code review](../delivery/code-review.md)) | Trunk-based development, automated releases, feature flags, safe database changes. | Signed, traceable releases. Approvals recorded. Environments separated. |
| Quality | Automated tests run on every change. Defects tracked. ([quality engineering](../quality/quality-engineering.md)) | Risk-based test strategy per service with performance, security and accessibility checks; fast and reliable suites; flaky tests quarantined within 24 hours and fixed within 14 days. ([test strategy](../quality/test-strategy.md)) | Test evidence retained and linked to releases and requirements. |
| Reliability | Basic monitoring, a written incident process, backups taken. ([service levels](../reliability/service-levels.md)) | SLOs with error budgets, blameless postmortems, sustainable on-call, restores tested. | Recovery targets tested and reported. Incident records kept as evidence. Regulatory reporting deadlines met. |
| Security | Secrets out of code, dependency updates automated, MFA everywhere. ([secure development](../security/secure-development.md)) | SBOMs, signed artefacts, vulnerability fix targets met, least-privilege access. | SSDF practices mapped and evidenced. Supply chain provenance verified at deploy. Access reviewed on a schedule. |
| Data | Data classified. Personal data known and minimised. ([data governance](../data/data-governance.md)) | Data owners, data contracts for shared data, quality checks in pipelines. | Impact assessments, retention enforced, lineage and access evidence for audit. |
| AI | Approved tools and a use policy. No sensitive data in unapproved tools. ([AI governance](../ai/ai-governance.md)) | Evals before launch, cost and latency budgets, AI-specific threat review. ([building with AI](../ai/building-with-ai.md)) | AI inventory and risk classification, records for regulators, human oversight documented. |
| Architecture | ADRs for costly decisions. Contracts for APIs with outside callers. ([decision records](../architecture/decision-records.md)) | RFC process, tech radar, house API standards checked in CI, OpenTelemetry everywhere. | Architecture decisions approved by named people, with security sign-off and retained history. |
| Platform | One template and one deploy path. Managed services preferred. ([golden paths](../platform/golden-paths.md)) | Platform run as a product, self-service for common requests, catalogue of all services. | Controls built into the platform and evidenced automatically. Tested exit plans. Air-gapped parity where needed. |
| People | Onboarding plan, README standard, code assistant policy. ([onboarding](../people/onboarding.md)) | Structured hiring, career framework, docs ownership and freshness, inner source. | Training and access evidence, key-person risk tracked, controlled documents. |
| Measurement | Deployment frequency and lead time tracked. One SLO. ([metrics](metrics.md)) | All five DORA metrics automated, SLO attainment, developer survey every 6 months. | Metric definitions versioned, raw data retained, figures reproducible for auditors. |
| Compliance | List of laws and standards that apply. ([control mapping](../compliance/control-mapping.md)) | Controls mapped to practices with automated evidence. | Evidence ready for audit on request. Independent review. Public sector or sector-specific duties met. |

## Running the self-assessment

The tool is a single Python script with no dependencies beyond the standard library (Python 3.11 or later). The full instructions are in the [assessment README](../../assessment/README.md). In short:

1. Generate a blank answers file for your profile:
   `python3 assessment/assess.py --questions assessment/questions.toml --init --profile scale-up --output my-answers.toml`
2. Answer each question `true` or `false`. Set `true` only when you can point to the evidence. Add overlays such as `"regulated"` or `"public-sector"` when they apply.
3. Score it:
   `python3 assessment/assess.py --questions assessment/questions.toml --answers my-answers.toml --format markdown --output report.md`
4. Read the report: the level reached per area, the target for your profile and overlays, and the next actions.
5. Commit the answers and the report. Repeat every quarter and compare.

To keep an area from slipping, run the tool in CI with `--check`, which exits with a non-zero code when any area falls below its target.

## Practice

### Foundation

- One person completes the assessment in under 1 hour. Fix the areas that are below Foundation before anything else.

### Standard

- Each engineering group completes its own assessment. Leadership reviews the results together each quarter and funds the top 3 gaps.
- Answers live in a repository with history, so progress is visible.

### Assured

- Every `true` answer links to its evidence. An internal audit or second-line function samples 10% of answers each year.
- Results feed the risk register and reports to the board or oversight body.

## Cloud, on-premises and air-gapped

The tool runs offline with no network access. Copy the `assessment/` folder through your transfer process and run it inside the enclave. Keep answers for classified systems on the classified network.

## Anti-patterns

| Anti-pattern | Fix |
|---|---|
| Treating Assured as the goal for everyone | Target the level your profile needs. Extra process costs time and buys nothing. |
| Answers set to `true` on intent | `true` needs evidence that exists today. |
| One heroic assessment, never repeated | Quarterly, committed to git, compared with the last run. |
| Comparing teams' scores to rank them | Use results to choose investments, not to grade teams. |
| Working on every gap at once | At most 3 gaps per quarter, each with an owner. |

## Templates

- [Assessment README and tool](../../assessment/README.md)
- [Example answers](../../assessment/example-answers.toml)

## Sources

- DORA capabilities catalogue, the research basis for many Standard criteria: https://dora.dev/capabilities/
- NIST Secure Software Development Framework, SP 800-218: https://csrc.nist.gov/projects/ssdf
- CNCF Platform Engineering Maturity Model: https://tag-app-delivery.cncf.io/whitepapers/platform-eng-maturity-model/
