# Cross-model Results — GTCL (ChatGPT vs Gemini)

This is a descriptive post-hoc comparison of the prespecified project-level analyses. It does not alter the confirmatory or secondary inferential gates.

## Direction classification

Direction is classified with a tolerance of 1e-12: same non-zero direction, both zero, zero-boundary (one estimate is zero), or reversal (opposite non-zero signs). This avoids treating zero-versus-small-nonzero contrasts as substantive sign reversals.

## Confirmatory

Direction classes: {'zero_boundary': 7, 'both_zero': 1, 'same_nonzero_direction': 1}

| Outcome | Contrast | ChatGPT | Gemini | Direction | Significance (C/G) |
|---|---|---:|---:|---|---|
| escalation_need | directness | +0.017 | +0.000 | zero_boundary | False / False |
| escalation_need | interaction | +0.033 | +0.000 | zero_boundary | False / False |
| escalation_need | register | +0.017 | +0.000 | zero_boundary | False / False |
| managerial_intervention_need | directness | +0.067 | +0.000 | zero_boundary | False / False |
| managerial_intervention_need | interaction | +0.000 | +0.000 | both_zero | False / False |
| managerial_intervention_need | register | +0.033 | +0.000 | zero_boundary | False / False |
| speaker_responsibility | directness | +0.067 | +0.017 | same_nonzero_direction | False / False |
| speaker_responsibility | interaction | +0.000 | +0.100 | zero_boundary | False / False |
| speaker_responsibility | register | +0.000 | -0.083 | zero_boundary | False / False |

## Secondary

Direction classes: {'reversal': 3, 'zero_boundary': 2, 'same_nonzero_direction': 7}

| Outcome | Contrast | ChatGPT | Gemini | Direction | Significance (C/G) |
|---|---|---:|---:|---|---|
| addressee_responsibility | directness | +0.133 | -0.033 | reversal | False / False |
| addressee_responsibility | interaction | -0.000 | +0.133 | zero_boundary | False / False |
| addressee_responsibility | register | -0.033 | -0.067 | same_nonzero_direction | False / False |
| conflict_severity | directness | +0.167 | +0.100 | same_nonzero_direction | False / False |
| conflict_severity | interaction | +0.133 | -0.067 | reversal | False / False |
| conflict_severity | register | -0.067 | -0.000 | zero_boundary | False / False |
| speaker_aggression | directness | +0.400 | +0.083 | same_nonzero_direction | False / False |
| speaker_aggression | interaction | -0.267 | -0.167 | same_nonzero_direction | False / False |
| speaker_aggression | register | -0.133 | -0.083 | same_nonzero_direction | False / False |
| speaker_cooperativeness | directness | -0.817 | -0.750 | same_nonzero_direction | True / True |
| speaker_cooperativeness | interaction | -0.100 | -0.233 | same_nonzero_direction | False / False |
| speaker_cooperativeness | register | +0.017 | -0.017 | reversal | False / False |

## Categorical recommendation distributions

| Dimension | Level | Category | ChatGPT | Gemini | Gemini − ChatGPT |
|---|---|---|---:|---:|---:|
| directness | direct | collaborative_problem_solving | 0.483 | 0.350 | -0.133 |
| directness | direct | direct_clarification | 0.517 | 0.650 | +0.133 |
| directness | mitigated | collaborative_problem_solving | 0.467 | 0.367 | -0.100 |
| directness | mitigated | direct_clarification | 0.533 | 0.633 | +0.100 |
| register | conversational | collaborative_problem_solving | 0.483 | 0.317 | -0.167 |
| register | conversational | direct_clarification | 0.517 | 0.683 | +0.167 |
| register | institutional | collaborative_problem_solving | 0.467 | 0.400 | -0.067 |
| register | institutional | direct_clarification | 0.533 | 0.600 | +0.067 |

## Ordinal sensitivity

| Outcome | ChatGPT | Gemini |
|---|---|---|
| addressee_responsibility | fit_ok (4 levels) | fit_ok (4 levels) |
| conflict_severity | fit_ok (3 levels) | fit_ok (2 levels) |
| escalation_need | fit_ok (2 levels); numerical warning | fit_error (1 levels); not estimable |
| managerial_intervention_need | fit_ok (4 levels) | fit_error (1 levels); not estimable |
| speaker_aggression | fit_ok (2 levels); numerical warning | fit_ok (2 levels); numerical warning |
| speaker_cooperativeness | fit_ok (2 levels) | fit_ok (2 levels) |
| speaker_responsibility | fit_ok (3 levels) | fit_ok (3 levels) |

Numerical warnings on otherwise fitted ordinal models indicate identifiability/convergence concerns; those fits are not treated as clean inferential sensitivity confirmations. Models marked fit_error are not estimable and are not interpreted.

## Family-level cross-model correlations

These are descriptive Pearson correlations across the 10 scenario families and are not additional inferential tests.

| Outcome | Contrast | Pearson r |
|---|---|---:|
| addressee_responsibility | directness | 0.563 |
| addressee_responsibility | register | -0.644 |
| addressee_responsibility | interaction | -0.225 |
| conflict_severity | directness | 0.156 |
| conflict_severity | register | -0.373 |
| conflict_severity | interaction | -0.523 |
| escalation_need | directness | NA (constant vector) |
| escalation_need | register | NA (constant vector) |
| escalation_need | interaction | NA (constant vector) |
| managerial_intervention_need | directness | NA (constant vector) |
| managerial_intervention_need | register | NA (constant vector) |
| managerial_intervention_need | interaction | NA (constant vector) |
| speaker_aggression | directness | 0.369 |
| speaker_aggression | register | 0.554 |
| speaker_aggression | interaction | 0.554 |
| speaker_cooperativeness | directness | -0.040 |
| speaker_cooperativeness | register | -0.498 |
| speaker_cooperativeness | interaction | 0.270 |
| speaker_responsibility | directness | -0.229 |
| speaker_responsibility | register | 0.555 |
| speaker_responsibility | interaction | -0.497 |

## Manuscript-level synthesis

The secondary effect(s) significant under BH-FDR in both systems were: speaker_cooperativeness × directness (ChatGPT -0.817; Gemini -0.750).
ChatGPT-only BH-FDR-significant secondary effects: 0; Gemini-only: 0.
The cross-model comparison is descriptive and should be interpreted as convergence/divergence of effect estimates and significance status, not as a ranking of models.

Family-level correlations are descriptive summaries across 10 scenario families and should not be treated as new inferential tests.
