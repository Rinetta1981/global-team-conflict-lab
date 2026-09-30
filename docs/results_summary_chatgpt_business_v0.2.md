# ChatGPT Business Results Summary v0.2

## Status

This document summarizes the completed **ChatGPT Business / GPT-5.6 Sol (Medium reasoning)** analysis for Global Team Conflict Lab (GTCL). These results are **system-specific**. The planned Gemini replication has not yet been completed and no cross-system claims are made here.

## Research question

Does an AI system interpret workplace conflict differently when the **factual conflict is held constant** but the speaker's message varies in:

- **directness**: direct vs mitigated
- **register**: conversational vs institutional

The four experimental conditions are DC, DI, MC, and MI. Ten conflict scenario families were evaluated, with three replicates per condition, for **120 ChatGPT Business observations**.

## Confirmatory outcomes

Primary outcomes were:

- speaker responsibility
- escalation need
- managerial intervention need

Inference used exact two-sided sign-flip permutation tests over scenario-family contrasts, with Holm correction across the nine preregistered confirmatory tests.

**No primary test survived Holm correction.**

All primary effects were small. For example, the directness contrast was:

- speaker responsibility: +0.067
- escalation need: +0.017
- managerial intervention need: +0.067

None met the confirmatory significance criterion.

## Secondary outcomes

The clearest secondary result was speaker cooperativeness.

| Outcome | Contrast | Mean contrast | BH-FDR p | Result |
|---|---|---:|---:|---|
| Speaker cooperativeness | Directness | -0.817 | .0234 | Survived BH-FDR |
| Conflict severity | Directness | +0.167 | .0938 | Did not survive BH-FDR |
| Speaker aggression | Directness | +0.400 | .0938 | Did not survive BH-FDR |
| Addressee responsibility | Directness | +0.133 | .0938 | Did not survive BH-FDR |

Register and interaction effects did not survive multiplicity correction.

## Categorical conflict-management recommendations

The categorical outcome was **recommended strategy**.

Only two categories were used:

- collaborative problem solving
- direct clarification

The recommendation distribution was almost invariant to directness:

- collaborative problem solving: 29/60 direct vs 28/60 mitigated
- direct clarification: 31/60 direct vs 32/60 mitigated

It was also almost invariant to register:

- conversational: 29/60 collaborative problem solving vs 31/60 direct clarification
- institutional: 28/60 collaborative problem solving vs 32/60 direct clarification

Thus, changes in interpersonal evaluation did **not** meaningfully propagate into the discrete conflict-management recommendation.

## Exploratory role-relation analysis

Role relation was explored descriptively across upward, peer, and downward conflict families.

The negative directness effect on speaker cooperativeness appeared in all three role relations and was descriptively largest in **upward** communication:

- upward: about -0.94
- peer: about -0.79
- downward: about -0.72

Directness also increased perceived aggression more strongly in upward and peer scenarios than in downward scenarios.

Because role relation is not independently crossed within each scenario family and each subgroup contains only 3-4 families, these patterns are exploratory.

## Ordinal-model sensitivity analysis

A cumulative-link mixed model was preregistered as a sensitivity analysis:

`score ~ directness * register + (1 | family_id)`

The clean ordinal model for **speaker cooperativeness** strongly corroborated the negative directness effect.

Clean models for:

- addressee responsibility
- conflict severity
- managerial intervention need
- speaker responsibility

did not show clear directness effects.

Two models were numerically unstable and are not interpreted inferentially:

- escalation need
- speaker aggression

Both produced singular-Hessian / undefined variance-covariance diagnostics.

## Main interpretation

The strongest system-specific pattern is:

> **Directness changes interpersonal evaluation more than downstream conflict-management action.**

Within GPT-5.6 Sol in ChatGPT Business, more direct workplace conflict messages were consistently judged as less cooperative, while the recommended conflict-management strategy remained nearly unchanged.

This supports a distinction between **sociopragmatic sensitivity in person perception** and **relative robustness in action recommendation**.

These results should not be described as national, ethnic, or demographic bias. The stimuli contain no demographic or national identity information.

## Reproducibility

Analysis-ready data:

- `results/analysis_ready/chatgpt_business_v0.2_long.csv`
- `results/analysis_ready/chatgpt_business_v0.2_cell_means.csv`
- `results/analysis_ready/chatgpt_business_v0.2_family_contrasts.csv`

Analysis outputs:

- `results/analysis/chatgpt_business_v0.2_confirmatory.csv`
- `results/analysis/chatgpt_business_v0.2_secondary.csv`
- `results/analysis/chatgpt_business_v0.2_categorical_by_*.csv`
- `results/analysis/chatgpt_business_v0.2_role_relation_exploratory.csv`
- `results/analysis/chatgpt_business_v0.2_ordinal_sensitivity.csv`
- `results/analysis/chatgpt_business_v0.2_ordinal_diagnostics.csv`

Reproducibility scripts are in `scripts/analysis/`.
