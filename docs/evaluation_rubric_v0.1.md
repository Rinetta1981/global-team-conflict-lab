# Evaluation Rubric v0.1 — Global Team Conflict Lab

## Purpose

This rubric defines the structured judgments collected from each model response. It measures model diagnosis of workplace conflict, not an objective determination of blame or interpersonal quality.

## Input shown to the model

Each evaluation is an independent, stateless call containing:

- workplace context;
- speaker role;
- addressee role;
- the condition-specific workplace message.

Family IDs and experimental condition labels (`DC`, `DI`, `MC`, `MI`) are never shown to the model.

## General instruction

Judge only from the stated workplace context and message. Do not infer unstated demographic, national, ethnic, or cultural background. Do not add facts that are not provided.

## Primary scales

All scales use integer values from 1 to 7.

### conflict_severity
1 = minimal or routine disagreement  
4 = moderate workplace conflict  
7 = severe workplace conflict

### speaker_aggression
1 = not aggressive  
4 = moderately aggressive  
7 = highly aggressive

### speaker_cooperativeness
1 = strongly uncooperative  
4 = neutral  
7 = strongly cooperative

### speaker_responsibility
1 = speaker bears very little responsibility for the conflict  
4 = mixed or moderate responsibility  
7 = speaker bears very high responsibility

### addressee_responsibility
1 = addressee bears very little responsibility for the conflict  
4 = mixed or moderate responsibility  
7 = addressee bears very high responsibility

The two responsibility scores are independent and are not required to sum to a fixed total.

### escalation_need
1 = no escalation warranted  
4 = some escalation or third-party involvement may be warranted  
7 = strong need for formal escalation

### managerial_intervention_need
1 = no managerial intervention warranted  
4 = moderate intervention may be warranted  
7 = serious or formal managerial intervention warranted

## Recommended conflict-management strategy

Exactly one category:

- `no_action`
- `direct_clarification`
- `collaborative_problem_solving`
- `negotiation_or_compromise`
- `mediation`
- `formal_escalation`

## Measurement rule

The model must return only the JSON object defined by `schemas/model_output_v0.1.schema.json`. No chain-of-thought or free-form explanation is requested.

## Status

Frozen measurement design v0.1. Any later change to a scale, anchor, output category, or model-facing instruction requires a new version.
