from typing import TypedDict, Dict, Any

class GraphState(TypedDict, total=False):
    user_input: str
    planner_output: Dict[str, Any]
    reviewer_output: Dict[str, Any]