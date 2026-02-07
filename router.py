from __future__ import annotations

from typing import Literal

from state import GraphState


def router_logic(state: GraphState) -> Literal["planner", "reviewer", "END"]:
    
    if "planner_output" not in state: 
        return "planner"
    if "reviewer_output" not in state:
        return "reviewer"

    reviewer_text = str(state.get("reviewer_output")) 

    if "issue" in reviewer_text.lower():
        return "planner"
    
    return "END"
