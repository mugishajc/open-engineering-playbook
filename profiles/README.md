# Profiles

A profile tells you which pages of the Open Engineering Playbook to adopt first, at which level, and what to skip for now. Pick one size profile. Then add an overlay if you work for government or under a regulator.

## Pick your profile in under a minute

**Step 1. How many engineers write production code?**

| Engineers | Profile | Default level |
|---|---|---|
| None: a small or medium business that uses software but does not build it | [SME](sme.md) | Foundation, in 8 of 14 areas |
| 1 | [Solo](solo.md) | Foundation |
| 2 to about 20, one team | [Startup](startup.md) | Foundation |
| About 20 to 200, several teams | [Scale-up](scale-up.md) | Standard |
| More than 200, many teams and shared platforms (groups of 1,000 or more also read its large groups section) | [Enterprise](enterprise.md) | Standard |

Between two sizes? Pick the smaller one and go up a level in the areas that hurt.

**Step 2. Does an overlay apply?** Answer each question separately. Both can apply.

| Question | If yes, add |
|---|---|
| Are you a government body, or do you build or run software for one? | [Public sector](public-sector.md) overlay |
| Can a financial, health, telecom or critical infrastructure regulator inspect how you build or run software? | [Regulated](regulated.md) overlay |

An overlay does not replace your size profile. You still follow the size profile's week 1 to year 1 plan, and you add the overlay's rows at each step. Any overlay raises the target to Assured, scoped to the systems the rules cover. With the SME profile, apply only the SME note in each overlay, not the full tables.

## What the levels mean

| Level | In one line | Default for |
|---|---|---|
| Foundation | The minimum that pays for itself at once | SME, Solo, Startup |
| Standard | Shared practice across several teams, measured | Scale-up, Enterprise |
| Assured | Standard plus evidence, separation of duties and audit trails | Any profile with an overlay |

Each profile page has a table with the target level for all 14 practice areas and the signs that one area should go higher early. The SME profile skips six areas that need in-house engineers.

Levels never lower a legal duty. Records of processing, impact assessments, processor contracts, breach registers, transfer mechanisms and reporting deadlines apply from the day the law applies to you, at every level and in every profile. See the [legal floor](../playbook/data/data-security-and-privacy.md#legal-floor-applies-at-every-level).

## How each profile page is laid out

1. Who it is for.
2. Target level by area.
3. Week 1, month 1, quarter 1 and year 1: what to do, the page to read, the template to copy.
4. What to skip at this size, why, and when to come back to it.
5. How to check progress with the assessment.

## Record your profile

The [assessment](../assessment/README.md) reads your profile and overlays from the answers file and sets your targets from them:

```toml
profile = "scale-up"            # sme, solo, startup, scale-up or enterprise
overlays = ["regulated"]        # optional: "public-sector", "regulated"
```

```bash
python3 assessment/assess.py --init --profile scale-up > my-answers.toml
```

With `--profile sme` the assessment asks its own 18 questions and leaves out the areas the SME profile skips.

Then copy the templates the profile names into your repository with `tools/adopt.sh`. It never overwrites a file you already have.
