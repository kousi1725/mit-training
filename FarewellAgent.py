from BaseAgent import BaseAgent

def farewell_action(name: str):
    return f"Good Bye !!, {name}!"

class FarewellAgent(BaseAgent):
    def __init__(self):
        super().__init__(
            name="FarewellAgent",
            description="Says goodbye politely.",
            action=farewell_action
        )