# Pilot Semantic-Invariance Audit v0.1

## Scope

This audit covers the 10 pilot scenario families (`GTCL_001`-`GTCL_010`) and 40 condition messages in Global Team Conflict Lab.

## Manipulation

Each family contains four realizations:

- `DC`: direct + conversational
- `DI`: direct + institutional
- `MC`: mitigated + conversational
- `MI`: mitigated + institutional

The intended manipulation is limited to directness/mitigation and register.

## Invariants reviewed

The manual audit checked that the four realizations within each family preserve:

- underlying conflict event;
- speaker and addressee roles;
- agency and responsibility;
- deadlines and temporal constraints;
- organizational consequences;
- source of disagreement;
- substantive certainty and feasibility claims;
- requested conflict-management action.

## Confound review

The automated heuristic audit returned 0 flagged families. A subsequent manual audit nevertheless identified subtler differences involving agency, certainty, and responsibility in several families. The generator was revised so that mitigation does not weaken the conflict facts and register shifts do not introduce additional authority, sanctions, evidence, urgency, or responsibility differences.

## Final pilot status

- Families: 10
- Condition messages: 40
- JSON-schema validation: 10/10 families pass
- Automated invariance audit: 0 flagged families after revision
- Manual semantic-invariance review: completed before freeze
- Confirmatory model data: none collected at freeze time

Any later stimulus modification requires a new dataset version rather than editing the frozen v0.1 dataset in place.
