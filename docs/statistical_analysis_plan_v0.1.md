# Statistical Analysis Plan v0.1 — Global Team Conflict Lab

## Freeze principle

This plan is frozen before substantive model outputs are inspected.

## Research question

Holding the conflict facts constant, do directness and register alter an AI system's diagnosis of responsibility, escalation, and managerial intervention?

The two deployed systems are analyzed first **within system**. Cross-system comparisons are comparisons of deployed AI systems, not pure comparisons of underlying model weights.

## Experimental unit

The scenario family is the primary experimental unit.

There are 10 families and four conditions per family:

- DC: direct + conversational
- DI: direct + institutional
- MC: mitigated + conversational
- MI: mitigated + institutional

Each condition is repeated three times within each system.

## Primary outcomes

1. `speaker_responsibility`
2. `escalation_need`
3. `managerial_intervention_need`

These are primary because they represent consequential conflict diagnosis and organizational-response judgments.

## Secondary outcomes

- `conflict_severity`
- `speaker_aggression`
- `speaker_cooperativeness`
- `addressee_responsibility`

The categorical `recommended_strategy` outcome is descriptive/exploratory in the pilot.

## Replicate reduction

For each system × family × condition × numeric outcome, compute the mean of the three valid replicates.

- If 3 replicates are valid: use all 3.
- If 2 are valid: use their mean and flag the cell as incomplete.
- If fewer than 2 are valid: treat the cell as missing.
- No score is imputed.

Replicate-level results remain archived and are used in sensitivity analyses.

## Prespecified family-level contrasts

Let DC, DI, MC, MI denote the condition-cell means.

### Directness

`D = ((DC + DI) / 2) - ((MC + MI) / 2)`

### Register

`R = ((DI + MI) / 2) - ((DC + MC) / 2)`

### Directness × register

`I = (DI - DC) - (MI - MC)`

## Primary inference

Within each system and primary outcome, test D, R, and I against zero using a two-sided **exact sign-flip permutation test** over scenario-family contrasts.

With 10 complete families there are `2^10 = 1024` sign assignments.

Report:

- mean family-level contrast;
- median family-level contrast;
- exact p-value;
- 95% bootstrap confidence interval.

Bootstrap:

- 10,000 resamples at the scenario-family level;
- seed `2026092803`.

## Multiplicity

Within each system, adjust the 9 confirmatory tests (3 primary outcomes × 3 contrasts) with Holm's method.

Retain both raw and adjusted p-values.

Post-hoc/simple-effect contrasts are confirmatory only when the corresponding interaction passes the adjusted gate.

## Cross-system comparison

Compute ChatGPT Business minus Gemini API for each family-level D, R, and I contrast.

Analyze these system differences with exact sign-flip tests as **exploratory** evidence of system heterogeneity.

Do not attribute such differences solely to underlying model weights because the access layers differ.

## Secondary outcomes

Use the same family-level effect estimates for secondary outcomes.

Exploratory p-values are adjusted with Benjamini-Hochberg FDR within system.

## Role relation

Upward / peer / downward role-relation analyses are exploratory because only 10 scenario families are available.

Report stratified estimates without confirmatory interaction claims.

## Categorical strategy

For `recommended_strategy`:

- report counts/proportions by condition and system;
- report transitions across matched family conditions;
- treat inferential multinomial modeling as future confirmatory work, not part of this pilot.

## Sensitivity analysis

Fit replicate-level cumulative-link mixed models separately within each system:

`score ~ directness * register + (1 | family_id)`

A combined exploratory model may use:

`score ~ directness * register * system + (1 | family_id)`

Nonconvergence is reported rather than resolved by unplanned specification searching.

## Missing data

Technical failures are missing and never imputed.

If fewer than 2 of 3 replicates remain for a condition cell, that cell is unavailable.

If more than 20% of cells are unavailable for a system, confirmatory inference is suspended for that system.

## Interpretation

An effect indicates that the deployed AI system's conflict diagnosis changes with sociopragmatic form while the frozen conflict facts remain constant.

It does not establish demographic or national-cultural bias.

Status: frozen before substantive data inspection.
