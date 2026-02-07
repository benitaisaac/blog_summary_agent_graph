# Blog Summary Stateful Agent Graph

This project demonstrates how to refactor a sequential AI agent pipeline into a **stateful, dynamically routed agent graph** using the LangGraph library. The system implements the **supervisor pattern**, allowing agents to share memory, make decisions based on state, and loop for self-correction.

## Overview

The graph consists of two agents:

- **Planner**: Generates topical tags and a summary from user-provided blog content.
- **Reviewer**: Reviews the Planner’s output and determines whether corrections are needed.

A shared state object allows agents to communicate indirectly, while a router function acts as the supervisor, deciding which agent runs next based on the current state.

## Architecture

- **State (`GraphState`)**  
  A shared dictionary (TypedDict) that stores user input and agent outputs.

- **Nodes**
  - `planner_node`: Reads user input from state and generates tags and a summary using an LLM.
  - `reviewer_node`: Reviews the planner output and updates the state with feedback.

- **Router**
  - `router_logic`: Inspects the shared state and determines whether the system should loop back to the planner or terminate.

- **Workflow Graph**
  - Built using LangGraph’s `StateGraph`
  - Uses conditional edges to enable dynamic routing and looping

## Execution Flow

1. The graph starts at the **Planner** node.
2. The Planner writes its output to shared state.
3. The **Reviewer** reads the Planner’s output and evaluates it.
4. The router decides whether to:
   - Loop back to the Planner for revision, or
   - End execution.

## Running the Project

### Prerequisites
- Python 3.9+
- Ollama running locally
- Required Python packages installed

### Run
```bash
python main.py
