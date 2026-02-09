from typing import Any, Dict, List
import json

from state import GraphState

import ollama

# -- PLANNER NODE --
def planner_node(state: GraphState) -> Dict[str, Any]:
    print("--- NODE: Planner ---")
    user_input = state.get("user_input", "")

    planner_message = {
    'role': 'user',
    'content': f'''
You are a Planner agent.

Blog Content:
{user_input}

Generate exactly three topical tags and one summary sentence.

STRICT OUTPUT RULES:
- Output MUST match the format exactly
- Do NOT add explanations
- Do NOT add introductory text
- Do NOT rename labels

OUTPUT FORMAT (FINAL, EXACT):

Tags:
- tag1
- tag2
- tag3

Summary:
<one sentence, max 25 words>


    '''
}
    # This is the LLM call 
    planner_result = ollama.chat(
    model='smollm:1.7b',
    messages=[
        planner_message,
    ],
    options={"temperature": 0.2}
)

    return {
        "planner_output": planner_result["message"]["content"]
    }

# -- Reviewer Node -- 
def reviewer_node(state: GraphState) -> Dict[str, Any]:
    print("--- NODE: REVIEWER ---")
    
    planner_output = state.get("planner_output", {})

    reviewer_message = {
    'role': 'user',
    'content': f'''
You are a Reviewer agent.

You must follow the rules exactly.
Infer exactly three topical tags from the Planner Output. 
If the summary is missing or too long, rewrite it correctly.

If the planner output violates any rule, explicitly state "ISSUE FOUND".
If everything is correct, state "NO ISSUES".

Planner Output:
{planner_output}

TASK:
1. Choose exactly THREE topical tags that best represent the Planner output.
2. Write ONE summary sentence of at most 25 words.

OUTPUT FORMAT:

Tags:
- tag1
- tag2
- tag3

**Summary Sentence:**
<one sentence, ≤25 words>


'''
}
    # The Reviewer LLM Call to Ollama 
    reviewer_response = ollama.chat(
    model='smollm:1.7b',
    messages=[
        reviewer_message,
    ]
)
    reviewer_output = "ISSUE"
    return {
        "reviewer_output": reviewer_response["message"]["content"]
        #"reviewer_output": reviewer_output
    }
