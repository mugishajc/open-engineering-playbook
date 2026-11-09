# Kata: error budget math

Work through ten short calculations on one service's SLO: how big the error budget is, how much an incident spent, how fast it was burning, when the burn-rate alerts fire and stop, and whether the service can meet its target at all given its dependencies. You need a calculator and the formulas below. Each answer is hidden; try first.

| | |
|---|---|
| Who | One person or a pair. Useful before joining an on-call rotation or writing an error budget policy. |
| Time | 30 to 40 minutes |
| Practice it teaches | [Service levels](../../playbook/reliability/service-levels.md), [incident management](../../playbook/reliability/incident-management.md), [postmortems](../../playbook/reliability/postmortems.md) |

## The service

The checkout API of an online shop. All numbers are fictional and simplified: traffic is a steady 1,000 requests per minute, day and night.

| Item | Value |
|---|---|
| Availability SLI | Share of requests that return a non-5xx response |
| Availability SLO | 99.9% over a rolling 28-day window |
| Latency SLO | 99% of requests complete in under 800 ms, same window |
| Error budget policy | From [service levels](../../playbook/reliability/service-levels.md#standard): any single incident that spends more than 20% of the budget gets a postmortem; an exhausted budget pauses feature releases |

## Formulas

```text
minutes in window       = days x 24 x 60
requests in window      = minutes in window x requests per minute
error budget (requests) = requests in window x (1 - SLO)
budget spent (%)        = failed requests / error budget x 100
burn rate               = observed error rate / (1 - SLO)
time to exhaust budget  = window length / burn rate
```

## Questions

**1. Size of the budget.** How many requests does the checkout API receive in the 28-day window? How many may fail? What is that as minutes of full outage?

<details>
<summary>Answer 1</summary>

- Minutes in window: 28 x 24 x 60 = 40,320.
- Requests: 40,320 x 1,000 = 40,320,000.
- Error budget: 40,320,000 x 0.001 = **40,320 failed requests**.
- Full outage equivalent: 40,320 x 0.001 = 40.32 minutes, about **40 minutes 19 seconds**. This matches the "about 40 min" row in the [service levels](../../playbook/reliability/service-levels.md#terms) table.

</details>

**2. One incident.** A bad deployment makes 30% of checkout requests fail for 30 minutes. How many requests failed? What share of the budget is that? Does the policy require a postmortem?

<details>
<summary>Answer 2</summary>

- Failed requests: 30 x 1,000 x 0.30 = **9,000**.
- Share of budget: 9,000 / 40,320 = 0.2232, about **22.3%**.
- 22.3% is more than 20%, so **yes**, the policy requires a postmortem with at least one action item at the same priority as top feature work.

</details>

**3. Burn rate.** What was the burn rate during that incident? Had it continued, how long until the whole 28-day budget was gone?

<details>
<summary>Answer 3</summary>

- Burn rate: 0.30 / 0.001 = **300**.
- Time to exhaust: 40,320 minutes / 300 = 134.4 minutes, about **2 hours 14 minutes**.
- Check: 134.4 x 1,000 x 0.30 = 40,320 failed requests. Correct.

</details>

**4. The fast-burn page.** The fast-burn alert pages when the burn rate exceeds 14.4 over both the last 1 hour and the last 5 minutes. What error rate is that? The playbook says burn rate 14.4 for 1 hour spends 2% of the budget. Is that exactly true for this 28-day window?

<details>
<summary>Answer 4</summary>

- Error rate threshold: 14.4 x 0.001 = **1.44%** of requests.
- Budget spent in 1 hour at burn rate 14.4: 14.4 x 60 / 40,320 = 0.0214, about **2.14%**.
- Not exactly. The 14.4 figure comes from the SRE Workbook, which uses a 30-day window: 14.4 x 1 hour / 720 hours = 2.0%. With a 28-day window, the same burn rate spends slightly more. The difference is too small to matter for paging; keep the standard thresholds and know where they come from.

</details>

**5. A slow leak.** At 09:00 a bug starts failing 1% of requests. Ignore the small background error rate before 09:00. Does the fast-burn alert fire? The second alert pages when the burn rate exceeds 6 over both the last 6 hours and the last 30 minutes. When does it fire, and how much budget has been spent by then?

<details>
<summary>Answer 5</summary>

- Burn rate: 0.01 / 0.001 = 10. That is below 14.4, so **the fast-burn alert never fires**, however long the leak lasts.
- Threshold for the second alert: 6 x 0.001 = 0.6%.
- Short window (30 minutes): the average passes 0.6% once 1% x t / 30 > 0.6%, so after t = 18 minutes.
- Long window (6 hours = 360 minutes): the average passes 0.6% once 1% x t / 360 > 0.6%, so after t = 216 minutes.
- Both must be true, so the page fires at 09:00 + 216 minutes = **12:36**.
- Budget spent by then: 216 x 1,000 x 0.01 = 2,160 failed requests; 2,160 / 40,320 = **about 5.4%**. This is what the alert is designed for: it pages at about 5% of budget spent.

</details>

**6. The rest of the window.** The slow leak is fixed at 13:00. Over the whole 28-day window there were also 6,000 scattered failures from normal background errors. Add the incident from question 2. How much budget is spent and how much is left? What does the policy say?

<details>
<summary>Answer 6</summary>

- Slow leak: 09:00 to 13:00 is 240 minutes; 240 x 1,000 x 0.01 = 2,400 failed requests.
- Total failed: 9,000 + 2,400 + 6,000 = **17,400**.
- Spent: 17,400 / 40,320 = **about 43.2%**.
- Left: 40,320 - 17,400 = **22,920 requests, about 56.8%**, or about 23 minutes of full outage.
- Policy: budget remains, so ship as normal. The 30-minute incident still needs its postmortem from question 2.

</details>

**7. Dependencies.** Checkout calls three services in sequence: payments, inventory and tax. Each has an availability of 99.95%, and so does checkout's own code. Assume failures are independent. What is the best availability checkout can expect? Can it meet its 99.9% SLO?

<details>
<summary>Answer 7</summary>

- Availability: 0.9995 x 0.9995 x 0.9995 x 0.9995 = 0.9995^4 = 0.998001, about **99.80%**.
- Expected failures: about 0.2% of requests, roughly 80 minutes of full outage equivalent in 28 days, against a budget of about 40.
- **No.** As the [service levels](../../playbook/reliability/service-levels.md#standard) page says, a service cannot promise more than its critical dependencies deliver unless it adds redundancy or graceful degradation. Options: cache tax rates so tax is not on the critical path, reserve inventory asynchronously, retry payments with idempotency keys, or ask dependencies for a tighter internal SLO. Lowering checkout's SLO is also a valid answer if users would accept it.

</details>

**8. Latency.** Over the window, 350,000 requests took longer than 800 ms. How much of the latency budget is spent?

<details>
<summary>Answer 8</summary>

- Latency budget: 40,320,000 x (1 - 0.99) = **403,200 slow requests**.
- Spent: 350,000 / 403,200 = **about 86.8%**.
- Left: 53,200 slow requests. Not exhausted, but one bad day could finish it. This is the time to look at the slowest endpoints, before the policy forces a release pause.

</details>

**9. SLA against SLO.** Customer contracts promise 99.5% availability per calendar month, with service credits below that. For a 30-day month, how many minutes of full outage does the SLA allow? Why is the SLO set at 99.9%, not 99.5%?

<details>
<summary>Answer 9</summary>

- 30 x 24 x 60 = 43,200 minutes; 43,200 x 0.005 = **216 minutes, or 3 hours 36 minutes**.
- The SLO is tighter so that the team acts (pauses features, fixes reliability) long before a contract is breached. The 99.9% SLO allows about 40 minutes in 28 days; the gap to 216 minutes is the safety margin.

</details>

**10. When the page fires and stops.** Go back to the question 2 incident: 30% of requests fail for 30 minutes, starting from no errors. When does the fast-burn alert (burn rate 14.4 over both 1 hour and 5 minutes) fire? After the fix, when does it stop?

<details>
<summary>Answer 10</summary>

- Threshold: 1.44% (question 4).
- Long window: the 1-hour average passes 1.44% once 30% x t / 60 > 1.44%, so after t = 2.88 minutes.
- Short window: the 5-minute average passes 1.44% once 30% x t / 5 > 1.44%, so after about 15 seconds.
- Both must be true, so the page fires about **3 minutes** after the errors start.
- After the fix, the 1-hour average stays above 1.44% for almost another hour. The 5-minute average drops below 1.44% once less than 0.24 minutes of the bad period is left in it, about **4 minutes 46 seconds** after the fix. The alert needs both windows, so it stops then. That is why the short window exists: without it, the alert would keep firing for about an hour after the fix.

</details>

## Check yourself

Ten correct: you are ready to write an error budget policy. Seven to nine: re-read the burn-rate table in [service levels](../../playbook/reliability/service-levels.md#standard). Fewer: work through the SRE Workbook chapter "Alerting on SLOs" (https://sre.google/workbook/alerting-on-slos/) and try again.

Then do it for real: take one of your own services, pull its last 28 days of request counts, and repeat questions 1, 2 and 6 with your numbers.
