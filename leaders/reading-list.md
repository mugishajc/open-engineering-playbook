# Reading list

These are the books that senior technology leaders, architects and planners return to. Read the three in your role's "start here" row first, then pick by the problem in front of you. Each entry says why the book matters and which playbook page puts it into practice. The list is short on purpose: a book earns a place only if it changes how you decide.

## When to use this

- You have stepped into a new role and want the ideas your peers take for granted.
- You are building a reading group for staff engineers, architects or a leadership team.
- A playbook page cites a book and you want the reasoning behind the practice.

| Role | Start here |
|---|---|
| CTO, CIO or executive | Accelerate; Good Strategy Bad Strategy; High Output Management |
| Principal or staff engineer | The Staff Engineer's Path; Software Engineering at Google; Working Effectively with Legacy Code |
| Architect | Fundamentals of Software Architecture; Designing Data-Intensive Applications; Building Evolutionary Architectures |
| Strategist or planner | Good Strategy Bad Strategy; Team Topologies; The Goal |
| Reliability or delivery lead | Site Reliability Engineering; Continuous Delivery; Release It! |
| Security lead | Security Engineering; Release It!; Thinking, Fast and Slow |

## CTOs and executives

| Book | Why it matters | Playbook page |
|---|---|---|
| Accelerate (Nicole Forsgren, Jez Humble, Gene Kim, 2018) | The research behind the DORA delivery metrics and the capabilities linked to better delivery performance. It gives leaders evidence instead of opinion. | [Metrics](../playbook/measurement/metrics.md) |
| High Output Management (Andy Grove, 1983) | A manager's output is the output of the teams they lead and influence. It describes the objectives and key results method and how to run meetings that produce decisions. | [Strategy toolkit](strategy-toolkit.md) |
| The First 90 Days (Michael Watkins, 2003) | How to diagnose the situation you are joining, learn fast and secure early wins in a new leadership role. | [First 90 days](first-90-days.md) |
| The Manager's Path (Camille Fournier, 2017) | Each stage of engineering management, from mentoring one person to leading as CTO, and what changes at each step. | [Roles](../playbook/operating-model/roles.md) |
| An Elegant Puzzle (Will Larson, 2019) | Practical systems for running engineering organisations: sizing teams, running migrations, planning. | [Portfolio and capacity](../playbook/strategy/portfolio-and-capacity.md) |
| The Phoenix Project (Gene Kim, Kevin Behr, George Spafford, 2013) | A novel about an IT organisation in crisis that makes flow, work in progress and unplanned work easy to explain to non-engineers. | [Transition playbook](../playbook/strategy/transition-playbook.md) |

## Principal and staff engineers

| Book | Why it matters | Playbook page |
|---|---|---|
| The Staff Engineer's Path (Tanya Reilly, 2022) | What staff engineers do beyond writing code: seeing the big picture, running cross-team projects and raising the level of others. | [Career framework](../playbook/people/career-framework.md) |
| Staff Engineer (Will Larson, 2021) | The different shapes the staff role takes, with first-hand accounts from people in it. Useful when defining the role in a career ladder. | [Career framework](../playbook/people/career-framework.md) |
| Software Engineering at Google (Titus Winters, Tom Manshreck, Hyrum Wright, 2020) | How practices such as code review, testing and large-scale changes hold up as code lives for years and teams grow. | [Code review](../playbook/delivery/code-review.md) |
| Working Effectively with Legacy Code (Michael Feathers, 2004) | Techniques for getting untested code under test safely so it can be changed. | [Legacy modernisation](../playbook/architecture/legacy-modernisation.md) |
| The Mythical Man-Month (Fred Brooks, 1975) | Why adding people to a late software project makes it later, and why conceptual integrity matters. Still the clearest case against planning by headcount. | [Planning and forecasting](../playbook/ways-of-working/planning-and-forecasting.md) |

## Architects

| Book | Why it matters | Playbook page |
|---|---|---|
| Fundamentals of Software Architecture (Mark Richards, Neal Ford, 2020) | Architecture characteristics, the main architecture styles and their trade-offs, and the soft skills of the role. | [Architecture practice](../playbook/architecture/architecture-practice.md) |
| Building Evolutionary Architectures (Neal Ford, Rebecca Parsons, Patrick Kua, 2017) | Fitness functions: automated checks that keep an architecture true as it changes. | [Architecture toolkit](architecture-toolkit.md) |
| Designing Data-Intensive Applications (Martin Kleppmann, 2017) | Replication, partitioning, transactions and consistency explained so you can reason about any data system you choose. | [Scaling](../playbook/architecture/scaling.md) |
| Domain-Driven Design (Eric Evans, 2003) | A shared language with the business and bounded contexts as the way to divide large systems. Underpins many service and team boundaries. | [Team topology](../playbook/operating-model/team-topology.md) |
| Monolith to Microservices (Sam Newman, 2019) | Patterns for splitting a system step by step, including when not to split it at all. | [Legacy modernisation](../playbook/architecture/legacy-modernisation.md) |

## Strategists and planners

| Book | Why it matters | Playbook page |
|---|---|---|
| Good Strategy Bad Strategy (Richard Rumelt, 2011) | A strategy is a diagnosis, a guiding policy and coherent actions. Everything else is goals or slogans. | [Technical strategy](../playbook/strategy/technical-strategy.md) |
| Team Topologies (Matthew Skelton, Manuel Pais, 2019) | Four team types and three interaction modes, designed around cognitive load and the flow of change. | [Team topology](../playbook/operating-model/team-topology.md) |
| The Goal (Eliyahu Goldratt, 1984) | A novel that teaches the theory of constraints: improving anything except the bottleneck does not raise throughput. | [Portfolio and capacity](../playbook/strategy/portfolio-and-capacity.md) |
| Thinking in Systems (Donella Meadows, 2008) | Stocks, flows and feedback loops, and why well-meant changes to a system often backfire. | [Root cause analysis](../playbook/reliability/root-cause-analysis.md) |
| Thinking, Fast and Slow (Daniel Kahneman, 2011) | The biases that distort estimates and decisions, including anchoring and the planning fallacy. | [Decision making](decision-making.md) |
| Shape Up (Ryan Singer, 2019) | Fixed time and variable scope: shape work before committing a team to it, and set an appetite instead of an estimate. | [Agile and Scrum](../playbook/ways-of-working/agile-and-scrum.md) |

## Reliability and delivery

| Book | Why it matters | Playbook page |
|---|---|---|
| Site Reliability Engineering (Betsy Beyer, Chris Jones, Jennifer Petoff, Niall Richard Murphy, eds., 2016) | Service level objectives, error budgets, toil and blameless postmortems, as practised at scale. Free to read online. | [Service levels](../playbook/reliability/service-levels.md) |
| Continuous Delivery (Jez Humble, David Farley, 2010) | The deployment pipeline: every change built, tested and made releasable automatically. | [Continuous integration](../playbook/delivery/continuous-integration.md) |
| Release It! (Michael Nygard, 2007) | Stability patterns such as timeouts, circuit breakers and bulkheads, and the failure patterns they prevent. | [Production readiness](../playbook/reliability/production-readiness.md) |

## Security

| Book | Why it matters | Playbook page |
|---|---|---|
| Security Engineering (Ross Anderson, 3rd edition, 2020) | How to build systems that stay dependable against malice, error and mischance, including the economics and human factors behind security failures. | [Secure development](../playbook/security/secure-development.md) |

Security practice moves faster than books. The playbook's security pages cite standards and official guidance directly; start with [supply chain](../playbook/security/supply-chain.md) and [vulnerability management](../playbook/security/vulnerability-management.md).

## Common mistakes

| Mistake | Fix |
|---|---|
| Reading a book as doctrine | Take the idea that fits your problem. Leave the rest. |
| Copying the practices of the authors' employers | Start from your own evidence, as the [technical strategy](../playbook/strategy/technical-strategy.md) page says. |
| Reading alone and changing nothing | Run a reading group: one chapter, one hour, one change to try. |
| Reading only in your own role | Leaders read one architecture book; architects read one strategy book. |

## Templates

None for this page. Reading groups can use the [team working agreement](../templates/docs/team-working-agreement.md) to agree a format.

## Sources

The books listed above, in their first editions unless stated.
