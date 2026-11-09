# Tabletop: supplier breach

A SaaS supplier you rely on announces it was breached, the notice sat unread in a shared mailbox for six hours, the supplier then stops answering, and your own logs show its integration doing things it should not. This scenario tests whether you know what each supplier can reach, whether you can cut a supplier off without stopping your own business, and how your data protection duties run when the breach is someone else's.

| | |
|---|---|
| Audience | Security, IT and SaaS administrators, the engineering lead for the affected integration, procurement or vendor management, legal or the data protection officer, customer support lead, communications |
| Time | 90 minutes (10 brief, 60 play, 20 debrief) |
| Read first | [Third-party and SaaS risk](../../playbook/security/third-party-and-saas-risk.md), [secrets](../../playbook/security/secrets.md), [access control](../../playbook/security/access-control.md), [incident management](../../playbook/reliability/incident-management.md) |
| Facilitator notes | [Facilitator guide](facilitator-guide.md) |

## Setup

The organisation is an online furniture retailer selling in three countries, with 300 staff and 40 engineers. Customer support runs on a hosted helpdesk and live chat product. The helpdesk holds three years of customer conversations and is connected to the retailer's orders API through an OAuth integration, so agents can look up orders and issue refunds without leaving the helpdesk.

The supplier register lists the helpdesk as Tier 2. Its contract says the supplier will notify security incidents "promptly", without a number of hours. All organisations, people and numbers here are fictional.

## Injects

### T+0 (Wednesday 14:30): the news story

An engineer shares a news article in the team chat: the helpdesk supplier confirms "unauthorised access to a subset of customer environments" between 2 and 9 November. A search of the shared `it-admin@` mailbox finds the supplier's notice, received at 08:32: "As a precaution, rotate all API tokens and review integration activity. We will share more details as our investigation continues."

**Decide:**
- Is this an incident for you? What severity? Who is incident commander?
- When did you become aware: 08:32 or 14:30? Why does it matter?
- What do you do in the next 15 minutes, before you know whether you were affected?

### T+15 (14:45): what can the supplier reach?

The team checks. The OAuth integration has read and write scopes on the orders API, including refunds, with no expiry. The helpdesk holds names, addresses, phone numbers and order histories of about 210,000 customers. Single sign-on protects staff log-ins, but six old local administrator accounts still exist in the helpdesk.

**Decide:**
- Is Tier 2 the right tier for this supplier? What does that say about the register?
- Revoke the OAuth token now? Support then cannot see orders or issue refunds; 90 agents work until 22:00.
- What else do you rotate or disable?

### T+30 (15:00): your logs say yes

The orders API logs show the integration's identity made 3,400 order lookups between 3 and 8 November from addresses outside the supplier's published ranges. Fourteen refunds, totalling 6,230, went to payment cards that had never been used on the account before.

**Decide:**
- You are now affected. What changes?
- How do you keep support working with the token revoked? (Read-only access? A temporary manual refund process with two-person approval?)
- Who contacts the payment provider about the 14 refunds?

### T+60 (15:30): the supplier goes quiet

Your account manager's email returns an out-of-office reply until next Monday. The supplier's support portal says "We are experiencing very high volumes." No indicators of compromise, no list of affected customers, no timeline. Legal points out that you are the data controller for your customers' data; the supplier is your processor. Under GDPR Article 33 your clock runs from when you became aware.

**Decide:**
- What do you notify to the supervisory authority, and when, with the supplier silent?
- How do you escalate with the supplier? Who in your organisation has a relationship above the account manager?
- What does the contract give you, and what does it not?

### T+90 (16:00): the customers notice

Customers forward emails that quote their real order numbers and ask them to "confirm delivery payment" on a lookalike site. The payment provider's risk team calls about the refund pattern and says it may pause refunds on your account while it reviews.

**Decide:**
- What do you tell customers, today, so they do not pay the phishing site?
- What do you need to show the payment provider to keep refunds running?
- What goes on the website and what goes by email?

### Optional injects

- **T+20:** An engineer finds a 2024 helpdesk ticket where someone pasted a production database password to "help debug a customer issue".
- **T+70:** The marketing team reports that its email platform uses the same helpdesk contact data through a second, forgotten integration.
- **T+100:** The supplier finally sends an indicator list. One address on it also appears in your VPN logs.

## Discussion questions

1. Which suppliers can read or change data in your production systems? Through what credentials, with what scopes, and do they expire?
2. Who reads security notices from suppliers, and how fast? What happens at weekends?
3. Which of your supplier contracts give a breach notification time in hours?
4. Could you cut off your three most important suppliers in an hour and keep working? How?
5. What customer data have you put into suppliers' systems that they never needed?

## What good looks like

- The supplier register tiers by what the supplier can reach, so an integration with write access to orders is Tier 1 ([third-party and SaaS risk](../../playbook/security/third-party-and-saas-risk.md)).
- Supplier security notices go to a monitored security address, not a shared IT mailbox.
- Integrations use their own scoped, expiring credentials, with logging that shows where calls came from ([access control](../../playbook/security/access-control.md), [secrets](../../playbook/security/secrets.md)).
- A tested fallback for each Tier 1 supplier, so cutting it off is a business decision taken in minutes, not hours.
- Legal or the data protection officer told within 1 hour, and your 72-hour clock run on your own facts, not the supplier's pace ([incident management: Assured](../../playbook/reliability/incident-management.md#assured)).
- Contracts that state breach notification within 72 hours or less, audit rights and named security contacts ([vendor risk questionnaire](../../templates/docs/vendor-risk-questionnaire.md)).
- Customers warned quickly and specifically about the phishing emails ([incident update template](../../templates/docs/incident-update.md)).

## Scoring rubric

| Criterion | 0 | 1 | 2 |
|---|---|---|---|
| Initial response | Waited for the supplier to confirm impact | Started after T+30 | Rotated, revoked or limited credentials within 15 minutes |
| Knowing the blast radius | Could not say what the supplier reached | Partial list | Full list of data, scopes and integrations by T+30 |
| Business continuity | Support stopped with no plan | Improvised workaround | Planned degraded mode with controls on refunds |
| Regulatory and legal | Waited for the supplier | Clock noted, no draft | DPO by T+60, awareness time recorded, notice drafted |
| Supplier escalation | Waited for the account manager | Generic tickets | Escalated through a named executive route, requests in writing |
| Customer protection | No message | Late or vague warning | Specific phishing warning sent the same day |

Maximum 12.

## Follow-up actions

- Re-tier every supplier by data and production access; move any supplier with write access to production data to Tier 1.
- Give each integration its own identity with least-privilege scopes, expiry and source-address checks.
- Route supplier security notices to a monitored security mailbox with an on-call owner.
- Add 72-hour breach notification, audit rights and a security contact to Tier 1 and Tier 2 contracts at renewal.
- Write and test an exit or fallback plan for each Tier 1 supplier ([build, buy or adopt](../../playbook/strategy/build-buy-adopt.md)).
- Scan supplier systems you control for secrets pasted into tickets, and rotate them ([secrets](../../playbook/security/secrets.md)).
