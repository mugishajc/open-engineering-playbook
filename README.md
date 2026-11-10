# Open Engineering Playbook

**How to build and run software well, written so that any organisation can adopt it: one engineer, a small business, a startup, a large enterprise, a bank or a government ministry.**

Writing code got cheap. Deciding what to build, proving it is safe, shipping it and running it for years did not. This playbook covers all of that, from technical strategy down to the pull request template your engineers will see this afternoon.

Most engineering handbooks describe how one company works. This one is written to be adopted. Every practice comes at three levels and every target is measurable. Everything works on public cloud, on-premises and air-gapped networks, and every template is ready to copy. New to a term? See the [glossary](GLOSSARY.md).

**111** practice pages in 16 areas · **8** regional compliance guides · **18** toolkits for leaders · **92** ready-to-copy templates · **136** real problems mapped to answers · **112**-question self-assessment (19 for small businesses) · **189** true-or-false statements · **19** tabletop exercises, katas and decision games

## Three ways in

1. **Start from your problem.** [PROBLEMS.md](PROBLEMS.md) maps real problems to the pages that fix them. Examples: "pull requests wait days for review", "the board cannot see whether IT is under control".
2. **Start from your role.** [For leaders](leaders/README.md) gives executives, technology, product, programme and quality leaders, government leaders and boards the toolkits they use every week.
3. **Start from your organisation.** [Profiles](profiles/README.md) say what to adopt in week 1, month 1, quarter 1 and year 1, for every size from one engineer to a ministry.

Terms and acronyms are explained in the [glossary](GLOSSARY.md).

## Pick your door

**By organisation**

| You are | Start here |
|---|---|
| A small or medium business that uses software but does not build it (clinic, school, law firm, retailer, manufacturer, NGO) | [SME profile](profiles/sme.md) and [for small and medium businesses](leaders/for-small-and-medium-businesses.md) |
| A solo engineer or freelancer | [Solo profile](profiles/solo.md), then copy the templates with `tools/adopt.sh` |
| A startup | [Startup profile](profiles/startup.md) and [code review](playbook/delivery/code-review.md) |
| A scale-up with several teams | [Scale-up profile](profiles/scale-up.md) and [team topology](playbook/operating-model/team-topology.md) |
| A large enterprise | [Enterprise profile](profiles/enterprise.md) and the [transition playbook](playbook/strategy/transition-playbook.md) |
| A ministry, agency or public body | [Public sector profile](profiles/public-sector.md) and [for government](leaders/for-government.md) |
| A bank, insurer, health or telecom provider | [Regulated profile](profiles/regulated.md) and [for financial services](leaders/for-financial-services.md) |

**By role**

| You are | Start here |
|---|---|
| A CEO, CFO, COO or board member in any sector | [For business executives](leaders/for-business-executives.md) and [questions for your technology leader](templates/leaders/questions-for-your-technology-leader.md) |
| Any leader deciding what to do about AI | [Leading in the AI era](leaders/leading-in-the-ai-era.md) |
| A newly appointed CTO, CIO or chief architect | [First 90 days](leaders/first-90-days.md) and [operating rhythm](leaders/operating-rhythm.md) |
| A CTO, CIO or principal engineer | [Technical strategy](playbook/strategy/technical-strategy.md), [decision making](leaders/decision-making.md) and [board reporting](leaders/board-and-executive-reporting.md) |
| A chief or enterprise architect | [Architecture toolkit](leaders/architecture-toolkit.md) and [AI architecture patterns](playbook/ai/ai-architecture-patterns.md) |
| An IT strategist or planner | [Strategy toolkit](leaders/strategy-toolkit.md) and [portfolio and capacity](playbook/strategy/portfolio-and-capacity.md) |
| A chief product officer, head of product or product leader | [For product leaders](leaders/for-product-leaders.md), [product strategy](playbook/product/product-strategy.md) and [roadmaps and prioritisation](playbook/product/roadmaps-and-prioritisation.md) |
| A programme director, portfolio lead or head of a PMO | [For programme and portfolio leaders](leaders/for-programme-and-portfolio-leaders.md), [status reporting](playbook/project-management/status-reporting.md) and [a modern PMO](playbook/project-management/modern-pmo.md) |
| A project manager | [Projects and products](playbook/project-management/projects-and-products.md), [planning fixed scope and budget](playbook/project-management/planning-fixed-scope-and-budget.md) and [risks, RAID logs and stage gates](playbook/project-management/risks-raid-and-stage-gates.md) |
| A head of QA, test manager or quality lead | [For QA and test leaders](leaders/for-qa-and-test-leaders.md), [test strategy](playbook/quality/test-strategy.md) and [quality engineering](playbook/quality/quality-engineering.md) |
| A chief data officer | [For data and digital officers](leaders/for-data-and-digital-officers.md) |
| A chief digital officer (services, channels, digital transformation) | [For data and digital officers](leaders/for-data-and-digital-officers.md#chief-digital-officers), the [transition playbook](playbook/strategy/transition-playbook.md) and [product partnership](playbook/ways-of-working/product-partnership.md) |
| A CISO or security lead | [Supply chain](playbook/security/supply-chain.md), [AI application security](playbook/ai/ai-application-security.md) and [control mapping](playbook/compliance/control-mapping.md) |
| An auditor or compliance officer | [Control mapping](playbook/compliance/control-mapping.md), [change management](playbook/reliability/change-management.md) and [regional guides](playbook/compliance/regions/) |
| An engineering manager or team lead | [Agile in the AI era](playbook/ways-of-working/agile-in-the-ai-era.md) and [AI engineering practices](playbook/ai/ai-engineering-practices.md) |
| A platform, DevOps or SRE engineer | [Golden paths](playbook/platform/golden-paths.md), [cloud native](playbook/platform/cloud-native.md) and [service levels](playbook/reliability/service-levels.md) |
| A technical evangelist or advocate | [Stakeholders and communication](playbook/strategy/stakeholders-and-communication.md) |
| Anyone who learns by doing | [Exercises](exercises/README.md): quizzes, tabletop scenarios, katas and decision games |

## Start in ten minutes: owners and executives

No tools needed.

1. Read [for small and medium businesses](leaders/for-small-and-medium-businesses.md) or [for business executives](leaders/for-business-executives.md).
2. Print the [first-hour plan](templates/sme/first-hour-plan.md) and fill in the contacts.
3. Send the [IT provider questions](templates/sme/it-provider-questions.md) to your IT provider, or the [questions for your technology leader](templates/leaders/questions-for-your-technology-leader.md) to your CTO or CIO.

## Start in ten minutes: engineers

You need git and Python 3.11 or later. Check with `python3 --version`. If it shows 3.10 or older, as on stock macOS or Ubuntu 22.04:

- run the commands below with `python3.12` or `python3.11` if one is installed;
- on Windows, use `py -3` (the Python launcher) instead of `python3`;
- otherwise install the current release from [python.org](https://www.python.org/downloads/), Homebrew (`brew install python@3.12`) or your package manager.

The scripts use only the standard library: nothing to install, no network access.

```bash
git clone https://github.com/mugishajc/open-engineering-playbook.git
cd open-engineering-playbook

# 1. See where you stand. Write a blank answers file for your profile:
#    solo, sme, startup, scale-up or enterprise.
python3 assessment/assess.py --init --profile startup > my-answers.toml
#    Set each answer to true or false, then score it:
python3 assessment/assess.py --answers my-answers.toml

# 2. Test what you know: ten true-or-false statements, each answer explained.
python3 exercises/quiz.py --count 10

# 3. Copy the templates into one of your repositories.
#    Existing files are never overwritten. Add --solo if you work alone.
tools/adopt.sh --target ../your-repo --platform github --with-security --dry-run
tools/adopt.sh --target ../your-repo --platform github --with-security
```

The report shows the level each area reaches, the level your profile calls for, and the next five actions. Each action links to the page that explains it. `tools/adopt.sh` needs bash, so on Windows run it in Git Bash or WSL.

## Come back each quarter

Run the assessment again every quarter and commit the answers file: the diff is your progress. Watch the repository's releases on GitHub to hear about changes, and read the [changelog](CHANGELOG.md) for what changed and why.

## What is inside

```
PROBLEMS.md    130 real problems, each mapped to the pages that address it
playbook/      16 areas, 105 pages, each practice at three levels
  strategy/          technical strategy, transition playbook, business case, budget and cost,
                     build or buy, suppliers and contracts, portfolio and capacity,
                     stakeholders, horizon scan to 2030
  operating-model/   team topology, decision rights, roles, engineering and IT governance
  product/           product strategy, discovery, roadmaps and prioritisation, metrics and
                     experiments, pricing and packaging, launch and adoption
  project-management/ projects and products, fixed scope and budget, RAID logs and stage
                     gates, status reporting, a modern PMO
  ways-of-working/   agile in the AI era, Scrum without the theatre, forecasting, product partnership
  delivery/          source control, code review, testing, CI, releases, versioning,
                     feature flags, environments, database changes, GitOps, infra as code
  quality/           quality engineering, test strategy, test automation, TDD, performance,
                     security and accessibility testing, exploratory and acceptance testing,
                     test data and environments
  reliability/       service levels, incidents, postmortems, root cause analysis, rollbacks,
                     on-call, readiness, backup and recovery, resilience testing,
                     change management without a weekly board
  security/          secure development, supply chain, secrets, dependencies,
                     vulnerabilities, access, zero trust, post-quantum, third parties
  data/              data governance, data quality and contracts, security and privacy
  ai/                AI governance, AI engineering practices, AI architecture patterns,
                     building with AI, AI application security
  architecture/      architecture practice, decision records, RFCs, tech radar, APIs,
                     events and messaging, observability, scaling, legacy modernisation,
                     technical debt
  platform/          golden paths, developer platform, cloud native, cloud,
                     on-premises and air-gapped, FinOps, green software
  people/            onboarding, documentation, code assistants, knowledge sharing,
                     hiring, skills gap, career framework, sustainable pace
  measurement/       metrics (DORA, SLOs, SPACE), maturity model
  compliance/        control mapping, public sector, regulated industries
    regions/          US, UK, India, UAE/Saudi, China, Russia, Rwanda, Africa
leaders/       toolkits for CTOs, CIOs, product, programme and QA leaders, data and digital officers,
               architects, strategists, government, banks, small businesses and business executives: operating rhythm, decisions, board reporting,
               first 90 days, leading in the AI era, crisis leadership, due diligence, reading list
exercises/     189 true-or-false statements, 9 tabletop scenarios, 5 katas, 5 decision games
profiles/      adoption paths: SME, solo, startup, scale-up, enterprise, public sector, regulated
templates/     ready-to-copy files: GitHub, GitLab, Kubernetes, Argo CD, documents, CSV registers,
               product, project and test templates, printable plans for small businesses
assessment/    maturity self-assessment that runs from a TOML file
tools/         adopt script, the plain-language check and the page structure check
GLOSSARY.md    acronyms and terms in plain words
```

## What is different about it

**Three levels, not one rule book.** Each practice has a Foundation, a Standard and an Assured level. A profile picks the level for you, so a five-person startup and a central bank both get a correct answer from the same page.

**It works without the internet.** Each page says what changes on-premises and on air-gapped networks. Sovereignty and exit plans are requirements, not edge cases.

**Do the work once, show the evidence many times.** The [control mapping](playbook/compliance/control-mapping.md) links each practice to the standards auditors use. Review records, CI logs, signed builds and postmortems become the audit evidence.

**Strategy and transition, not only practices.** The [transition playbook](playbook/strategy/transition-playbook.md) moves an organisation in five phases, with a stop decision at every gate. It covers public budget years and regulator notice.

**Maturity assessment as code.** The [assessment](assessment/README.md) is a TOML file in your repository. Commit it each quarter and the history shows your progress.

**A toolkit for the people who decide.** The [leaders section](leaders/README.md) has meeting agendas, a one-page board scorecard, decision aids and a first 90 days plan. It also covers crisis leadership and due diligence.

**Practice, not only reading.** The [exercises](exercises/README.md) include a true-or-false quiz, timed tabletop scenarios, katas and decision games for leaders.

**Plain language, enforced.** Many readers use English as a second language. A check in CI rejects filler words and dashes used as punctuation, and the [glossary](GLOSSARY.md) explains every acronym.

**Change management without a weekly meeting.** [Change management](playbook/reliability/change-management.md) replaces a change advisory board with automated controls. It shows how those controls still meet ISO/IEC 27001 control 8.32 and SOC 2 CC8.1.

**Written for the AI era, without the hype.** When code is cheap, the bottleneck moves to deciding, reviewing and verifying. See [agile in the AI era](playbook/ways-of-working/agile-in-the-ai-era.md), [AI engineering practices](playbook/ai/ai-engineering-practices.md) and [leading in the AI era](leaders/leading-in-the-ai-era.md).

**Ready for the deadlines already on the calendar.** The [horizon scan](playbook/strategy/horizon-scan.md) covers EU Cyber Resilience Act reporting, EU AI Act high-risk dates and the move to post-quantum cryptography.

**People problems are engineering problems.** See [hiring](playbook/people/hiring.md), the [career framework](playbook/people/career-framework.md) and [sustainable pace](playbook/people/sustainable-pace.md). Teams that cannot keep good engineers do not get to the rest.

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
| Product | Marty Cagan's product risks, Teresa Torres's continuous discovery, the HEART framework (CHI 2010), Kohavi, Tang and Xu on controlled experiments |
| Project management | [PMBOK Guide](https://www.pmi.org/standards/pmbok), PRINCE2, DSDM MoSCoW, reference class forecasting, earned value (SAE EIA-748), [GOV.UK Service Manual](https://www.gov.uk/service-manual) phases |
| Testing | ISO/IEC/IEEE 29119, [OWASP ASVS](https://owasp.org/www-project-application-security-verification-standard/) and the Web Security Testing Guide, DORA continuous testing |
| Teams | Team Topologies |
| Public services | [UK Service Standard](https://www.gov.uk/service-manual/service-standard), [UK Technology Code of Practice](https://www.gov.uk/guidance/the-technology-code-of-practice), [US Digital Services Playbook](https://playbook.cio.gov/) |
| Conventions | [Conventional Commits](https://www.conventionalcommits.org/en/v1.0.0/), [SemVer](https://semver.org/), [Keep a Changelog](https://keepachangelog.com/en/1.1.0/), [MADR](https://adr.github.io/madr/), [OpenAPI](https://spec.openapis.org/oas/latest.html), [OpenTelemetry](https://opentelemetry.io/) |

This playbook is not legal advice. Where it mentions a regulation, read the regulation and talk to your counsel.

## Built on public work

The playbook stands on work that others shared openly. Each page links the sources it draws on. The main ones:

- [Google's engineering practices](https://google.github.io/eng-practices/) and the [Google SRE books](https://sre.google/books/)
- the [DORA research programme](https://dora.dev/)
- Team Topologies by Matthew Skelton and Manuel Pais
- the [UK Government Digital Service](https://www.gov.uk/service-manual) and the [US Digital Services Playbook](https://playbook.cio.gov/)
- the [OpenSSF](https://openssf.org/)
- the [GitLab handbook](https://handbook.gitlab.com/)
- the [Rust RFC process](https://rust-lang.github.io/rfcs/) and [Kubernetes enhancement proposals](https://github.com/kubernetes/enhancements)
- the [Diátaxis](https://diataxis.fr/) documentation framework
- the [Thoughtworks Technology Radar](https://www.thoughtworks.com/radar)

## Contributing

Corrections, templates and on-premises details from people who run real systems help most. Read [CONTRIBUTING.md](CONTRIBUTING.md) and [STYLE.md](STYLE.md). [GOVERNANCE.md](GOVERNANCE.md) says how recommendations change.

## Licence

Templates, scripts and code: MIT, copy them freely. Playbook text: CC BY 4.0, share and adapt with credit. See [LICENSE](LICENSE).
