# Open Engineering Playbook

**An open engineering playbook and template kit for any organisation that builds software: one engineer, a startup, an enterprise, a bank or a government ministry.**

Most engineering handbooks describe how one company works. They are useful to read and hard to adopt. This playbook is written to be adopted. Every practice comes at three levels, every level has measurable outcomes, every recommendation works on public cloud, on-premises and air-gapped networks, and every template is ready to copy into a repository today.

It covers the full path: from technical strategy and how to move a whole organisation to a new way of working, down to the pull request template your engineers will see this afternoon. It is written for the problems teams have now: code assistants in every editor, AI features that stall before production, supply chain attacks, new regulation with real deadlines, cloud bills that outgrow revenue, and senior engineers who are hard to hire and easy to lose.

**Arrived with a problem? Start at [PROBLEMS.md](PROBLEMS.md).** It maps about seventy real problems to the pages that address them.

## Who it is for

| You are | Start here |
|---|---|
| A solo engineer or freelancer | [Solo profile](profiles/solo.md), then copy the templates with `tools/adopt.sh` |
| A startup CTO or tech lead | [Startup profile](profiles/startup.md) and [code review](playbook/delivery/code-review.md) |
| A head of engineering at a scale-up | [Scale-up profile](profiles/scale-up.md) and [team topology](playbook/operating-model/team-topology.md) |
| A CTO or principal engineer at an enterprise | [Transition playbook](playbook/strategy/transition-playbook.md) and [technical strategy](playbook/strategy/technical-strategy.md) |
| A CISO or security lead | [Supply chain](playbook/security/supply-chain.md) and [control mapping](playbook/compliance/control-mapping.md) |
| An auditor or compliance officer | [Control mapping](playbook/compliance/control-mapping.md) and [change management](playbook/reliability/change-management.md) |
| A public sector technology lead | [Public sector profile](profiles/public-sector.md) and [public sector](playbook/compliance/public-sector.md) |
| At a bank, insurer, health or telecom provider | [Regulated profile](profiles/regulated.md) and [regulated industries](playbook/compliance/regulated-industries.md) |
| A platform or DevOps engineer | [Golden paths](playbook/platform/golden-paths.md) and [cloud, on-premises and air-gapped](playbook/platform/cloud-on-prem-air-gapped.md) |
| A technical evangelist or advocate | [Stakeholders and communication](playbook/strategy/stakeholders-and-communication.md) |

## Start in ten minutes

```bash
git clone https://github.com/mugishajc/open-engineering-playbook.git && cd open-engineering-playbook

# 1. See where you stand. Writes a blank answers file, one line per question.
python3 assessment/assess.py --questions assessment/questions.toml --init > my-answers.toml
#    Answer true or false, set your profile, then score it:
python3 assessment/assess.py --questions assessment/questions.toml --answers my-answers.toml

# 2. Copy the templates into one of your repositories. Existing files are never overwritten.
tools/adopt.sh --target ../your-repo --platform github --with-security --dry-run
tools/adopt.sh --target ../your-repo --platform github --with-security
```

The assessment report shows the level you reach in each of the fourteen areas, the level your profile calls for, and the next five actions, each linked to the page that explains it. Python 3.11 or later, standard library only.

## What is inside

```
PROBLEMS.md    seventy real problems, each mapped to the pages that fix it
playbook/      fourteen areas, about ninety pages, each at three levels
  strategy/          technical strategy, transition playbook, business case,
                     build or buy, portfolio and capacity, stakeholders, horizon scan to 2030
  operating-model/   team topology, decision rights, roles, engineering and IT governance
  ways-of-working/   agile and Scrum without the theatre, forecasting, product partnership
  delivery/          source control, code review, testing, CI, releases, versioning,
                     feature flags, environments, database changes, GitOps, infra as code
  quality/           quality engineering, test-driven development
  reliability/       service levels, incidents, postmortems, root cause analysis, rollbacks,
                     on-call, readiness, backup and recovery, change management without a weekly board
  security/          secure development, supply chain, secrets, dependencies,
                     vulnerabilities, access, zero trust, post-quantum, third parties
  data/              data governance, data quality and contracts, security and privacy
  ai/                AI governance, building with AI, AI application security
  architecture/      architecture practice, decision records, RFCs, tech radar, APIs,
                     observability, scaling, legacy modernisation, technical debt
  platform/          golden paths, developer platform, cloud native, cloud,
                     on-premises and air-gapped, FinOps, green software
  people/            onboarding, documentation, code assistants, knowledge sharing,
                     hiring, skills gap, career framework, sustainable pace
  measurement/       metrics (DORA, SLOs, SPACE), maturity model
  compliance/        control mapping, public sector, regulated industries
profiles/      adoption paths: solo, startup, scale-up, enterprise, public sector, regulated
templates/     ready-to-copy files: GitHub, GitLab, Kubernetes, Argo CD, documents, CSV registers
assessment/    maturity self-assessment that runs from a TOML file
tools/         init script and the plain-language check
```

## What is different about it

**Three levels, not one rule book.** Every practice has a Foundation level that pays for itself in a week, a Standard level for organisations with several teams, and an Assured level that adds the evidence and separation of duties regulators and auditors ask for. A profile picks the level for you. A five-person startup and a central bank read the same page and get different, correct answers.

**It works without the internet.** Each page has a section on what changes on-premises and on air-gapped networks: internal mirrors, key-pair signing, offline update media, self-hosted runners. Sovereignty and exit plans are treated as first-class requirements, not edge cases.

**Do the work once, show the evidence many times.** The [control mapping](playbook/compliance/control-mapping.md) links each practice to ISO/IEC 27001:2022, SOC 2, the NIST SSDF, SLSA, the OpenSSF OSPS Baseline, the EU Cyber Resilience Act, NIS2 and the EU DORA regulation. Code review, CI logs, signed builds and postmortems become the audit evidence. No separate compliance theatre.

**Strategy and transition, not only practices.** The [transition playbook](playbook/strategy/transition-playbook.md) covers how to move an organisation from where it is to where it needs to be: assess, decide, pilot, scale, sustain, with measurable exit criteria and a stop decision at every gate. It includes what changes for public bodies working in budget years and for firms that must notify a regulator.

**Maturity assessment as code.** The assessment is a TOML file in your repository. Answer it each quarter, commit it, and the history shows your progress in pull requests, not in a slide deck.

**Plain language, enforced.** The playbook is written for busy readers, many of whom read English as a second language. A check in CI rejects vague filler words and dashes used as punctuation. You can run the same check on your own documentation.

**Change management without a weekly meeting.** The playbook shows how to replace a change advisory board with automated controls that produce better evidence: peer review, required checks, deployment records. It explains how that still satisfies ISO 27001 control 8.32 and SOC 2 CC8.1.

**Written for the AI era, without the hype.** A fill-in policy for code assistants: what data may be sent where, who owns the result, and how to measure the effect honestly, including the rework it can cause. A path from AI pilot to production with evaluations, cost budgets and fallbacks. Controls for every item in the OWASP Top 10 for LLM Applications, and approval rules for agents that can call tools.

**Ready for the deadlines already on the calendar.** The [horizon scan](playbook/strategy/horizon-scan.md) and the pages behind it cover the EU Cyber Resilience Act reporting duty that started in September 2026, the EU AI Act high-risk obligations now due from December 2027, and the move away from RSA and elliptic-curve cryptography that NIST plans to deprecate after 2030.

**People problems are engineering problems.** Structured hiring with work samples and scorecards, a career framework, sustainable on-call and pace, and agile practice with the theatre removed. Teams that cannot hire, grow and keep good engineers do not get to the rest of this playbook.

## Standards and frameworks covered

| Area | Referenced |
|---|---|
| Delivery performance | [DORA metrics](https://dora.dev/guides/dora-metrics-four-keys/), including rework rate and failed deployment recovery time |
| Reliability | [Google SRE book and workbook](https://sre.google/books/): SLOs, error budgets, burn-rate alerts |
| Secure development | [NIST SP 800-218 SSDF](https://csrc.nist.gov/projects/ssdf), [OWASP](https://owasp.org/) |
| Supply chain | [SLSA](https://slsa.dev/spec/), [Sigstore](https://www.sigstore.dev/), [CycloneDX](https://cyclonedx.org/), [SPDX](https://spdx.dev/), [OpenSSF Scorecard](https://scorecard.dev/), [OSPS Baseline](https://baseline.openssf.org/) |
| Information security | ISO/IEC 27001:2022 Annex A, SOC 2 Trust Services Criteria, [NIST SP 800-207 zero trust](https://csrc.nist.gov/pubs/sp/800/207/final) |
| AI | [EU AI Act](https://eur-lex.europa.eu/eli/reg/2024/1689/oj), ISO/IEC 42001:2023, [NIST AI RMF](https://www.nist.gov/itl/ai-risk-management-framework), [OWASP Top 10 for LLM Applications](https://genai.owasp.org/) |
| Cryptography | [NIST FIPS 203, 204, 205](https://csrc.nist.gov/projects/post-quantum-cryptography) post-quantum standards and the NIST IR 8547 transition timeline |
| Cost and carbon | [FinOps Framework](https://www.finops.org/framework/), [Software Carbon Intensity](https://sci.greensoftware.foundation/) (ISO/IEC 21031:2024) |
| Regulation | [EU Cyber Resilience Act](https://digital-strategy.ec.europa.eu/en/policies/cyber-resilience-act), NIS2, EU DORA regulation, GDPR and national data protection laws |
| Accessibility | [WCAG 2.2](https://www.w3.org/TR/WCAG22/), European Accessibility Act |
| Teams | Team Topologies |
| Public services | [UK Service Standard](https://www.gov.uk/service-manual/service-standard), [UK Technology Code of Practice](https://www.gov.uk/guidance/the-technology-code-of-practice), [US Digital Services Playbook](https://playbook.cio.gov/) |
| Conventions | [Conventional Commits](https://www.conventionalcommits.org/en/v1.0.0/), [SemVer](https://semver.org/), [Keep a Changelog](https://keepachangelog.com/en/1.1.0/), [MADR](https://adr.github.io/madr/), [OpenAPI](https://spec.openapis.org/oas/latest.html), [OpenTelemetry](https://opentelemetry.io/) |

This playbook is not legal advice. Where it mentions a regulation, read the regulation and talk to your counsel.

## Built on public work

The playbook stands on work that others shared openly: [Google's engineering practices](https://google.github.io/eng-practices/), the [Google SRE books](https://sre.google/books/), the [DORA research programme](https://dora.dev/), Team Topologies by Matthew Skelton and Manuel Pais, the [UK Government Digital Service](https://www.gov.uk/service-manual), the [US Digital Services Playbook](https://playbook.cio.gov/), the [OpenSSF](https://openssf.org/), the [GitLab handbook](https://handbook.gitlab.com/), the [Rust RFC process](https://rust-lang.github.io/rfcs/), [Kubernetes enhancement proposals](https://github.com/kubernetes/enhancements), the [Diátaxis](https://diataxis.fr/) documentation framework and the [Thoughtworks Technology Radar](https://www.thoughtworks.com/radar). Each page links the sources it draws on.

## Contributing

Corrections, templates and on-premises details from people who run real systems are the most valuable contributions. Read [CONTRIBUTING.md](CONTRIBUTING.md) and [STYLE.md](STYLE.md), and see [GOVERNANCE.md](GOVERNANCE.md) for how recommendations change.

## Licence

Templates, scripts and code: MIT, copy them freely. Playbook text: CC BY 4.0, share and adapt with credit. See [LICENSE](LICENSE).
