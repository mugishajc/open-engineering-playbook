# Secure development

Build security into the normal delivery pipeline, organised around the four practice groups of the NIST Secure Software Development Framework (SSDF): prepare the organisation, protect the software, produce well-secured software, and respond to vulnerabilities. Security checks that run on every pull request cost minutes; vulnerabilities found by customers or attackers cost weeks and trust. Using the SSDF structure also answers customer, auditor and regulator questions with one body of evidence.

## Outcomes

Starting points. Tune them to your risk.

- 100% of repositories run secret scanning, dependency scanning and static analysis (SAST) in CI on every pull request.
- New services and significant design changes have a threat model before the first production release.
- Critical and high findings from CI block the merge, with an exception process that expires within 30 days.
- Every team has a named security champion who spends about 10% of their time on security work.
- Every engineer completes secure coding training once a year, matched to the languages they use.
- Vulnerability fix times meet the SLAs in [vulnerability management](vulnerability-management.md) for at least 90% of findings.

## The SSDF in one table

NIST SP 800-218 (SSDF version 1.1, February 2022) is the published version. A draft version 1.2 (SP 800-218r1 initial public draft, December 2025) adds practices, including PO.6. The table shows where each group lives in this playbook.

| SSDF group | What it asks | Where in this playbook |
|---|---|---|
| PO: Prepare the Organization | Define security requirements, roles, toolchains, criteria for security checks, and secure environments for development | This page; [access control](access-control.md); [secrets](secrets.md); [roles](../operating-model/roles.md) |
| PS: Protect the Software | Protect code from unauthorised access and tampering; provide a way to verify release integrity; archive each release | [Supply chain](supply-chain.md); [source control](../delivery/source-control.md) |
| PW: Produce Well-Secured Software | Design to meet requirements and reduce risk; review the design; reuse secure components; secure coding; secure build settings; code review and analysis; testing; secure defaults | This page; [dependencies](dependencies.md); [code review](../delivery/code-review.md); [testing](../delivery/testing.md) |
| RV: Respond to Vulnerabilities | Identify and confirm vulnerabilities; assess, prioritise and fix them; analyse causes to prevent repeats | [Vulnerability management](vulnerability-management.md); [root cause analysis](../reliability/root-cause-analysis.md) |

ISO/IEC 27001:2022 covers the same ground in Annex A controls 8.25 (secure development life cycle), 8.26 (application security requirements), 8.27 (secure system architecture and engineering principles), 8.28 (secure coding) and 8.29 (security testing in development and acceptance).

## Practice

### Foundation

1. **Turn on what is free.** Secret scanning with push protection, dependency alerts and automated update pull requests in your forge or CI (see [secrets](secrets.md) and [dependencies](dependencies.md)).
2. **One static analysis tool** in CI for your main language, with rules tuned so the team reads every finding. Start by blocking only high-confidence, high-severity rules.
3. **Pre-commit hooks** for secrets and formatting, using the [pre-commit configuration](../../templates/repo/.pre-commit-config.yaml).
4. **Protected main branch** and review on every change (see [code review](../delivery/code-review.md)).
5. **SECURITY.md** in every repository so people know how to report a vulnerability (see the [template](../../templates/repo/SECURITY.md)).
6. **Secure defaults.** Authentication on every endpoint unless explicitly public; TLS everywhere; no default passwords; least-privilege service accounts.

### Standard

1. **Security requirements by data class.** Use OWASP ASVS as the requirement catalogue. Pick a level per service tier and add the requirements to the definition of done.
2. **Threat model** new services, new data flows, new external integrations and changes to authentication or authorisation. Use the [STRIDE-based template](../../templates/docs/threat-model.md). A first threat model takes 1 to 2 hours with the team; update it when the design changes.
3. **Pipeline checks** on every pull request:

   | Check | Blocks merge on |
   |---|---|
   | Secret scanning | Any verified secret |
   | Dependency scanning (SCA) | Known exploited or critical vulnerability with a fix available |
   | SAST | High-confidence high or critical findings |
   | Infrastructure-as-code and container scanning | Critical misconfigurations (public storage, privileged containers, root user) |
   | Licence check | Licences on the deny list (see [dependencies](dependencies.md)) |

   Run DAST (dynamic scanning) against a test environment nightly, not on every pull request.
4. **Security champions.** One per team, with a monthly meeting across teams. Champions triage findings, lead threat models and spread fixes.
5. **Training that matches the stack.** Annual, hands-on, in the languages and frameworks the team uses, plus a session after any incident that exposed a gap.
6. **Measure maturity** once a year with OWASP SAMM and pick 2 or 3 practices to improve.

### Assured

Everything in Standard, plus:

1. **SSDF attestation.** Map each SSDF practice to your controls and evidence. US federal software suppliers attest to SSDF practices through CISA's Secure Software Development Attestation Form.
2. **Independent security testing** (penetration test) before first release of Tier 1 services and at least once a year, plus after major changes. Findings follow the vulnerability management SLAs.
3. **Separation of duties.** The author of a change cannot approve it. Changes to security-sensitive code paths (authentication, cryptography, payment, access control) need a second reviewer from the security champion group, enforced by CODEOWNERS.
4. **Evidence retained** from CI scans, threat models and pen tests for the audit period. Map them in [control mapping](../compliance/control-mapping.md).
5. **EU Cyber Resilience Act.** Manufacturers of products with digital elements must meet the essential requirements in Annex I. Most obligations apply from 11 Dec 2027; vulnerability and incident reporting applies from 11 Sep 2026 (see [vulnerability management](vulnerability-management.md)).

## Cloud, on-premises and air-gapped

- Every check on this page runs on self-hosted CI. Choose tools that run offline with a local rule set and vulnerability database, and update those databases through your approved transfer process at least weekly.
- In air-gapped networks, record the date of the vulnerability database each scan used. A scan against a 3-month-old database gives false comfort.
- Code assistants and hosted scanners that send code to an outside service need the same approval as any other data transfer (see [code assistants](../people/code-assistants.md)).

## Anti-patterns

| Anti-pattern | Fix |
|---|---|
| Scanner turned on with every rule, 4,000 findings, all ignored | Start with high-confidence rules that block. Add rules as the backlog clears. |
| Security review at the end, a week before launch | Threat model at design time; checks on every pull request. |
| Security team owns all fixes | Owning teams fix; champions and the security team help. |
| Pen test as the only security activity | Pen tests find what the pipeline missed. They do not replace it. |
| Exceptions with no expiry | Every exception has an owner and expires within 30 days, then is reviewed. |

## Templates

- [Threat model](../../templates/docs/threat-model.md)
- [SECURITY.md](../../templates/repo/SECURITY.md)
- [Vulnerability disclosure policy](../../templates/docs/vulnerability-disclosure-policy.md)
- [Pre-commit configuration](../../templates/repo/.pre-commit-config.yaml)
- [CI workflow](../../templates/github/workflows/ci.yml)

## Sources

- NIST SP 800-218, *Secure Software Development Framework (SSDF) Version 1.1*: https://csrc.nist.gov/pubs/sp/800/218/final
- NIST SSDF project page (including the version 1.2 draft): https://csrc.nist.gov/projects/ssdf
- CISA, Secure Software Development Attestation Form: https://www.cisa.gov/secure-software-attestation-form
- OWASP Application Security Verification Standard: https://owasp.org/www-project-application-security-verification-standard/
- OWASP SAMM: https://owaspsamm.org/
- ISO/IEC 27001:2022: https://www.iso.org/standard/27001
- Regulation (EU) 2024/2847 (Cyber Resilience Act): https://eur-lex.europa.eu/eli/reg/2024/2847/oj
