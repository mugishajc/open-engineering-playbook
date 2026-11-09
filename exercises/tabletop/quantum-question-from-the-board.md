# Tabletop: the quantum question from the board

A board member has read an article about quantum computers and asks, in the middle of a board meeting, whether your members' data is exposed and what you are doing about it. There is no outage and no attacker, only a question you cannot fully answer, a budget conversation and a salesperson with a three-week offer. This scenario tests whether leaders can explain a long-term risk honestly, avoid both panic and dismissal, and start the cheap, necessary work now.

| | |
|---|---|
| Audience | CTO or CIO, CISO, chief architect, CFO, head of procurement, and one or two board members or executives playing themselves |
| Time | 60 minutes (10 brief, 35 play, 15 debrief) |
| Read first | [Post-quantum readiness](../../playbook/security/post-quantum-readiness.md), [horizon scan](../../playbook/strategy/horizon-scan.md), [decision making](../../leaders/decision-making.md) |
| Facilitator notes | [Facilitator guide](facilitator-guide.md) |

## Setup

The organisation is a pension fund administrator. It holds records for 900,000 members, some of which it must keep for the member's lifetime plus several decades. Members use an online portal. Payment files to banks are signed with keys held in a hardware security module (HSM). Scanned member documents are encrypted and stored with a third-party archive under a 15-year contract. A replacement of the core administration system is planned: contract signature in 2027, go-live in 2029, expected life 10 to 15 years.

Nobody has listed where the organisation uses public-key cryptography. All organisations, people and numbers here are fictional.

## Injects

### T+0 (board meeting, 14:00): the question

A non-executive director says: "I read that quantum computers will break the encryption banks use. Can someone read our members' data today? Do we need to do anything this year?" The chair gives the CTO five minutes.

**Decide:**
- What do you say in five minutes that is true, short and does not overclaim in either direction?
- What do you promise to bring back, and by when?

Facilitator note: a good answer covers three points. Nobody can say when a large enough quantum computer will exist. Attackers can record encrypted traffic today and decrypt it later ("harvest now, decrypt later"), which matters for data that must stay secret for 10 years or more. NIST has published replacement standards (FIPS 203, 204 and 205) and plans to deprecate RSA and elliptic-curve algorithms after 2030 and disallow them after 2035.

### T+15 (14:15): the CFO

The CFO asks: "What will it cost? Can it wait until the new core system goes live in 2029, so we do it once?"

**Decide:**
- What costs almost nothing and should start now? What is expensive and can be planned?
- What does the 2027 core system contract need to say about cryptography?
- How do you answer "do it once" when the new system will run past 2035?

### T+30 (next morning): what do we actually have?

The CISO's team spends two hours on a first list. They find: TLS on the member portal, a site-to-site VPN to the outsourced call centre, the HSM that signs payment files, single sign-on tokens, encrypted backups, and the document archive, which uses keys and algorithms nobody internally can name. The HSM vendor has published no post-quantum roadmap. The archive supplier's account manager does not understand the question.

**Decide:**
- Which items carry data that must stay secret for 10 years or more? Which go first?
- What do you ask the HSM vendor and the archive supplier, in writing?
- Who owns the inventory, and what format do you keep it in?

### T+60 (one week later): the offer and the regulator

Two things arrive on the same day:
- A vendor offers a "quantum-safe encryption appliance" for 400,000, with a discount if signed within three weeks.
- The financial supervisor sends a questionnaire on post-quantum readiness, due in six weeks.

**Decide:**
- Do you buy the appliance? What would you need to know first?
- What can you honestly say to the supervisor in six weeks?
- What goes to the next board meeting?

### Optional injects

- **T+20:** Another director says: "This is fifteen years away. Why spend a penny now?"
- **T+40:** An engineer proposes replacing AES-256 encryption on backups "to be quantum safe".
- **T+70:** The core system bidders' responses arrive. Two of three do not mention cryptographic agility at all.

## Discussion questions

1. Which of your data must stay confidential for 10 years or more? Where does it travel encrypted today?
2. Could you change the cryptographic algorithm in your three most important systems by configuration, or would it need new code or hardware?
3. Which of your suppliers hold keys or encrypt data on your behalf? Have you asked them about their post-quantum plans?
4. What contracts will you sign in the next two years for systems that will still run after 2035?
5. How do you tell a board about a risk with no fixed date without causing panic or being ignored?

## What good looks like

- A five-minute board answer that is honest about uncertainty and specific about the dates and standards that are known ([post-quantum readiness](../../playbook/security/post-quantum-readiness.md)).
- A cryptographic inventory started this quarter, owned by a named person, using the [crypto inventory template](../../templates/docs/crypto-inventory.csv), with confidentiality lifetime recorded for each item.
- Long-lived data and harvest-now-decrypt-later exposure prioritised first, including data held by suppliers.
- Supplier questions sent in writing to the HSM vendor and archive supplier, and added to procurement ([vendor risk questionnaire](../../templates/docs/vendor-risk-questionnaire.md)).
- The 2027 core system contract requires crypto-agility and a supplier post-quantum roadmap.
- No purchase of a single-vendor appliance before the inventory shows what problem it would solve ([build, buy or adopt](../../playbook/strategy/build-buy-adopt.md)).
- Symmetric encryption with 128-bit or stronger keys left alone; effort goes to public-key algorithms.
- A board-level owner and yearly progress report against the 2028, 2031 and 2035 milestones.

## Scoring rubric

| Criterion | 0 | 1 | 2 |
|---|---|---|---|
| Board answer | Panic or dismissal | Accurate but vague | Accurate, short, names harvest-now-decrypt-later, known dates and next step |
| Cost framing | "Wait until 2029" accepted, or large spend promised | Some split of cheap and expensive work | Cheap work starts now; large items planned with procurement |
| Inventory | Not started | Started without owner or lifetime data | Owner, template and confidentiality lifetime per item |
| Suppliers and contracts | Not considered | Questions asked verbally | Written questions; 2027 contract requires crypto-agility |
| Vendor offer | Signed in three weeks | Delayed without criteria | Declined or deferred until the inventory defines the need |

Maximum 10.

## Follow-up actions

- Name an executive owner for post-quantum readiness and add it to the risk register.
- Complete a first [crypto inventory](../../templates/docs/crypto-inventory.csv) for Tier 1 systems within 90 days.
- Send the six supplier questions from [post-quantum readiness](../../playbook/security/post-quantum-readiness.md#questions-to-ask-suppliers) to every supplier that holds keys or encrypts data for you.
- Add crypto-agility and a post-quantum roadmap to the requirements for every system procured from now on.
- Enable hybrid post-quantum key exchange on external TLS endpoints where your libraries support it.
- Put post-quantum progress on the board's yearly agenda.
