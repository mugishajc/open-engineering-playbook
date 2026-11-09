# Secrets

Keep secrets out of source control, issue them from a secret manager, prefer short-lived credentials over long-lived ones, and rotate what remains on a schedule. Leaked credentials are one of the most common ways attackers get in, and a key committed to git stays in its history and every clone. Short-lived, automatically issued credentials remove most of the risk and most of the rotation work.

## Outcomes

Starting points. Tune them to your risk.

- Zero secrets in source control: secret scanning runs on every push and pull request, and on full history once a quarter.
- 100% of CI pipelines that deploy to cloud or call Vault use OIDC federation, not stored long-lived keys.
- A leaked production credential is revoked within 1 hour of detection.
- Every remaining static secret has an owner and a rotation date; at least 95% are within their rotation interval.
- No human holds a long-lived production database password.

## What counts as a secret

Passwords, API keys and tokens, private keys (TLS, SSH, signing), cloud access keys, database connection strings with credentials, OAuth client secrets, webhook signing secrets, encryption keys, session signing keys, and recovery codes.

## Practice

### Foundation

1. **Never in git.** Not in code, config files, `.env` files, notebooks, test fixtures or CI files. Add `.env` and key file patterns to `.gitignore`.
2. **Scan before commit and in CI.** A pre-commit hook (for example gitleaks) stops most leaks on the laptop (see the [pre-commit configuration](../../templates/repo/.pre-commit-config.yaml)). CI scans again because hooks can be skipped. Turn on push protection in your forge where it exists.
3. **Store secrets in a manager**, not in a shared document or chat: your cloud provider's secret manager, HashiCorp Vault or OpenBao, or the CI system's protected and masked variables as a minimum.
4. **When a secret leaks, revoke first.** Rotate or revoke the credential immediately, then check logs for use, then clean history. Deleting the commit does not un-leak the secret; someone may already have cloned it.
5. **Use a team password manager** for human credentials, with MFA.

### Standard

1. **OIDC federation from CI.** GitHub Actions and GitLab CI issue a signed OIDC token per job. Configure the cloud provider or Vault to trust it, scoped to the repository, branch or environment. The job gets short-lived credentials (minutes to hours) and nothing long-lived is stored in CI.
2. **Workload identity in runtime.** Services get credentials from the platform (cloud workload identity, Kubernetes service account tokens exchanged with Vault), not from environment variables set by hand.
3. **Dynamic secrets** for databases and cloud access where possible: Vault or OpenBao create a credential per request with a time-to-live of 1 to 24 hours (starting point) and revoke it automatically.
4. **Rotation intervals** for secrets that must stay static (starting points):

   | Secret | Rotate |
   |---|---|
   | Service API keys and tokens | Every 90 days, automated |
   | Database passwords for services | Every 90 days, or replace with dynamic secrets |
   | TLS certificates | Automated, with lifetimes of 90 days or less (ACME or an internal CA) |
   | Signing keys (artifacts, tokens) | Every 1 to 2 years, with a published rollover plan |
   | Any secret held by someone who leaves | Within 1 working day of their departure, within 4 hours for production and admin secrets (matches [access control](access-control.md)) |

   Public TLS certificate lifetimes are falling under CA/Browser Forum ballot SC-081v3: a maximum of 200 days from 15 Mar 2026, 100 days from 15 Mar 2027 and 47 days from 15 Mar 2029. Any certificate still renewed by hand will become an outage. Automate renewal now and alert when any certificate is within 14 days of expiry.

5. **Kubernetes.** Kubernetes Secrets are only base64-encoded by default. Turn on encryption at rest, restrict who can read Secrets with RBAC, and sync from a secret manager with a tool such as External Secrets Operator. For secrets that must live in git (for example GitOps configuration), encrypt them with SOPS and a KMS or age key.
6. **Scan full history** of every repository once a quarter, and scan container images and build artifacts for embedded secrets.

### Assured

Everything in Standard, plus:

1. **Keys in hardware.** Root and signing keys live in an HSM or a cloud KMS with HSM backing. Nobody can export them.
2. **Separation of duties.** People who administer the secret manager cannot read application secrets; access to read production secrets is just-in-time and logged (see [access control](access-control.md)).
3. **Audit trail.** Every read of a production secret is logged with identity and time, kept for the audit period, and alerts fire on unusual access. This supports ISO/IEC 27001:2022 controls 5.17 (authentication information), 8.24 (use of cryptography) and 8.15 (logging).
4. **Inventory.** A register of all static secrets with owner, purpose, location and rotation date, reviewed quarterly. The same inventory feeds [post-quantum readiness](post-quantum-readiness.md).

## Cloud, on-premises and air-gapped

- **On-premises:** Vault or OpenBao, run in high-availability mode, with auto-unseal through an HSM. Back up its storage and test restore (see [backup and recovery](../reliability/backup-and-recovery.md)); losing it can stop every service.
- **Air-gapped:** OIDC federation still works inside the network if your CI and secret manager both run there; configure Vault's JWT auth to trust your self-hosted GitLab or Gitea instance's OIDC issuer.
- **Break-glass secrets** (root passwords, unseal keys) are split between at least 2 people (for example Shamir key shares) and stored offline in separate safes.

## Anti-patterns

| Anti-pattern | Fix |
|---|---|
| Cloud access key with admin rights stored in CI variables | OIDC federation, scoped to one repository and environment. |
| Leaked key "fixed" by force-pushing to remove the commit | Revoke first. Assume it was copied. |
| One shared service account password used by five teams | One identity per service; dynamic credentials. |
| Secrets passed as plain environment variables and printed in logs | Mount from the secret manager; mask in CI; scan logs. |
| Rotation never done because it breaks things | Automate rotation and test it in staging every cycle. |

## Templates

- [Pre-commit configuration](../../templates/repo/.pre-commit-config.yaml)
- [CI workflow](../../templates/github/workflows/ci.yml)
- [Crypto inventory](../../templates/docs/crypto-inventory.csv)

## Sources

- OWASP Secrets Management Cheat Sheet: https://cheatsheetseries.owasp.org/cheatsheets/Secrets_Management_Cheat_Sheet.html
- GitHub Docs, OpenID Connect in GitHub Actions: https://docs.github.com/en/actions/concepts/security/openid-connect
- GitLab Docs, OpenID Connect (OIDC) authentication using ID tokens: https://docs.gitlab.com/ci/secrets/id_token_authentication/
- HashiCorp Vault documentation: https://developer.hashicorp.com/vault/docs and OpenBao: https://openbao.org
- Kubernetes, encrypting confidential data at rest: https://kubernetes.io/docs/tasks/administer-cluster/encrypt-data/
- gitleaks: https://github.com/gitleaks/gitleaks and SOPS: https://github.com/getsops/sops
- CA/Browser Forum, Ballot SC-081v3, reducing certificate validity periods: https://cabforum.org/2025/04/11/ballot-sc081v3-introduce-schedule-of-reducing-validity-and-data-reuse-periods/
