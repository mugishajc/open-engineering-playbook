# Access control

Put every human and machine identity behind single sign-on, require phishing-resistant MFA for anything that touches production, grant the least access that does the job, and make production admin rights temporary. Stolen credentials and forgotten accounts are among the most common ways in. Central identity, short-lived elevation and regular reviews close most of those doors and give auditors the evidence they ask for.

## Outcomes

Starting points. Tune them to your risk.

- 100% of engineering tools (forge, CI, cloud consoles, observability, ticketing) use SSO through one identity provider.
- 100% of people with production or admin access use phishing-resistant MFA (FIDO2 or WebAuthn security keys or passkeys).
- Zero people hold standing production admin rights; elevation is just-in-time, approved and expires within 4 hours.
- Leavers lose all access within 4 hours of their departure time for privileged roles and within 1 working day for everyone else.
- Access reviews happen every quarter for production and sensitive data, with 100% of entitlements confirmed or removed.
- Break-glass accounts are tested every quarter and every use raises an alert.

## Practice

### Foundation

1. **One identity provider.** Use your workspace or directory provider (or Keycloak on-premises) as the single source of identities. Turn off local accounts in tools that support SSO.
2. **MFA everywhere,** starting with email, the forge, the cloud console and the password manager. Prefer security keys or passkeys over SMS codes.
3. **Least privilege by default.** New people get read access to code and the tools for their team. Write access to production comes later, when needed.
4. **No shared accounts** for people. Each person has their own identity so actions are traceable.
5. **Offboarding checklist** run on each person's last day, covering every tool not behind SSO.

### Standard

1. **SSO plus automated provisioning.** Use SCIM or directory sync so joiners, movers and leavers update every connected tool automatically. HR changes drive access, not tickets.
2. **Role-based access.** Define roles per team and environment (for example `payments-developer`, `payments-prod-operator`) and grant access to groups, never to individuals.
3. **Phishing-resistant MFA** (FIDO2 or WebAuthn) mandatory for admins, production access and the identity provider itself.
4. **Just-in-time production access.** Engineers request elevation for a reason linked to a ticket or incident; a peer or the on-call lead approves; access expires within 4 hours (starting point); every action is logged. Tools include cloud provider privileged access features and Vault or OpenBao dynamic credentials. On-call engineers can self-approve during a declared incident, reviewed afterwards.
5. **Non-human identities.** Every service, pipeline, bot and AI agent has its own identity with an owner, scoped permissions and short-lived credentials (see [secrets](secrets.md) and [AI application security](../ai/ai-application-security.md)). No personal tokens in automation.
6. **Break-glass accounts.** At least 2 emergency admin accounts per critical system that do not depend on the identity provider. Credentials and hardware keys are stored offline in separate safes. Any use alerts the security team. Test login every quarter, then rotate.
7. **Quarterly access reviews** for production, customer data and admin roles. Managers or service owners confirm each entitlement. Unconfirmed access is removed after 10 working days.
8. **Source code access** follows the same model: write access by team, admin rights limited to 2 or 3 people per organisation (see [source control](../delivery/source-control.md)).

### Assured

Everything in Standard, plus:

1. **Separation of duties** written as rules: authors cannot approve their own changes, people who request access cannot approve it, security administrators cannot also administer the audit logs.
2. **Privileged session recording** for production shells and database consoles, kept for the audit period.
3. **Customer data access** needs a recorded reason and is reported to data owners monthly (see [data security and privacy](../data/data-security-and-privacy.md)).
4. **Evidence.** Keep provisioning logs, review results, elevation approvals and break-glass use for the audit period. This supports ISO/IEC 27001:2022 controls 5.15 (access control), 5.16 (identity management), 5.17 (authentication information), 5.18 (access rights), 8.2 (privileged access rights) and 8.5 (secure authentication), and SOC 2 CC6.1 to CC6.3.
5. **Device trust.** Production access only from managed devices that meet a posture check (see [zero trust](zero-trust.md)).

## In the AI era

AI agents, coding agents and chat bots now act on systems with real permissions. Treat each one as a non-human identity with the same rigour as a production service, plus limits that reflect how easily its instructions can be hijacked (see [AI application security](../ai/ai-application-security.md) and [AI engineering practices](../ai/ai-engineering-practices.md)).

| Rule | Starting point |
|---|---|
| One identity per agent and per environment | No shared "ai-bot" account across teams; no agent uses a person's token or session |
| Named human owner | Recorded in the identity provider; ownerless agent identities are disabled within 10 working days |
| Short-lived credentials | Issued per task or per session through OIDC federation or a secret manager; 1 hour or less, no static API keys |
| Scoped tool permissions | Each tool grants one action on one resource type (for example `tickets:comment`, not `tickets:*`); read-only by default |
| Acting for a user | The agent carries the user's authorisation as well as its own; the narrower of the two applies |
| Human approval | Required for anything that deletes data, moves money, changes access, deploys to production or sends data outside the organisation |
| Logging | Every tool call logged with the agent identity, the user it acted for, the parameters and the approver |
| Reviews | Agent identities are in the quarterly access review, and any permission unused for 30 days is removed |

A worked example: a support agent that drafts refund replies gets read access to the orders of the customer in the current ticket and permission to create a draft refund. Issuing the refund stays a human action in the payments tool. If the agent is tricked by a prompt injection in a customer email, the worst outcome is a wrong draft, not a payment.

Code assistants that open pull requests follow the same rules: a bot identity with write access to branches only, never to protected branches, and a human approval on every merge (see [code assistants](../people/code-assistants.md)).

## Cloud, on-premises and air-gapped

- **On-premises identity:** Keycloak or your directory service as the identity provider, with SAML or OIDC to each tool. Run it highly available; if it fails, nobody can sign in, so break-glass accounts matter more.
- **Air-gapped:** a separate identity domain inside the network with no trust to the corporate directory, so a compromise outside cannot spread in. Provision accounts by an approved process, and review them on the same quarterly cycle.
- **Cloud:** use the provider's organisation-level controls to block long-lived access keys for people, require MFA, and enforce SSO into accounts.

## Anti-patterns

| Anti-pattern | Fix |
|---|---|
| Ten engineers with permanent cloud admin "for incidents" | Just-in-time elevation with self-approval during declared incidents. |
| Access reviews that rubber-stamp 400 rows | Review by group and role; highlight unused access (no use in 90 days) for removal. |
| SMS codes for admin accounts | Security keys or passkeys. |
| Leaver's personal access token still runs the nightly job | Non-human identities for automation, owned by a team. |
| Break-glass password in a wiki page | Offline, split storage; alert on use; quarterly test. |
| SSO on the main tools, local accounts on the rest | Inventory every tool; remove or federate local accounts. |

## Templates

- [Onboarding checklist](../../templates/docs/onboarding-checklist.md)
- [CODEOWNERS](../../templates/github/CODEOWNERS)
- [Default branch ruleset](../../templates/github/rulesets/default-branch.json)

## Sources

- NIST SP 800-63B, *Digital Identity Guidelines: Authentication and Lifecycle Management*: https://pages.nist.gov/800-63-4/sp800-63b.html
- NIST SP 800-207, *Zero Trust Architecture*: https://csrc.nist.gov/pubs/sp/800/207/final
- ISO/IEC 27001:2022: https://www.iso.org/standard/27001
- AICPA, Trust Services Criteria (CC6): https://www.aicpa-cima.com/resources/download/2017-trust-services-criteria-with-revised-points-of-focus-2022
