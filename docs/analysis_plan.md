# Analysis Plan: Beauty & Wellness Customer Purchase and Retention

## Status and analytical boundary

This is a proposed analysis. There is no customer dataset attached, no
customer-level analysis has been run, and no hypothesis has been tested.
Market context from published sources is not a substitute for company data.
No real customer findings should be claimed until the data are approved,
validated, and analyzed.

## Business problem

Beauty and wellness businesses operate in categories where market growth,
value expectations, channel behavior, and consumer needs are changing.
McKinsey's 2025 and 2026 beauty publications describe continued market growth
alongside changing value perceptions and channel dynamics; its 2025 wellness
research describes demand across multiple dimensions and markets (S1–S3 in
`docs/research_sources.csv`). Those sector observations motivate questions; they
do not establish that any particular business has a retention problem.

## Academic research foundation and transfer limits

The rationale combines beauty-specific consumer research with established
marketing/customer-analytics studies. These sources justify questions and
candidate methods, but none supplies findings for the business proposed here.

- Perret and Schwientek (2025; S4) study customer experience and loyalty for
  augmented-reality- and AI-driven cosmetics using an online survey. Their
  abstract describes links involving experience, satisfaction, purchase
  intention, advocacy, and repurchase intention. This beauty-specific context
  motivates considering customer experience as a construct, but it is a narrow
  beauty-tech setting and reported intentions are not observed repeat
  transactions or proof of causal impact. Full methods and sample characteristics
  should be reviewed before relying on further details.
- Fader, Hardie, and Lee (2005; S5) formalize the relationship between
  recency/frequency/monetary (RFM) purchase histories and customer lifetime
  value, with holdout tests using online music customer data. This supports
  RFM as candidate summaries and holdout validation; it does not establish that
  those model assumptions fit beauty or wellness transactions.
- Fader, Hardie, and Shang (2010; S6) develop a discrete-time
  beta-geometric/beta-Bernoulli model for noncontractual repeat behavior and
  latent dropout, applying it to nonprofit donations. This motivates care in
  distinguishing observed inactivity from confirmed churn. The nonprofit
  context is not beauty retail, and no such model is fitted in this proposal.
- Gupta, Lehmann, and Stuart (2004; S7) frame customer value as expected
  discounted future earnings and illustrate customer valuation using five
  firms. This supports connecting repeat behavior to margin and costs rather
  than treating order count alone as business value. Their quantitative
  estimates are context-specific and are not used as this project's forecast,
  causal effect, or benchmark.

Together, these sources motivate the proposed sequence: industry publications
frame market questions, beauty-specific research informs possible experience
constructs, and marketing-science research informs candidate behavioral
measures and validation. The primary outcomes remain approved customer
transactions; external research is context, not a substitute. Bibliographic
metadata and transfer limitations are logged in `docs/research_sources.csv`.

The proposed business problem is therefore framed as a decision question:
**using consented, appropriately governed transaction and customer data, can
the organization identify actionable patterns associated with repeat
purchasing and design measurable, customer-respectful retention actions?**

## Scope and exclusions

**In scope**

- Transaction-level orders/items, customer key, order dates, net sales,
  discount/refund fields, product category, and channel where available.
- Repeat purchase, customer cohort, category/channel mix, recency/frequency/
  monetary (RFM) summaries, and descriptive segment comparisons.
- Optional, time-aware repeat-purchase or lapse-risk modeling, only if data
  quality, volume, permissions, and observation windows support it.
- Recommendations expressed as testable actions with guardrails and owners.

**Out of scope**

- Claims about actual brand performance, customers, causal drivers, or
  campaign lift before analysis.
- Sensitive health, skin-condition, treatment, or inferred-trait data unless
  specifically approved, necessary, and legally reviewed; such fields are not
  required for the core transaction analysis.
- Personalized health advice, individual-level automated decisions, and
  deployment of a production targeting model.
- Treating correlation, a predictive score, or a market-level survey as proof
  of causal impact.

## Objectives and research questions

1. Synthesize current industry context and peer-reviewed marketing research,
   stating transfer limitations.
2. Define measurable purchase, repeat, customer-experience, and business-value
   outcomes before requesting data.
3. Identify feasible data sources and specify variables, access constraints,
   and quality checks.
4. Formulate testable research questions and hypotheses that remain untested
   until actual analysis.
5. Design reproducible data-quality checks and exploratory analysis with
   appropriate denominators and visualizations.
6. Select suitable statistical methods and conditional segmentation/prediction
   approaches, assumptions, leakage controls, and evaluation criteria.
7. Translate validated evidence into responsible, measurable marketing tests
   with customer and business guardrails.

**Research questions:** the report specifies seven questions, each with
variables, analysis, expected output, and business relevance:

1. Which first-purchase product categories are associated with different
   repeat rates?
2. How is pre-cutoff purchase recency associated with a future purchase?
3. Do purchase frequency and future average order value differ across
   pre-defined, cutoff-safe segments?
4. Are discounts associated with order value or subsequent repeat after
   accounting for observable differences?
5. Where available, are linked customer ratings/satisfaction associated with
   future repeat purchase?
6. Do patterns vary by acquisition channel or customer cohort under comparable
   follow-up?
7. Can transaction patterns support useful segmentation or future repeat/churn
   risk ranking beyond a simple baseline?

The satisfaction and review questions require optional linked/approved data;
transaction data do not measure satisfaction.

## Hypotheses (not tested)

- **H1:** Shorter pre-cutoff recency is associated with a higher subsequent
  repeat probability; H0 is no association. Candidate test: pre-specified
  logistic regression. Assumptions include independent customers, complete
  follow-up, valid dates, adequate sample and no leakage.
- **H2:** Repeat rates differ by first-purchase category; H0 is equal
  proportions. Candidate test: chi-square where independence and expected cell
  counts permit, otherwise a justified exact/Monte Carlo approach. Control
  multiplicity for follow-up comparisons.
- **H3:** Future-window AOV differs among segments defined from prior behavior;
  H0 is equal means. Candidate test: Welch ANOVA or robust/non-parametric
  alternative. Do not define segments using the future outcome.
- **H4:** Discount use/rate is associated with subsequent repeat after
  pre-specified adjustment; H0 is no association. Candidate test: adjusted
  logistic regression. Direction is not assumed; selection and product mix
  confound and adjustment does not establish causality.
- **H5:** A linked pre-outcome satisfaction score is associated with future
  repeat; H0 is no association. Candidate method: Spearman for ordinal
  exploratory analysis or suitable ordinal/logistic regression. Requires a
  validated instrument, temporal linkage, sufficient responses, and
  nonresponse-bias review.

These are directional research prompts, not confirmed results. Tests, windows,
eligible populations, and multiple-comparison handling must be pre-registered
with the project sponsor before inferential claims are made.

## Candidate population and operational definitions

The unit of observation is the customer, anchored to a qualifying first
completed purchase. The eligible population, geography, channels, brands,
date range, exclusions, and order-status rules must be agreed with the data
owner before extraction.

- **Qualifying order:** an order meeting agreed status, refund, and test-order
  rules; define once and use consistently.
- **First purchase:** earliest qualifying order visible in the complete
  observation history. If the history begins after true customer acquisition,
  flag customers as left-censored and do not call their first observed order
  their true first purchase without qualification.
- **Repeat purchase:** at least one later qualifying order after the anchor
  purchase and before the stated horizon.
- **90/180/365-day repeat rate:** eligible anchored customers with a qualifying
  repeat within the horizon divided by anchored customers with the full
  horizon of observable follow-up. Report the denominator and censoring rule.
- **Net sales:** order/item revenue after agreed discounts, cancellations,
  refunds, tax, and shipping treatment. Confirm accounting conventions first.
- **Time to second order:** elapsed days between the first and second
  qualifying order; customers without an observed second order are censored
  at their last valid follow-up date.

The 90-, 180-, and 365-day horizons are proposed reporting cuts, not known
business norms. Select horizons that fit the category's replenishment cycle
and the length and completeness of available history.

## Candidate variables

See `docs/variable_dictionary.csv` for the full proposed dictionary. Core
fields include pseudonymous customer ID, order ID, order date, order status,
net sales, discount, refund, category, channel, and geography at an approved
level. Derived fields include first-order date, cohort, order count,
recency, frequency, monetary value, time to second order, and horizon-based
repeat flags.

Avoid direct identifiers in the analysis layer. Do not ingest free text or
sensitive inferred traits by default. Use a stable pseudonymous key only if
linkage is approved and necessary.

## Potential data sources and readiness checks

1. **Commerce/POS order and item-line exports:** source of transaction dates,
   status, prices, units, discounts, returns, product and channel.
2. **Customer/CRM table:** pseudonymous customer key, account creation, and
   only approved coarse attributes.
3. **Campaign/contact log:** send/eligibility/treatment timestamps, consent,
   and campaign assignment only for a separate, properly designed campaign
   evaluation.
4. **Product master and channel mapping:** consistent category, SKU, and
   channel definitions over time.
5. **Data governance metadata:** provenance, event definitions, retention,
   permission, timezone, and refresh cadence.
6. **Optional customer-experience survey or digital experience logs:** only
   when an approved question requires the construct and the business has a
   suitable instrument or recorded experience event. Survey scores need
   instrument, timing, response-rate, and nonresponse-bias review; transaction
   records do not measure satisfaction.

Check row grain, key uniqueness, duplicate orders, timestamp timezone,
history start, missing customer keys, refund/cancellation handling, currency,
category/channel drift, and sample coverage. Reconcile aggregate order counts
and sales to a trusted operational source before modeling.

## EDA and analysis sequence

1. **Governance gate:** confirm purpose, lawful basis/permission, minimum
   fields, access controls, retention, geography, and suppression rules.
2. **Profiling:** load with pandas; validate schema, data types, row grain,
   uniqueness, dates, currencies, missingness, invalid values, and key joins.
3. **Reconciliation:** quantify exclusions and tie core totals back to approved
   source-system aggregates; log discrepancies rather than silently repairing.
4. **Descriptive EDA:** use pandas and NumPy for summaries; Matplotlib and
   Seaborn for distributions, time trends, cohort curves, and category/channel
   comparisons. Show denominators, follow-up completeness, and uncertainty.
5. **Cohort analysis:** anchor cohorts to first qualifying order; use
   comparable follow-up windows; flag immature cohorts and left truncation.
6. **Segment comparisons:** report effect sizes and confidence intervals where
   assumptions support them; control false discovery or keep comparisons
   explicitly exploratory.
7. **Optional model:** define a prediction date and future outcome window;
   build only with features available at prediction time. Compare logistic
   regression to a prevalence-only baseline; use a time-based split, not a
   random row split. Consider a tree model only if it adds justified value.
8. **Decision synthesis:** map sufficiently supported patterns to test
   hypotheses, owners, cost, customer benefit, and guardrail metrics.

## Analytical methods and evaluation

**Descriptive first.** Cohort repeat-rate tables and time-to-event curves
(Kaplan–Meier where suitable) can describe repeat timing while accounting for
right-censoring. For group contrasts, select a test compatible with outcome
type, sample size, and independence assumptions; publish denominators and
uncertainty. Regression may adjust for pre-specified covariates but does not
by itself establish causality.

**Optional supervised prediction.** Define a prediction unit, cutoff date,
positive class (repeat within a future horizon, or lapse under a business
definition), and eligible denominator before modeling. Use chronological
train/validation/test periods, customer-level separation, and preprocessing
fitted only within training folds. Prevent target leakage by excluding
post-cutoff fields. Use scikit-learn pipelines and retain a simple,
interpretable baseline.

**Metrics**

- Descriptive: repeat rate with denominator, cohort size, median time to
  second purchase, follow-up coverage, and interval estimates.
- Class imbalance: precision-recall AUC as a ranking summary; ROC AUC as a
  secondary ranking metric; precision, recall, and lift at the actual
  contactable/action capacity.
- Probability quality: log loss and calibration plot/Brier score where
  probability estimates will inform decisions.
- Operational: incremental contribution margin, contact cost, opt-out/
  complaint rate, and holdout-measured incremental outcomes for campaigns.

No universal success threshold is assumed. The sponsor must set decision
thresholds, minimum sample sizes, economic constraints, and guardrails before
examining test results. For impact claims, use randomized holdouts when
feasible; otherwise describe the design limitations and avoid causal wording.
The RFM/customer-value and noncontractual repeat-purchase literature (S5–S7)
motivates these candidate methods; external model results must not be assumed
to transfer to this business.

## Privacy, fairness, and responsible use

Apply purpose limitation, data minimization, least-privilege access, approved
retention/deletion, secure transfer/storage, and audit logging. Confirm consent
and channel permissions for any outreach; do not equate purchase history with
permission to market. Remove direct identifiers from analytical working
files, document re-identification risk, and suppress small cells. Treat
precise location and sensitive health, skin, or treatment information as
out of scope unless separately approved and demonstrably necessary. Review
applicable privacy, consumer-protection, and marketing rules with qualified
stakeholders. Check group-level model errors and avoid sensitive-attribute
proxies or exclusionary targeting. These safeguards are planning controls,
not a claim of legal compliance.

## Recommendation framework

Only after validation, score candidate actions on: (1) strength and
consistency of evidence, (2) customer value and relevance, (3) measurable
incremental margin or service outcome, (4) operational feasibility, (5)
privacy/fairness risk, and (6) testability. Translate each candidate into an
experiment card: target population and exclusions, treatment, randomization
unit, holdout, primary metric, guardrails, duration/sample-size method,
analysis rule, owner, and stop conditions. Prefer useful service, replenishment
reminders, onboarding, or relevant product education over indiscriminate
discounting; these are candidate interventions, not recommendations based on
observed results.

## Expanded objectives and question-to-analysis specification

The report provides seven specific objectives and a seven-question analysis
matrix. The matrix pairs each question with variables, method, expected output,
and decision relevance. The customer-experience question is conditional on
linked, approved survey data; transaction data do not measure satisfaction.
Every question remains unanswered until suitable data are available.

## Hypothesis specification

The report specifies five hypotheses, each with H0/Ha, predictor and outcome,
expected direction where defensible, a candidate test, assumptions, and
limitations: (1) prior recency and future repeat; (2) first-purchase category
and repeat-rate differences; (3) prior-behavior segment and later AOV;
(4) discount association with later repeat; and (5) linked satisfaction and
later repeat. These hypotheses are not tested. Choose tests only after
confirming unit of analysis, data type, independence, expected counts,
follow-up, sample size, distribution, and pre-specified comparison rules.
For H3, define segments only from pre-window data so future AOV does not leak
into or define its own comparison.

## Public and internal data acquisition options

- **UCI Online Retail II (S11):** official page documents transaction-like
  invoice/item/date/quantity/unit-price/customer/country fields. It may support
  a methods demonstration, but it is not identified as beauty/wellness-specific.
  Verify dataset license, attribution, access terms, cancellation behavior,
  missing IDs, and suitability before download or use.
- **Amazon Reviews'23 (S12):** candidate for review/rating/product metadata
  analysis only after confirming category, schema, access and reuse conditions.
  Reviews are not linked order histories and cannot provide repeat-purchase
  labels. Do not link reviewer identities or scrape restricted data without
  specific approval.
- **Company commerce, POS, CRM, product, campaign and consent sources:** best
  fit for business-specific analysis, contingent on data owner approval,
  permitted purpose, least-privilege handling, and a documented retention plan.
- **Surveys/reviews/social signals:** include only where collection and reuse
  are permitted and an explicit research question needs them; document
  instrument/selection bias and do not treat ratings as transactions.

No public data were downloaded for this proposal. Dataset-specific licensing,
terms, exact fields, and category coverage must be manually checked at
acquisition time; entries S11–S12 in the source log state the verification
boundary.

## Ten-phase implementation roadmap

1. Business understanding and literature review.
2. Data source identification and authorized acquisition.
3. Data dictionary, qualifying transaction, outcome, cutoff, and target definition.
4. Data quality assessment and source reconciliation.
5. Documented cleaning and preprocessing.
6. Exploratory data analysis: dimensions/types, missingness, duplicate
   transactions, invalid dates/prices/quantities/discounts, purchase-frequency
   and order-value distributions, category sales/repeat rates, RFM, cohort
   maturity, approved segment comparisons, and suitable numeric correlations.
7. Hypothesis testing where assumptions and power support it.
8. RFM or optional clustering-based segmentation, with stability and usefulness
   checks.
9. Optional baseline repeat/churn prediction with time-based evaluation,
   customer separation, and leakage prevention.
10. Evaluation, interpretation, economics, guardrails, recommendations, and
    limitations.

For each EDA output, document the question, fields, method, visualization,
denominator/follow-up, and potential business use. Use a cohort matrix only for
mature follow-up; show distributions and exclusion counts; use a correlation
heatmap only as exploratory context, not causal evidence.

## Modeling and KPI selection notes

For a later supervised model, split by time and keep customers from leaking
between evaluation partitions; fit transformations on training data only.
Report class prevalence and a majority/prevalence baseline. Accuracy alone
can be misleading under class imbalance; select precision, recall, F1,
ROC-AUC, PR-AUC, lift at action capacity, calibration/log loss, and economic
metrics according to the decision. Set thresholds using contact capacity,
false-positive/false-negative costs, and customer guardrails before launch.
Measure business impact with randomized holdout where feasible, using
incremental contribution margin, qualifying repeat rate, opt-out/complaint
rates, and customer experience as appropriate. These are proposed KPIs, not
results or targets.

## Tools, roles, and 30–35-hour schedule

| Workstream | Hours | Planned output |
|---|---:|---|
| Business framing and source review | 4 | Sponsor questions, source log, scope |
| Governance and data inventory | 4 | Approved field list, access/readiness checklist |
| Data extraction and quality checks | 6 | Reconciled, documented analytical table |
| EDA and cohort definitions | 7 | Summary tables, charts, cohort measures |
| Optional exploratory modeling | 5 | Baseline, time split, metrics if gate passed |
| Interpretation and test design | 4 | Evidence-to-action experiment cards |
| Report, QA, and presentation | 4 | Reviewed report and handoff |
| **Total** | **34** | **Within the 30–35-hour target** |

The modeling block is conditional. If data permissions, sample size, or
follow-up are inadequate, reallocate those five hours to data-quality
resolution, uncertainty analysis, or stakeholder validation. Tools: Python,
pandas, NumPy, Matplotlib, Seaborn, scikit-learn (future optional modeling),
Jupyter/VS Code, and python-docx for this report.

## Deliverables and exit criteria

- This proposal/report and source log.
- Approved data specification and completed variable dictionary.
- Reproducible, documented cleaning and analysis notebook or scripts.
- Quality-checked EDA and cohort outputs with denominators and caveats.
- Optional validated model card, only if the modeling gate passes.
- Prioritized, experiment-ready recommendations and stakeholder presentation.

Exit the Week 1 planning phase when the sponsor approves the decision question,
population, retention definitions, data access/privacy gate, and next-step
owner. Do not publish business findings until analysis and review are complete.
