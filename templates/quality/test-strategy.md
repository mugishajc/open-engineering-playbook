# Test strategy: [product or service]

<!--
How to use: the team writes this together after a 60-minute risk workshop, with a quality engineer.
Keep it to 1 to 3 pages. Replace every [bracket]. Delete rows that do not apply and say why in
section 9. Review every 6 months, and when a trigger in section 10 happens.
Guidance: playbook/quality/test-strategy.md
-->

| Field | Value |
|---|---|
| Product or service | [name] |
| Tier | [Tier 1 / Tier 2 / Tier 3] |
| Owning team | [team] |
| Quality engineer | [name] |
| Product owner | [name] |
| Data class | [from the data classification] |
| Last reviewed | [YYYY-MM-DD] |
| Next review | [YYYY-MM-DD, at most 6 months later] |

## 1. What we are protecting

The 3 to 5 quality characteristics that matter most (ISO/IEC 25010:2023), and why.

| Characteristic | Why it matters here |
|---|---|
| [for example functional suitability] | [tax must be calculated correctly to the cent] |
| [security] | [holds personal and payment data] |
| [interaction capability] | [public service; legal accessibility duty] |

## 2. Risks

Likelihood and impact from 1 to 3. Impact 3: money or data wrong, legal duty broken, personal data exposed, safety, Tier 1 outage. Likelihood 3: new or complex code, new team or technology, frequent change, or recent defects here. Score = likelihood times impact.

| # | Risk | Who is harmed | L | I | Score | Checks that catch it (layer) | Owner |
|---|---|---|---|---|---|---|---|
| R1 | [VAT rounded wrongly on mixed baskets] | [customers, finance] | 2 | 3 | 6 | [unit tests with decision table; property test; exploratory each release] | [name] |
| R2 | [user reads another tenant's invoices] | [customers] | 2 | 3 | 6 | [authorisation matrix tests; pen test] | [name] |
| R3 | | | | | | | |

Depth by score: 6 or 9, two automated layers or more plus exploratory and specialist review; 3 or 4, the cheapest automated layer; 1 or 2, smoke checks or accept and record in section 9. Any impact 3 risk gets at least one automated check and a production alert, whatever its score.

## 3. Test layers and budgets

| Layer | Tool | Runs on | Time budget | Owner |
|---|---|---|---|---|
| Static checks | [ ] | Every commit | Under 1 minute | |
| Unit and component | [ ] | Every pull request | Under 5 minutes | |
| Integration (real dependencies in containers) | [ ] | Every pull request | Within the 10-minute pipeline | |
| Contract | [ ] | Both sides, every pull request | Under 2 minutes | |
| End to end ([number] critical paths, 5 to 20) | [ ] | Before production deploy and on a schedule | Under 15 minutes | |
| Production checks (synthetic probes, SLO alerts) | [ ] | Continuously | n/a | |

Critical paths covered end to end: [list]

Flaky tests: quarantined within 24 hours, fixed or deleted within 14 days. Dashboard: [link]. Owner: [name]

Platform and device matrix (covers [__]% of sessions, from [analytics source, date]):

| Platform | Versions or models | Emulated on every pull request | Real device before release |
|---|---|---|---|
| [browsers] | | | |
| [Android] | [lowest-specification device supported: ] | | |
| [iOS] | | | |
| [oldest app version still supported against the API] | | Contract tests | |

## 4. Non-functional testing

| Area | Target | How and when tested | Owner |
|---|---|---|---|
| Performance | [p95 under ___ ms at 2 times peak; see performance test plan] | [ ] | |
| Security | [ASVS level ___; pipeline checks; pen test date] | [ ] | |
| Accessibility | [WCAG 2.2 AA; axe-core in CI; manual checks; audit date] | [ ] | |
| Resilience | [fault hypotheses tested this quarter] | [ ] | |
| AI features | [evaluation set size, thresholds; see quality engineering] | [ ] | |

## 5. Exploratory, acceptance and usability testing

- Exploratory sessions: [which risks get chartered sessions, how often]
- Acceptance: [story acceptance examples / continuous UAT through previews and flags / formal UAT for this release, with reason]
- Usability and testing with disabled people: [when]

## 6. Environments and data

| Environment | Used for | Data source | Differences from production (parity list link) |
|---|---|---|---|
| Local and CI containers | | Factories | |
| Preview per pull request | | Seeded synthetic | |
| Staging | | Seeded synthetic | |
| Performance | | Synthetic at volume | |

Production-derived data: [none / approved masked copy, approval record link, deletion date]

## 7. Release gates

- [ ] Required checks green (list): [ ]
- [ ] End-to-end checks green against the release artifact
- [ ] No open severity 1 or 2 defect without written acceptance by [role]
- [ ] Chartered exploratory session for each high-risk change
- [ ] Performance and accessibility budgets met
- [ ] [Assured: independent review of test evidence for high-risk changes]

## 8. Evidence kept

| Evidence | Where | Kept for |
|---|---|---|
| Test results per release, with commit and artifact digest | [ ] | [retention period] |
| Exploratory session notes | [ ] | |
| UAT sign-off | [ ] | |
| Pen test and audit reports | [ ] | |
| [Assured: requirement to test traceability] | [ ] | |

## 9. Not tested, and why

| What | Why | Risk accepted by | Review date |
|---|---|---|---|
| [ ] | [ ] | [name, role] | [YYYY-MM-DD] |

## 10. Review triggers

Review this strategy early when any of these happen: a new data class or integration, a major architecture change, an escaped severity 1 or 2 defect, a new legal or contract duty, a change of tier.
