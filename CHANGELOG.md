# Changelog

All notable changes to the Open Engineering Playbook are listed here. It uses calendar versions (`YYYY.MM`). The format follows [Keep a Changelog 1.1.0](https://keepachangelog.com/en/1.1.0/).

## [2026.11] - 2026-11-09

First public release.

### Added

- Playbook with fourteen areas and about ninety pages: strategy, operating model, ways of working, delivery, quality, reliability, security, data, AI, architecture, platform, people, measurement and compliance
- Three levels for every practice: Foundation, Standard, Assured
- Adoption profiles: Solo, Startup, Scale-up, Enterprise, with Public sector and Regulated overlays
- PROBLEMS.md: an index from about seventy real problems to the pages that address them
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
