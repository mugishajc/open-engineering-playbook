# Security testing

The problem: "We passed the annual penetration test, and three months later a researcher found an injection flaw in a form we added after it." A yearly test sees one moment; the code changes every day. Layer security testing: automated scans on every pull request, dynamic scans every night, security requirements from OWASP ASVS at a level that matches the data, turned into tests the team owns, and expert human testing for what automation cannot find. The pipeline checks and their blocking rules are set in [secure development](../security/secure-development.md#standard); this page covers how to test, verify and get value from testers.

## Outcomes

Starting points. Tune them to your risk.

| Signal | Starting target |
|---|---|
| Repositories with secret scanning, dependency scanning (SCA) and static analysis (SAST) on every pull request | 100%, as in [secure development](../security/secure-development.md) |
| Web applications and APIs with an authenticated dynamic scan (DAST) against a test environment | Nightly |
| Services with an ASVS level recorded and every requirement at that level mapped to a test, a review step or a manual check | 100% of Tier 1 and Tier 2 |
| Endpoints covered by automated authorisation tests (other user, other tenant, lower role, no session) | 100% of endpoints that read or change data |
| New scanner findings triaged (confirmed, false positive, or accepted with a reason) | Within 7 days, by the weekly security champion triage |
| Penetration test of Tier 1 services | Before first release, at least yearly, and after major changes |
| Penetration test findings fixed within the [vulnerability management](../security/vulnerability-management.md) SLAs | At least 90% |
| Penetration test findings that could be automated and now have a regression test or pipeline rule | 100% |

## What each kind of test finds

No single method finds everything. Pick by what each one sees.

| Method | Finds | Misses | When |
|---|---|---|---|
| Secret scanning | Keys, tokens and passwords in code and history | Secrets stored elsewhere | Pre-commit and every pull request |
| SCA (software composition analysis) | Known vulnerable or deny-listed dependencies | Flaws in your own code | Every pull request and daily against the SBOM |
| SAST (static analysis) | Code patterns: injection, unsafe deserialisation, weak cryptography | Business logic and authorisation flaws; produces false positives | Every pull request |
| Infrastructure-as-code and container scanning | Public storage, privileged containers, open ports | Runtime drift | Every pull request |
| Authorisation tests (written by the team) | Users reaching other users' or tenants' data; missing role checks | Flaws in endpoints nobody listed | Every pull request |
| DAST (dynamic scanning) | Runtime issues: headers, injection, misconfiguration, exposed endpoints | Logic flaws; pages it cannot reach without login set up | Nightly, authenticated |
| Fuzzing | Crashes and memory errors in parsers, file formats and protocol handlers | Logic flaws | Continuously for parsers; nightly |
| Penetration test | Chained weaknesses, business logic abuse, what the scanners missed | Anything outside scope or time box | Yearly and after major change |
| Threat-led or red team test | Whether attackers can reach goals, and whether you detect and respond | Breadth: it follows one path | Where regulators require it, or for mature Tier 1 estates |
| Vulnerability disclosure and bug bounty | What outside researchers find in production | Areas researchers do not look at | Always on, through [SECURITY.md](../../templates/repo/SECURITY.md) |

## Triage and noise

Scanners that cry wolf get ignored, and then the real finding is ignored too. Run them so that a red build means something.

- **Block only on new findings.** When you add a scanner to an existing codebase, record the existing findings as a baseline. Fix them through the backlog with the [vulnerability management](../security/vulnerability-management.md) SLAs. The pipeline blocks only findings the change introduces, so teams can turn the tool on today.
- **Promote and demote rules with data.** Start SAST with high-confidence, high-severity rules only. Then use the promotion rule in [secure development](../security/secure-development.md#foundation): a rule blocks when at least 8 of its last 10 findings were real.
- **Prioritise SCA findings by exploitability**, not by the Common Vulnerability Scoring System (CVSS) score alone: the CISA Known Exploited Vulnerabilities (KEV) catalog, the Exploit Prediction Scoring System (EPSS) and whether the vulnerable function is reachable from your code, as [vulnerability management](../security/vulnerability-management.md) sets out. Many dependency alerts are in code your service never calls, and reachability analysis shows which.
- **One queue.** Send findings from every tool into one tracker, de-duplicated by location and rule, so the same issue from SAST and DAST is one ticket.
- **Suppress in the open.** Mark each false positive in the tool or in code, with a reason, the person and a review date. A security champion reviews a sample each month; a suppression without a reason is removed.
- **Measure the noise**: share of findings marked false positive per tool and per rule. Tune or remove the rules that generate most of it.

## Requirements as tests: OWASP ASVS

The OWASP Application Security Verification Standard (ASVS) lists security requirements for web applications and APIs at three levels. Version 5.0 was released in 2025. Pick a level per service from its data class and tier:

| ASVS level | Use for |
|---|---|
| Level 1 | Every application: the minimum |
| Level 2 | Applications that handle personal, financial or business-sensitive data. Most services. |
| Level 3 | The highest-value systems: large payments, health records, critical infrastructure, where a breach causes serious harm |

Then make the level testable:

1. **Map each requirement** to how you verify it: an automated test (session timeout, password rules, access control), a configuration check in the pipeline (TLS settings, security headers), a design review item, or a manual check in the penetration test.
2. **Reference requirements by version and number** in tests and tickets, in the form ASVS suggests (`v5.0.0-` followed by the requirement number). Requirement numbers changed between versions, so an unversioned reference becomes wrong.
3. **Add the level's requirements to the definition of done** for stories that touch authentication, sessions, access control, input handling or cryptography.
4. **Mobile apps** use the OWASP Mobile Application Security Verification Standard (MASVS) and its testing guide (MASTG) in the same way.

## Authorisation tests

Broken object-level authorisation is first in the OWASP API Security Top 10 (2023): an attacker changes an ID in a request and reads or changes someone else's record. Scanners rarely find it, because they do not know which records belong to whom. Teams can test it cheaply.

1. Write an access matrix: roles down the side, actions and resources across, with "allow" or "deny" in each cell. Include "another tenant's record" as a resource.
2. Generate tests from the matrix. For each endpoint that reads or changes data, call it as the owner, as another user with the same role, as a user in another tenant, as a lower role and with no session. Assert the expected allow or deny.
3. Fail the build when a new endpoint has no row in the matrix.

## Dynamic scanning in the pipeline

- **Passive baseline scan** (for example the ZAP baseline scan) on each deploy to a preview or staging environment. It watches traffic and does not attack.
- **Active, authenticated scan** nightly against a non-production environment with synthetic data. Give the scanner test accounts for each role, and import the OpenAPI definition so it reaches every API endpoint. Check the scanner stayed logged in for the whole run: a scan that lost its session after 10 minutes tested only the login page.
- **Time-box it.** A full active scan of a large application can run for many hours. Scan the endpoints that changed each night, and the whole application weekly, so the results arrive before the team's next working day.
- **Never run active scans against production** without approval, a time window and a stop person. They submit forms and can change or delete data.
- **Tune and record.** Mark false positives with a reason and a review date. Findings go into the same queue and SLAs as every other vulnerability.

## Penetration testing that pays for itself

- **Scope from risk**, not from a standard list: the new payment flow, the tenant boundary, the admin interface, the integration with the new supplier. Name in-scope systems, roles, test accounts and the environment.
- **Rules of engagement** signed before work starts: dates, source addresses, what is forbidden (denial of service, real customer data), emergency contacts, and how to stop.
- **Give testers the design and the code** (grey-box or white-box testing). They spend their days finding flaws, not mapping your system.
- **Methodology.** Ask testers to follow the OWASP Web Security Testing Guide for web applications and NIST SP 800-115 for the overall approach, and to say which parts they covered.
- **Qualified testers.** Use firms with recognised accreditation for your market, for example CREST, or the UK National Cyber Security Centre (NCSC) CHECK scheme for UK public-sector systems. Rotate the firm or the testers every 2 to 3 years (starting point) so fresh eyes see the system.
- **A useful report**: steps to reproduce, evidence, severity with CVSS, and the root cause class. A retest is part of the contract.
- **Close the loop.** Fix within the [vulnerability management](../security/vulnerability-management.md) SLAs. Turn each finding class into a test, a SAST rule or an authorisation matrix row, so it cannot come back unnoticed.

Penetration tests find what the pipeline missed. They do not replace it.

## In the AI era

Features built on language models add prompt injection, data leakage and excessive agency to the attack surface. Add attack cases to the evaluation set that runs in CI (see [quality engineering](quality-engineering.md#in-the-ai-era)), and red team customer-facing features before launch and every 6 months, as set out in [AI application security](../ai/ai-application-security.md). Code assistants can also write vulnerable code fluently, so keep SAST and authorisation tests as the gate, not the assistant's word.

## Practice

### Foundation

- Turn on the free checks: secret scanning with push protection, dependency alerts, one SAST tool. See [secure development](../security/secure-development.md#foundation).
- Authorisation tests for every endpoint that reads or changes data, including "another user's record".
- A ZAP baseline scan against staging or a preview environment.
- A [SECURITY.md](../../templates/repo/SECURITY.md) so outsiders can report what you missed.
- **Solo and Startup:** if a penetration test is not affordable yet, work through the authentication, session and access control sections of the OWASP Web Security Testing Guide yourself before you take payments or hold personal data at scale. Commission an external test before your first large customer or regulated launch.

### Standard

- An ASVS level per service, mapped to tests and checks; Level 2 for most services.
- An access matrix per service with generated authorisation tests.
- Nightly authenticated DAST; fuzzing for parsers and file handling.
- Penetration tests for Tier 1 services before first release, yearly and after major changes, with findings turned into regression tests.
- Security champions triage scanner findings weekly (see [secure development](../security/secure-development.md#standard)).

### Assured

- ASVS Level 3 for the highest-value systems, with each requirement's verification recorded per release.
- Independent penetration testing by accredited testers who are not part of the development team.
- **Sector rules.** PCI DSS v4.0.1 (requirement 11.4) requires internal and external penetration testing at least every 12 months and after significant changes for systems in its scope, plus segmentation tests where segmentation reduces scope. EU financial entities identified by their authorities must run threat-led penetration testing (TLPT) at least every 3 years under EU DORA, with TIBER-EU as the reference; see [for financial services](../../leaders/for-financial-services.md).
- Scan results, test reports and retest evidence kept for the audit period. They support ISO/IEC 27001:2022 Annex A 8.29 and NIST SSDF PW.7 (review and analyse code) and PW.8 (test executable code).

## Cloud, on-premises and air-gapped

- **Cloud:** read your provider's penetration testing policy before a test. Providers generally let you test your own resources within published rules and forbid attacks on their shared infrastructure and denial-of-service testing.
- **On-premises:** testers need network access, accounts and a desk or a controlled remote route. Agree this in the rules of engagement.
- **Air-gapped:** scanners run offline with local rule sets and vulnerability databases; record the database date on every scan (see [secure development](../security/secure-development.md#cloud-on-premises-and-air-gapped)). Testers work on site, and their tools come in through the reviewed import process.

## Anti-patterns

| Anti-pattern | Fix |
|---|---|
| The yearly penetration test is the security testing | Pipeline checks every day; the penetration test finds what they missed. |
| Unauthenticated DAST that sees only the login page | Test accounts for each role and the OpenAPI definition. |
| Authorisation tested only by the penetration testers | An access matrix with generated tests in CI. |
| The same finding in three yearly reports | Turn each finding class into a test or a pipeline rule. |
| A black-box test with no design or code, to "be realistic" | Grey-box or white-box: more findings per day paid. |
| ASVS level chosen, then never checked | Map each requirement to a verification and record the result per release. |
| Active scan run against production on a Friday afternoon | Non-production with synthetic data, or an approved window with a stop person. |

## Templates

- [Threat model](../../templates/docs/threat-model.md)
- [SECURITY.md](../../templates/repo/SECURITY.md)
- [Vulnerability disclosure policy](../../templates/docs/vulnerability-disclosure-policy.md)
- [Test strategy](../../templates/quality/test-strategy.md), security section

## Sources

- OWASP Application Security Verification Standard: https://owasp.org/www-project-application-security-verification-standard/
- OWASP Web Security Testing Guide: https://owasp.org/www-project-web-security-testing-guide/
- OWASP API Security Top 10 (2023): https://owasp.org/API-Security/editions/2023/en/0x11-t10/
- OWASP Mobile Application Security (MASVS and MASTG): https://mas.owasp.org/
- ZAP: https://www.zaproxy.org/
- NIST SP 800-115, *Technical Guide to Information Security Testing and Assessment*: https://csrc.nist.gov/pubs/sp/800/115/final
- NIST SP 800-218 Secure Software Development Framework: https://csrc.nist.gov/pubs/sp/800/218/final
- PCI Security Standards Council, PCI DSS document library: https://www.pcisecuritystandards.org/document_library/
- Regulation (EU) 2022/2554 (EU DORA), Article 26: https://eur-lex.europa.eu/eli/reg/2022/2554/oj
- European Central Bank, TIBER-EU framework: https://www.ecb.europa.eu/paym/cyber-resilience/tiber-eu/html/index.en.html
- CREST: https://www.crest-approved.org/
- NCSC CHECK penetration testing: https://www.ncsc.gov.uk/information/check-penetration-testing
- OSS-Fuzz: https://google.github.io/oss-fuzz/
