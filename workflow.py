from langgraph.graph import StateGraph, END


from state import GraphState
from nodes import planner_node, reviewer_node
from router import router_logic

def build_workflow():
    workflow = StateGraph(GraphState)

    workflow.add_node("planner", planner_node)
    workflow.add_node("reviewer", reviewer_node)

    workflow.set_entry_point("planner")

    workflow.add_conditional_edges(
        "planner",
        router_logic,
        {
            "planner": "planner",
            "reviewer": "reviewer",
            "END": END,
        }
    )

    workflow.add_conditional_edges(
        "reviewer",
        router_logic,
        {
            "planner": "planner",
            "END": END,
        }
    )

    return workflow.compile()