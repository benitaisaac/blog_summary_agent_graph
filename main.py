from workflow import build_workflow

def main():
    app = build_workflow()

    initial_state = {
        "user_input": """
Wicked is a musical that reimagines the story of the witches from The Wizard of Oz.
It explores themes of friendship, identity, and how history is shaped by those in power.
"""
    }

    #final_state = app.invoke(initial_state)

    #print("\nFINAL STATE:\n")
    #print(final_state)

    for step in app.stream(initial_state):
        print(step)


if __name__ == "__main__":
    main()
