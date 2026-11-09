# Changelog

All notable changes to the Open Engineering Playbook are listed here. It uses calendar versions (`YYYY.MM`). The format follows [Keep a Changelog 1.1.0](https://keepachangelog.com/en/1.1.0/).

## [2026.11.2] - 2026-11-09

Product management, project management and testing join the playbook. Four expert challenges followed: a chief product officer on the product pages, a head of quality and testing on the quality pages, a programme director on the project management pages, and a board chair, a bank chief risk officer and a permanent secretary on the decision-making and board pages for leaders. Each finding was fixed in place, or handed to the page that owns the topic and fixed there.

### Added

- A product area with six pages: [product strategy](playbook/product/product-strategy.md), [product discovery](playbook/product/product-discovery.md), [roadmaps and prioritisation](playbook/product/roadmaps-and-prioritisation.md), [product metrics and experiments](playbook/product/product-metrics-and-experiments.md), [pricing and packaging](playbook/product/pricing-and-packaging.md) and [launch and adoption](playbook/product/launch-and-adoption.md). They cover B2B products, internal platforms and public services where users cannot choose another provider, and what changes when code is cheap to produce.
- A project management area with five pages: [projects and products](playbook/project-management/projects-and-products.md), [planning fixed scope and budget](playbook/project-management/planning-fixed-scope-and-budget.md), [risks, RAID logs and stage gates](playbook/project-management/risks-raid-and-stage-gates.md), [status reporting](playbook/project-management/status-reporting.md) and [a modern PMO](playbook/project-management/modern-pmo.md). They cover reference class forecasting, contingency and management reserve, fixed-price contracts with systems integrators, public procurement change limits, go/no-go, cutover and rollback, and benefits after go-live.
- Seven quality pages: [test strategy](playbook/quality/test-strategy.md), [test automation](playbook/quality/test-automation.md), [performance testing](playbook/quality/performance-testing.md), [security testing](playbook/quality/security-testing.md), [accessibility testing](playbook/quality/accessibility-testing.md), [exploratory and acceptance testing](playbook/quality/exploratory-and-acceptance-testing.md) and [test data and environments](playbook/quality/test-data-and-environments.md).
- Leaders pages [for product leaders](leaders/for-product-leaders.md), [for programme and portfolio leaders](leaders/for-programme-and-portfolio-leaders.md) and [for QA and test leaders](leaders/for-qa-and-test-leaders.md).
- Templates in `templates/product/`, `templates/project/` and `templates/quality/`: a product strategy on a page, an opportunity solution tree, an experiment brief, a product one-pager, a launch checklist, a project charter, a RAID log, a status report, a stage gate checklist, lessons learned, a test strategy, a UAT sign-off, a performance test plan and an exploratory testing charter. `tools/adopt.sh` copies them to `docs/templates/product/`, `docs/templates/project/` and `docs/templates/quality/`.
- A decision game: [the red project before go-live](exercises/decision-games/red-project-before-go-live.md).
- Assessment: areas `product` and `project-management` with 6 questions each, and `quality.risk-based-strategy`. The SME profile skips product and gets one owner-level project question (`project-management.sme-system-change`): a one-page plan with a way back before a big IT change.
- Quiz: Product and Project management areas with 10 statements each, and 6 more quality statements on performance, security, accessibility, exploratory testing and test data. 94 true and 95 false out of 189.
- 27 problems in PROBLEMS.md, 63 glossary terms (from A/B test to vanity metric), product, programme, project manager and QA rows in the README's "Pick your door", and a learning path for product, programme and quality leaders.

### Changed

- The playbook index has 16 areas: Product and Project management are areas 3 and 4. The maturity model, profiles and scoring cover them. The scale-up target is now at least 11 of the 16 areas at Standard within a year.
- Quality questions link to the new pages, and the accessibility question now asks for manual keyboard, zoom and screen reader checks as well as automated ones. The assessment allows 4 to 7 questions per area.
- Leaders pages: "off track" for a programme now means outside the board's tolerance (forecast cost more than 10% over budget, or the 85% date past the plan); overdue P0 and P1 security findings must be zero; DORA terms aligned to "failed deployment recovery time"; starting points for large product bets and for concurrent launches.
- Leaders pages on [decision making](leaders/decision-making.md), [board and executive reporting](leaders/board-and-executive-reporting.md), [business executives](leaders/for-business-executives.md) and [government](leaders/for-government.md) now cover staged funding with kill criteria, speed against control, escalation thresholds for what reaches the board, what the board decides, and the decisions accounting officers keep.
- Notice periods in [API standards](playbook/architecture/api-standards.md) now cover removing user-facing features.
- Links from related pages to the new ones: suppliers and contracts (acceptance, warranty and delay damages terms), business case (benefit owners and baselines), public sector (tender flexibility, US accessibility dates), regulated industries (price and value rules), release management (mobile store releases), developer platform and decision rights.

## [2026.11.1] - 2026-11-09

An expert review of the first release. Five reviewers read the playbook as a CTO, an enterprise architect, a CISO, an SRE lead and an adoption panel (a clinic owner, a ministry digital lead, a corporate trainer and a plain-language editor). Each finding was fixed, or rejected with a written reason.

### Added

- `GLOSSARY.md`: acronyms and terms in plain words, from ADR to zero trust, including DORA metrics versus the EU DORA regulation. Linked from README, STYLE and the leaders section.
- Playbook pages: [technology budget and cost](playbook/strategy/technology-budget-and-cost.md), [suppliers and contracts](playbook/strategy/suppliers-and-contracts.md), [events and messaging](playbook/architecture/events-and-messaging.md) and [resilience testing](playbook/reliability/resilience-testing.md).
- Privacy and exit templates in `templates/security/`: records of processing, a personal data breach register, a data protection impact assessment and an exit plan. A legal floor in [data security and privacy](playbook/data/data-security-and-privacy.md): levels never lower a legal duty.
- Templates for small businesses in `templates/sme/`: a printable first-hour plan with a downtime procedure, IT provider questions, an online services list and a one-page staff AI use policy.
- A solo GitHub ruleset that a single engineer can merge with; `tools/adopt.sh --solo` copies it and `--updates dependabot|renovate` copies one update bot only.
- Assessment: profile rules in the question bank (`[profiles.<name>]` with `skip_areas`, `area_order` and `overlays_raise_target`, and per-question `only_profiles` and `skip_profiles`). The SME profile now skips the six areas that need in-house engineers and asks 14 Foundation questions written for owners and IT providers, so a clinic or school gets actions such as "turn on multi-factor authentication for every email account" first.
- Assessment: report links point at the public repository when the answers file lives elsewhere.
- Quiz: a "Business owners" area, `--save FILE` to keep a record of each session and `--retry-missed FILE` to replay misses. `--check` now fails when true and false answers are unbalanced, overall, per area, or for statements with absolute words.
- Exercises: learning paths by role for trainers, and a retry storm tabletop.
- `tools/check_structure.py`, which fails when a page lacks a required section, and a `--long-sentences N` warning in `tools/plain_lint.py`.
- Leaders: choosing an IT provider and the cost type of each essential control; hiring and reviewing your technology leader; a section for chief digital officers; a large groups section in the enterprise profile; public sector and data rows and newer editions in the reading list.
- GOVERNANCE: continuity rules, a 3-maintainer target and how the second approval works until there are two maintainers. CONTRIBUTING: a translation policy and every check, including the exercises.

### Changed

- One set of numbers everywhere, matching the practice pages: on-call at least 6 people per 24 by 7 rotation (one week in six; 8 at one site if the same people cover backup), flaky tests quarantined in 24 hours and fixed in 14 days, setup from the README in under one hour, first review response within one working day with a median under 4 working hours, governance answers within 5 working days, restore tests every 3 months (monthly for Tier 1).
- Enterprise profile follows the transition phases: quarter 1 is Assess and Decide; pilots, SLOs, the group incident process and SBOMs arrive wave by wave, in waves of 2 to 5 teams.
- Scale-up profile: at least 10 of the 14 areas at Standard within a year, as its year 1 check already said.
- README quick start explains the Python 3.11 requirement and the alternatives (`python3.12`, `py -3` on Windows), offers a no-tools start for owners and executives, and suggests a quarterly return. Both scripts now say how to fix an old Python.
- Quiz: "it depends", negative and recall-only statements rewritten; jargon in explanations spelled out; 82 true and 81 false out of 163.
- SME first-hour plan: keep evidence, call the insurer earlier, switch to a downtime procedure.
- AI Act dates on the data officers page now cite Regulation (EU) 2026/1744.
- Principle 4 is "Golden paths, not gates"; principle 9 says levels never lower a legal duty.
- Many more fixes across the security, reliability, delivery, architecture and strategy pages: sourced claims, corrected dates and aligned targets.

### Removed

- The quiz statement on "one week in six", replaced by a statement that tests the principle (`reliability.three-person-rota`).

## [2026.11] - 2026-11-09

First public release.

### Added

- Playbook with 14 areas and 83 pages: strategy, operating model, ways of working, delivery, quality, reliability, security, data, AI, architecture, platform, people, measurement and compliance
- Three levels for every practice: Foundation, Standard, Assured
- Adoption profiles: SME, Solo, Startup, Scale-up, Enterprise, with Public sector and Regulated overlays
- PROBLEMS.md: an index from 89 real problems to the pages that address them
- Leaders section with 15 toolkits: operating rhythm, decision making, first 90 days, board and executive reporting, crisis leadership, strategy and architecture toolkits, technical due diligence, leading in the AI era, a reading list, and pages for data and digital officers, government, financial services, small and medium businesses and business executives
- AI era pages: agile in the AI era (beyond Scrum theatre), AI engineering practices, AI architecture patterns, and AI era sections in code review, CI, release management, incident management, quality, runbooks, scaling, access control and metrics
- Exercises: 153 true-or-false statements with a terminal quiz and playable pages, 8 tabletop scenarios with a facilitator guide, 5 katas and 4 decision games
- SME profile for businesses that use software but do not build it
- Transition playbook for moving an organisation to a new way of building software, with exit criteria and a stop decision at each gate
- Portfolio and capacity planning, architecture practice, IT governance (ISO/IEC 38500, COBIT 2019, ITIL 4) and a horizon scan to 2030
- AI area: governance (EU AI Act as amended in 2026, ISO/IEC 42001, NIST AI RMF), building with AI from pilot to production, and controls for the OWASP Top 10 for LLM Applications
- Security pages on zero trust, post-quantum readiness (NIST IR 8547, October 2026) and third-party and SaaS risk
- Reliability pages on root cause analysis and rollbacks
- People pages on hiring, closing skills gaps in Kubernetes, cloud, security and AI, career frameworks and sustainable pace
- Control mapping to ISO/IEC 27001:2022, SOC 2, NIST SSDF, SLSA, OpenSSF OSPS Baseline, EU CRA, NIS2, the EU DORA regulation, the EU AI Act and ISO/IEC 42001
- Templates for GitHub and GitLab: pull and merge request templates, issue forms, CODEOWNERS, rulesets, CI, release automation, OpenSSF Scorecard, SBOM generation and signing
- Kubernetes service baseline and Argo CD application templates
- Document templates: decision records, RFCs, postmortems, runbooks, incident updates, production readiness reviews, threat models, vulnerability disclosure policy, vendor risk questionnaire, code assistant policy, AI use case assessment, data classification, interview scorecard
- Registers as CSV: risks, RACI, technical debt, cryptographic inventory, career ladder, tech radar
- Self-assessment tool (`assessment/assess.py`) with 84 questions across 14 areas that reports the level reached, the gap to your profile's target and the next five actions
- `tools/adopt.sh`, which copies templates into an existing repository without overwriting files
- Plain-language check used in the playbook's own CI and reusable by adopters
