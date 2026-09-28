import json
from pathlib import Path

OUT_DIR = Path("global-team-conflict-lab/data/raw")

EVALUATION_QUESTION = (
    "Assess conflict severity, aggression, cooperativeness, attribution of responsibility, "
    "appropriate conflict-management strategy, escalation level, and a suitable managerial response."
)

def make_family(fid, domain, relation, speaker, addressee, context, trigger, source, consequence, dc, di, mc, mi):
    return {
        "schema_version": "0.1",
        "project": "global-team-conflict-lab",
        "family_id": fid,
        "domain": domain,
        "role_relation": relation,
        "speaker_role": speaker,
        "addressee_role": addressee,
        "invariant_facts": {
            "context": context,
            "conflict_trigger": trigger,
            "source_of_disagreement": source,
            "organizational_consequence": consequence,
        },
        "evaluation_question": EVALUATION_QUESTION,
        "conditions": {
            "DC": {"directness": "direct", "register": "conversational", "message": dc},
            "DI": {"directness": "direct", "register": "institutional", "message": di},
            "MC": {"directness": "mitigated", "register": "conversational", "message": mc},
            "MI": {"directness": "mitigated", "register": "institutional", "message": mi},
        },
    }

families = [
    make_family(
        "GTCL_002","credit_attribution","peer","researcher","researcher",
        "Two researchers jointly prepared a presentation, and one researcher contributed the analysis used in three slides.",
        "The final presentation credits the other researcher for the presentation but does not mention the speaker's analytical contribution.",
        "The speaker believes their contribution should be acknowledged in the presentation materials.",
        "The omission may affect how contribution to the joint work is recognized.",
        "I contributed the analysis used in three of these slides, but my contribution is not credited. Please add my contribution to the presentation materials.",
        "I contributed the analysis used in three of these slides, but that contribution is not acknowledged in the presentation materials. Please add the appropriate attribution.",
        "I noticed that the analysis I contributed to three of these slides is not credited. Could you please add my contribution to the presentation materials?",
        "I noticed that the analysis I contributed to three of these slides is not acknowledged in the presentation materials. Could you please add the appropriate attribution?",
    ),
    make_family(
        "GTCL_003","task_ownership","peer","project_specialist","project_specialist",
        "Two project specialists are working on a shared implementation plan, and the testing checklist remains unfinished.",
        "Each specialist understood that the other person was responsible for completing the testing checklist.",
        "The disagreement concerns who was expected to own the unfinished testing task.",
        "The checklist must be completed before implementation can proceed.",
        "The testing checklist is still unfinished. I understood that you were responsible for it, and you understood that I was. We need to agree who will complete it.",
        "The testing checklist remains incomplete. I understood that responsibility for it sat with you, while you understood that it sat with me. We need to establish ownership for completion.",
        "It looks like we had different understandings about the testing checklist. I thought you were responsible for it, and you thought I was. Could we agree who will complete it?",
        "It appears that we had different understandings regarding responsibility for the testing checklist. I understood that it sat with you, while you understood that it sat with me. Could we establish ownership for completion?",
    ),
    make_family(
        "GTCL_004","meeting_participation","peer","team_member","team_member",
        "Two team members are discussing a project issue in a meeting, and one person has repeatedly begun speaking before the other has finished making a point.",
        "The speaker raises the repeated interruptions with the colleague during the meeting.",
        "The disagreement concerns turn-taking and the speaker's ability to complete their contributions.",
        "Continued interruptions may reduce effective participation in the discussion.",
        "You have interrupted me several times before I finished my point. Please let me finish before you respond.",
        "You have spoken over me several times before I completed my point. Please allow me to complete my contribution before responding.",
        "I wanted to mention that you have interrupted me several times before I finished my point. Could you please let me finish before you respond?",
        "I wanted to raise that you have spoken over me several times before I completed my point. Could you please allow me to complete my contribution before responding?",
    ),
    make_family(
        "GTCL_005","workload_allocation","upward","analyst","manager",
        "An analyst has already told the manager that their current assignments fill their available capacity for the week.",
        "The manager assigns an additional task due within the same week.",
        "The analyst disputes the additional allocation because the previously reported capacity constraint remains unchanged.",
        "The analyst must either reprioritize existing work or accept a workload beyond the stated capacity.",
        "I already told you that my current assignments fill my capacity this week. This additional task does not fit without changing priorities. We need to decide what should move.",
        "I previously reported that my current assignments use my available capacity for this week. This additional assignment cannot be accommodated without reprioritization. We need to determine which existing priority should change.",
        "I wanted to flag that I had already said my current assignments fill my capacity this week. This additional task does not fit unless we change priorities. Could we decide what should move?",
        "I wanted to raise that I previously reported my current assignments use my available capacity for this week. This additional assignment cannot be accommodated without reprioritization. Could we determine which existing priority should change?",
    ),
    make_family(
        "GTCL_006","decision_transparency","upward","project_specialist","manager",
        "A project specialist and manager had agreed to use one implementation approach in a planning meeting.",
        "The manager later changes the implementation approach without explaining the reason for the change.",
        "The specialist wants an explanation for why the previously agreed approach was replaced.",
        "The unexplained change affects how the specialist prepares the next stage of work.",
        "We agreed on the original implementation approach, and it has now been changed without an explanation. Please explain why the approach changed.",
        "We previously agreed on the original implementation approach, which has now been replaced without an explanation. Please provide the rationale for the change.",
        "I wanted to ask about the implementation approach we agreed on, which has now been changed without an explanation. Could you please explain why it changed?",
        "I wanted to ask about the implementation approach we previously agreed on, which has now been replaced without an explanation. Could you please provide the rationale for the change?",
    ),
    make_family(
        "GTCL_007","deadline_feasibility","upward","coordinator","manager",
        "A coordinator is already responsible for two deliverables due on Thursday when the manager assigns another substantial deliverable for the same day.",
        "The coordinator tells the manager that the new deadline conflicts with existing commitments.",
        "The disagreement concerns whether all three substantial deliverables can reasonably be completed by Thursday.",
        "Without reprioritization, at least one of the scheduled deliverables may not be completed by the deadline.",
        "I already have two substantial deliverables due Thursday, and this adds a third. I cannot complete all three by Thursday. We need to change a deadline or priority.",
        "I already have two substantial deliverables scheduled for Thursday, and this assignment creates a third concurrent deadline. Completing all three by Thursday is not feasible. We need to revise a deadline or priority.",
        "I wanted to flag that I already have two substantial deliverables due Thursday, and this adds a third. I cannot complete all three by Thursday. Could we change a deadline or priority?",
        "I wanted to raise that I already have two substantial deliverables scheduled for Thursday, and this assignment creates a third concurrent deadline. Completing all three by Thursday is not feasible. Could we revise a deadline or priority?",
    ),
    make_family(
        "GTCL_008","missed_handoff","downward","team_lead","team_member",
        "A team lead and team member agreed that a completed dataset would be handed off by Monday morning for the next stage of analysis.",
        "The Monday morning handoff was missed and the dataset has not yet been delivered.",
        "The team lead raises the missed handoff and asks when the dataset will be provided.",
        "The next stage of analysis cannot begin until the dataset is delivered.",
        "The dataset was due Monday morning and has not been delivered. Please tell me when you will provide it so the analysis can begin.",
        "The dataset was scheduled for handoff Monday morning and has not been delivered. Please confirm when it will be provided so the next analysis stage can begin.",
        "I wanted to check on the dataset that was due Monday morning because it has not arrived yet. Could you please let me know when you will provide it so the analysis can begin?",
        "I wanted to follow up on the dataset scheduled for handoff Monday morning because it has not yet been delivered. Could you please confirm when it will be provided so the next analysis stage can begin?",
    ),
    make_family(
        "GTCL_009","process_compliance","downward","manager","analyst",
        "A manager and analyst had agreed that client-facing figures would be reviewed internally before being sent outside the team.",
        "The analyst sent a set of client-facing figures before completing the agreed internal review step.",
        "The manager raises the skipped review step and asks that the agreed process be followed for future client-facing figures.",
        "Bypassing the review step increases the risk that unreviewed figures are sent externally.",
        "You sent the client-facing figures before the agreed internal review. Please follow the review step before sending figures outside the team.",
        "You sent the client-facing figures before completion of the agreed internal review. Please follow the established review process before external distribution.",
        "I wanted to raise that you sent the client-facing figures before the agreed internal review. Could you please follow the review step before sending figures outside the team?",
        "I wanted to raise that you sent the client-facing figures before completion of the agreed internal review. Could you please follow the established review process before external distribution?",
    ),
    make_family(
        "GTCL_010","resource_allocation","downward","project_lead","team_member",
        "A project lead has two available software licenses and three team members who requested them for the same project period.",
        "The lead allocates the two licenses based on immediate project tasks, and one team member disputes the allocation.",
        "The disagreement concerns the basis used to allocate a limited resource among three requests.",
        "The team must continue the project with only two licenses available during the period.",
        "We have two licenses for three requests, and I allocated them based on the immediate project tasks. You disagree with that allocation. Please explain what alternative basis you think we should use.",
        "We have two licenses available for three requests, and I allocated them according to immediate project requirements. You disagree with that allocation. Please explain what alternative allocation criterion you propose.",
        "I wanted to discuss the allocation. We have two licenses for three requests, and I allocated them based on the immediate project tasks. You disagree with that allocation. Could you explain what alternative basis you think we should use?",
        "I wanted to discuss the allocation. We have two licenses available for three requests, and I allocated them according to immediate project requirements. You disagree with that allocation. Could you please explain what alternative allocation criterion you propose?",
    ),
]

def main():
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    for family in families:
        path = OUT_DIR / f"{family['family_id']}.json"
        path.write_text(json.dumps(family, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    print(f"Generated {len(families)} new Global Team Conflict Lab pilot families.")

if __name__ == "__main__":
    main()
