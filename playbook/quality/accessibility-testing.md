# Accessibility testing

The problem: "The automated checker shows zero errors, and a blind user still cannot finish the application form." Automated tools check only part of the Web Content Accessibility Guidelines (WCAG); most success criteria need a person to judge them. Test against WCAG 2.2 level AA in three layers. First, automated checks in CI on every change. Second, manual checks with keyboard, zoom and screen readers on every new or changed journey. Third, an expert audit and testing with disabled people before major releases, and at least yearly for public services. Accessibility is a legal duty for many services, and a defect that stops someone completing a task is a severity 1 defect.

## Outcomes

Starting points. Tune them to your users and legal duties.

| Signal | Starting target |
|---|---|
| Serious or critical automated violations (axe-core impact levels) on pages and states covered by CI | Zero at merge |
| New or changed user journeys that pass the manual keyboard, zoom and screen reader checks before release | 100% |
| Public services with a manual audit against WCAG 2.2 AA and a dated accessibility statement | At least yearly, as in [public sector](../compliance/public-sector.md) |
| Usability sessions with disabled people | Before each major release, and at least twice a year for public services |
| Design system components with documented keyboard behaviour and automated accessibility tests | 100% |
| Accessibility defects that block a task, open at release | Zero, unless the service owner accepted the risk in writing with a workaround published |

## What automation can and cannot check

| Automated tools find | People must judge |
|---|---|
| Images with no text alternative | Whether the text alternative says what the image means |
| Form fields with no label | Whether labels, hints and error messages make sense |
| Text contrast below the ratio, for most static text | Contrast over images, gradients and in every state |
| Missing page language, invalid ARIA, empty buttons and links | Whether the focus order and reading order are logical |
| Some target size problems | Whether the page still works at 400% zoom and reflows at 320 CSS pixels wide (WCAG 1.4.10) |
| Some missing headings and landmarks | Whether a screen reader user can complete the task |
| | Whether time limits, motion, captions and audio description work for the people who need them |
| | Whether sign-in avoids a memory or puzzle test without an alternative (WCAG 3.3.8, new in 2.2) |

WCAG 2.2 added four success criteria at level AA: focus not obscured (2.4.11), dragging movements (2.5.7), target size (2.5.8) and accessible authentication (3.3.8). It added two at level A: consistent help (3.2.6) and redundant entry (3.3.7). It also removed 4.1.1 Parsing. Check that your test plan matches; older checklists do not.

## From design to audit

1. **Design.** Check contrast and target sizes in design files. Annotate headings, landmarks, focus order and the accessible name of each control before build.
2. **Components.** Test each design system component with axe-core in its unit or component tests, and test its keyboard behaviour against the patterns in the W3C ARIA Authoring Practices Guide. A defect fixed in a component is fixed everywhere it is used.
3. **Pages and states in CI.** Run axe-core through your end-to-end framework on each key page, including states such as an open dialog, a validation error and an expanded menu. Fail on serious and critical violations. Find elements by role and accessible name, as [test automation](test-automation.md#design-rules-for-test-code) recommends.
4. **Manual checks per story**, 15 to 30 minutes by a trained team member:
   - keyboard only: reach and operate everything, see where focus is, never get trapped;
   - zoom to 200% and 400%, and narrow the window to 320 CSS pixels: nothing lost or overlapping;
   - a screen reader pass on one desktop and one mobile combination: headings, labels, errors and status messages are announced;
   - forced colours or high contrast mode, and reduced motion.
5. **Assistive technology coverage.** Pick combinations from user research and the market you serve. A common starting set: NVDA with Firefox or Chrome on Windows; JAWS with Chrome where your users work in large organisations; VoiceOver with Safari on macOS and iOS; TalkBack with Chrome on Android; voice control; screen magnification. Web analytics cannot detect screen readers, so do not use them to decide this.
6. **Screen reader testing that finds real problems.** A tester who has used a screen reader for an afternoon reports both false passes and false failures. Train the people who do it, and have them:
   - move the way users do: by headings, landmarks, links and form controls, and with Tab, not only by reading from top to bottom;
   - complete the task without looking at the screen for at least part of the session;
   - check that changes on the page are announced: errors after submit, items added, loading finished (WCAG 4.1.3, status messages);
   - repeat a failure on a second screen reader and browser before filing it, to separate a code defect from a screen reader bug;
   - record the screen reader, browser, operating system and their versions in every defect.
7. **Expert audit** against WCAG 2.2 AA using the W3C Website Accessibility Conformance Evaluation Methodology (WCAG-EM): a defined scope, a representative sample of pages, and complete processes tested end to end.
8. **Testing with disabled people.** Recruit people with a range of visual, hearing, motor, cognitive and neurological impairments. Pay them, let them use their own devices and settings, and test real tasks. This finds the problems that conformance testing does not, such as a process that conforms but takes 40 minutes with a screen reader.

## Documents, mobile apps and bought software

- **Documents.** PDF and office documents published to the public are in scope. Prefer HTML. Where PDF is needed, test tagged structure and reading order; ISO 14289 (PDF/UA) sets the requirements.
- **Mobile apps.** Apply WCAG through EN 301 549 and use platform tools: Android Accessibility Scanner and Espresso accessibility checks, and Xcode Accessibility Inspector. Test with TalkBack and VoiceOver on real devices.
- **Bought software.** Ask suppliers for an Accessibility Conformance Report in the ITI VPAT format, then test the main tasks yourself before you sign. A report is a claim, not evidence.

## Legal duties

This is not legal advice. Check the laws for each market you serve.

| Where | Duty |
|---|---|
| EU, public sector | Directive (EU) 2016/2102 on public sector websites and mobile apps: meet the harmonised standard EN 301 549, publish an accessibility statement, provide a feedback route |
| EU, many private-sector products and services | European Accessibility Act, Directive (EU) 2019/882, applies from 28 Jun 2025 to services including e-commerce, consumer banking, e-books, electronic communications and transport ticketing |
| UK, public sector | Public Sector Bodies (Websites and Mobile Applications) (No. 2) Accessibility Regulations 2018, and the Equality Act 2010 |
| US | Section 508 for federal agencies. The Department of Justice's 2024 rule under Title II of the Americans with Disabilities Act (ADA) sets WCAG 2.1 AA for state and local government web content and apps. An interim final rule of 20 April 2026 moved compliance to 26 April 2027 for entities serving 50,000 people or more and 26 April 2028 for smaller ones and special districts; check for later changes |
| Elsewhere | Many countries have disability rights laws or procurement rules that reference WCAG. Check yours with counsel |

EN 301 549 currently references WCAG 2.1 level AA. Targeting WCAG 2.2 AA meets it and covers the newer criteria, as [public sector](../compliance/public-sector.md#accessibility) explains.

## Practice

### Foundation

- axe-core (or an equivalent rule engine) in CI on the main pages, failing on serious and critical violations.
- A keyboard-only and zoom check on every new screen before release.
- Use a design system or component library with documented accessibility, and do not override its focus styles.
- **Solo and Startup:** learn one screen reader on the platform you build for, and use it on your main journey before each release. The basic reading and navigation commands are enough for this check.

### Standard

- All eight steps above, with the manual checks in the definition of done for user-facing stories.
- Accessibility defects triaged with the same severity scale as other defects. A defect that stops a task is severity 1.
- A trained accessibility specialist for every 4 to 6 teams (starting point) who coaches, runs audits and keeps the assistive technology matrix current.
- Usability sessions with disabled people for new services and major redesigns.

### Assured

- A WCAG-EM audit of each public service at least yearly and after major changes, by an auditor independent of the team.
- A published accessibility statement per service, dated, listing known issues and the date by which each will be fixed.
- Accessibility requirements and acceptance tests in every contract for software you buy or have built.
- Evidence kept per release: automated results, manual check records, audit reports.

## Cloud, on-premises and air-gapped

- axe-core and similar rule engines run offline, so they work on self-hosted and air-gapped CI. Mirror them like other test tools.
- Screen readers and other assistive technologies are installed locally. Keep test machines and devices with current versions inside the network.
- Internal systems on closed networks still have users who need assistive technology, and employment law covers them in many countries. Test staff tools as well as public ones.

## Anti-patterns

| Anti-pattern | Fix |
|---|---|
| A clean automated report treated as conformance | Automated checks plus manual testing with assistive technology. |
| An overlay widget bought to "make the site compliant" | Fix the code and the components. Overlays do not repair the underlying markup. |
| One audit before launch, never repeated | Checks in CI, manual checks per story, a yearly audit. |
| Accessibility defects filed as low priority by default | Severity by impact on the task. A blocked task is severity 1. |
| Testing only with a desktop screen reader | Include mobile screen readers, zoom, voice control and keyboard. |
| Disabled users invited only to the final round | Include them from early prototypes. |
| Screen reader checks by someone who learned the tool that day | Train the testers; repeat each failure on a second screen reader before filing it. |

## Templates

- [Test strategy](../../templates/quality/test-strategy.md), accessibility section
- [Exploratory testing charter](../../templates/quality/exploratory-charter.md): use one with an assistive technology as the resource
- [Release checklist](../../templates/docs/release-checklist.md)

## Sources

- W3C, Web Content Accessibility Guidelines (WCAG) 2.2: https://www.w3.org/TR/WCAG22/
- W3C, What's new in WCAG 2.2: https://www.w3.org/WAI/standards-guidelines/wcag/new-in-22/
- W3C, Website Accessibility Conformance Evaluation Methodology (WCAG-EM) 1.0: https://www.w3.org/TR/WCAG-EM/
- W3C, ARIA Authoring Practices Guide: https://www.w3.org/WAI/ARIA/apg/
- axe-core: https://github.com/dequelabs/axe-core
- ETSI EN 301 549, Accessibility requirements for ICT products and services.
- Directive (EU) 2016/2102 (Web Accessibility Directive): https://eur-lex.europa.eu/eli/dir/2016/2102/oj
- Directive (EU) 2019/882 (European Accessibility Act): https://eur-lex.europa.eu/eli/dir/2019/882/oj
- UK, The Public Sector Bodies (Websites and Mobile Applications) (No. 2) Accessibility Regulations 2018: https://www.legislation.gov.uk/uksi/2018/952/contents/made
- US Section 508: https://www.section508.gov
- US Department of Justice, ADA: https://www.ada.gov/
- US Department of Justice, extension of ADA Title II web compliance dates, Federal Register, 20 April 2026: https://www.federalregister.gov/documents/2026/04/20/2026-07663/extension-of-compliance-dates-for-nondiscrimination-on-the-basis-of-disability-accessibility-of-web
- ITI, Voluntary Product Accessibility Template (VPAT): https://www.itic.org/policy/accessibility/vpat
- ISO 14289-1, PDF/UA.
