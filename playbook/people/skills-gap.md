# Skills gap

"We adopted Kubernetes, cloud and AI faster than we could train people, and now three engineers hold everything together." Close the gap from both sides: reduce the skills each team needs by hiding complexity behind golden paths and the platform, and grow the skills that remain through pairing, hands-on labs, rotations and protected learning time. Measure skill coverage with a team skills matrix so you know where a single departure would hurt, and fix those spots first.

## Outcomes

Starting points. Tune them to your organisation.

- Every critical skill for each production system is held at "can do unaided" level by at least 2 people (a bus factor of 2 or more).
- Each team updates its skills matrix every 6 months and closes at least 2 single-person gaps per half-year.
- Every engineer has at least 4 hours a fortnight of protected learning time, and teams report using it.
- At least 80% of on-call engineers have taken part in a game day or hands-on lab in the last 12 months.
- Time for a new team to deploy its first service on the platform falls each quarter, a sign that less specialist skill is needed.

## Where the gaps usually are

| Area | Typical gap |
|---|---|
| Kubernetes and cloud native | Networking, storage, upgrades, debugging pods, security contexts |
| Cloud | Identity and access design, networking, cost, managed service limits |
| Security | Threat modelling, secure code review, supply chain, incident handling |
| Data | Data modelling, pipelines, data quality, privacy law in practice |
| AI | Evaluating model output, retrieval design, prompt injection, cost control |
| Operations | Observability, incident command, capacity planning |

## Techniques that work

### Reduce the skills needed

- The cheapest skill to teach is the one nobody needs. A [golden path](../platform/golden-paths.md) that sets up Kubernetes manifests, pipelines, scanning and dashboards means product engineers need to understand them, not build them.
- The [developer platform](../platform/developer-platform.md) team holds deep specialist skills so stream-aligned teams do not each need them.
- Prefer managed services where hosting rules allow. Each self-hosted component adds skills you must keep.

### Learn by doing, together

- **Pairing and mob programming.** Pair a specialist with a learner on real work. For a skill the whole team needs, work as a group on one problem for a few days.
- **Hands-on labs.** Short, self-paced exercises on a safe environment: break a deployment and fix it, rotate a secret, trace a slow request.
- **Game days.** Practise failures in a controlled way: kill a node, expire a certificate, restore a backup. Everyone learns the system and the runbooks get better (see [incident management](../reliability/incident-management.md)).
- **Rotations.** Engineers spend 4 to 12 weeks in the platform, security or SRE team, then return to their own team with the skills.

### Structure the learning

- **Internal academies.** A short curriculum per area (for example 6 sessions on Kubernetes operations), taught by internal experts with labs, repeated each quarter.
- **Communities of practice.** Guilds keep skills current after the course ends (see [knowledge sharing](knowledge-sharing.md)).
- **Certifications as a signal, not a goal.** CNCF certifications (CKA, CKAD and CKS for Kubernetes) and cloud provider certifications give a structured syllabus and an external check. They do not prove someone can run your systems. Fund them for people who want them, and never make them a promotion gate on their own.
- **Hire for learning ability.** When hiring, assess how people learn and reason as well as what they know today (see [hiring](hiring.md)).

### Get outside help, and transfer it

- For on-premises products and distributions, buy vendor support and use it to train your people, not to replace them. Write contract terms that include knowledge transfer and joint troubleshooting.
- When partners or contractors build systems, the contract requires documentation, runbooks and paired handover before final payment.

## The team skills matrix

- List the skills each system needs as rows, people as columns. Rate each cell: 0 none, 1 learning, 2 can do with help, 3 can do unaided, 4 can teach.
- Any skill with fewer than 2 people at level 3 or above is a gap. Rank gaps by the criticality of the system.
- Use the matrix to plan pairing, rotations and training, and to inform hiring. Never use it to rank or rate individuals.
- Keep it in the team's repository or a shared sheet. Review it every 6 months, and after anyone joins or leaves.

## Practice

### Foundation

- A simple skills matrix for the team. Pair on anything only one person knows.
- Protected learning time every fortnight.

### Standard

- Skills matrices per team, with gaps fed into the platform roadmap (to remove the need) and into training plans (to grow the skill).
- Internal academy tracks for the 2 or 3 biggest gaps. Game days at least every quarter.
- Rotation programme into the platform or security team.
- A learning budget per engineer per year, spent at the engineer's choice within broad rules.

### Assured

- Key-person risk for critical systems is recorded in the risk register when the bus factor is below 2, with an owner and a date.
- Training required for privileged roles (for example production administration, incident command) is recorded with dates, as evidence.
- Contracts with vendors and integrators include knowledge transfer obligations and are checked at handover.

## Cloud, on-premises and air-gapped

- On-premises and air-gapped estates need skills that cloud providers would otherwise supply: storage, networking, hardware, cluster upgrades, certificate authorities. Plan for them explicitly or buy support.
- Build training labs inside isolated networks, or on a separate network with the same software versions, because engineers cannot learn on public cloud sandboxes and transfer the habits directly.

## Anti-patterns

| Anti-pattern | Fix |
|---|---|
| Sending people on a course, then giving them no time to use it | Pair the course with real work in the following weeks. |
| Every team must master Kubernetes | Golden paths and a platform team hold the depth. |
| Certifications as the target | Certifications as a structured syllabus. Judge skill by work. |
| The one expert never takes leave because nobody else can cover | Pairing, rotations and a bus factor of 2 for critical systems. |
| Vendor engineers fix everything and leave nothing behind | Knowledge transfer in the contract. |

## Templates

- [Onboarding checklist](../../templates/docs/onboarding-checklist.md)
- [Career ladder](../../templates/people/career-ladder.csv)
- [Runbook](../../templates/docs/runbook.md), for game days

## Sources

- Linux Foundation and CNCF certifications (CKA, CKAD, CKS): https://www.cncf.io/training/certification/
- Matthew Skelton and Manuel Pais, Team Topologies (2019), on cognitive load and enabling teams: https://teamtopologies.com/
- DORA capabilities, including learning culture: https://dora.dev/capabilities/
