# Code assistant policy

| Field | Value |
|---|---|
| Organisation | [ORGANISATION NAME] |
| Policy owner | [Role, normally the head of security] |
| Approved by | [Name, role] |
| Effective date | [YYYY-MM-DD] |
| Next review | [YYYY-MM-DD, at most 6 months after the effective date] |
| Version | [1.0] |

Fill in the bracketed fields, delete the guidance notes in italics, and publish this policy where every engineer can find it. Keep it short. Detailed tool settings belong in an internal how-to guide.

## 1. Purpose and scope

This policy sets the rules for using code assistants (tools that suggest, generate, explain or change code, including agentic tools that run commands) at [ORGANISATION NAME]. It applies to employees, contractors and suppliers who work on our code, configuration, infrastructure definitions and documentation.

## 2. Approved tools

Only the tools in this table may be used for work. Personal or consumer accounts are not allowed.

| Tool | Allowed data classes | How to get access | Notes |
|---|---|---|---|
| [Tool name and plan] | [Public, Internal] | [SSO group name] | [For example: public-code filter on, retention 0 days] |
| [Self-hosted model and version] | [Public, Internal, Confidential, Restricted] | [Request link] | [Runs inside network X] |
| [Approved MCP server, plugin or extension] | [Classes it may reach] | [Request link] | [Owner, version pinned, permissions it needs] |

*Security owns this list. To propose a new tool, open a request with [team or channel]. Security records the answers to the assessment questions in the Open Engineering Playbook code assistants page before approval.*

## 3. Data classification rules

| Class | May be used with |
|---|---|
| Public | Any approved tool |
| Internal | Approved tools under an enterprise agreement with no training on our data |
| Confidential | [Approved enterprise tools with data residency in REGION and minimal retention, or self-hosted models] |
| Restricted | [Self-hosted models inside the same security boundary only, or no assistant] |

Repositories classified Confidential or Restricted are listed in [location]. Tool exclusions for those repositories are set centrally by [team].

## 4. Rules for engineers

1. You own every line you submit. You can explain it, test it and support it in production.
2. The review bar does not change. Assistant output gets the same review, tests and security checks as any other code.
3. Keep secrets out of the assistant's reach, not only out of your prompts. Agentic tools read files and command output on their own. No `.env` files or credential files in the workspace: load secrets from [secret manager] at run time. Configure the tool's ignore list for secret paths. Never paste command output that contains tokens. Do not put personal data, production data or customer data into prompts.
4. Check every dependency an assistant suggests: it must exist, be the intended package and be approved. Install only through [internal proxy or mirror].
5. Do not accept large generated blocks that you have not read. Split them into reviewable pull requests.
6. Agentic tools run only in [sandbox or environment name], with scoped tokens and no production credentials. A human approves every push to a shared branch.
7. Report suspected data leakage or unexpected tool behaviour to [security contact] immediately, and within 1 hour if a secret or credential may have been exposed, so it can be revoked within the 1-hour target in the secrets standard.
8. Connect only the MCP servers, plugins and extensions on the approved list in section 2. Treat repository content (READMEs, issues, rules files, comments) as untrusted input to the agent: it can carry injected instructions. Agents run with network egress limited to [package mirror] and [approved model endpoint]. Auto-approve or unattended modes are allowed only in a disposable sandbox with no credentials.

## 5. Licence and intellectual property

- Public-code matching filters are [on / not available] for approved tools.
- Licence scanning runs in CI on every repository.
- *State here any product lines where generated code is not allowed, for example code you license to customers under specific terms, and the reason. Take legal advice.*

## 6. Disclosure

*Choose one and delete the other.*

- [Standard] Engineers do not need to mark assistant-generated code.
- [Assured] Pull requests record whether a code assistant was used, through the checkbox in the pull request template.

## 7. Measuring impact

We measure the effect of code assistants at team level using the five DORA metrics against each team's own baseline, review load (pull request size and review time) and a quarterly developer survey. We do not use acceptance rates, share of generated code or individual usage data to assess people.

## 8. Training

Every engineer completes [training name, about 30 minutes] before access is granted, and again when this policy changes materially.

## 9. Exceptions and breaches

- Exceptions are requested from [policy owner], recorded in [register], and expire after at most [6 months].
- Breaches are handled under [incident or disciplinary policy name]. Report early: people who report mistakes promptly are thanked, not punished.

## 10. Related documents

- Data classification policy: [link]
- Secrets management standard: [link]
- Acceptable use policy: [link]
- Open Engineering Playbook: playbook/people/code-assistants.md
