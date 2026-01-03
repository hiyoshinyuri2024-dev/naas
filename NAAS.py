import json
from typing import Dict, Any, Optional

class EmpathicStateMachine:
    def __init__(self, flow_config: Dict[str, Any]):
        self.config = flow_config
        self.memory = {}
        self.attempts = {}
        self.signals = []

    def listen(self, response: str, state_id: Any) -> Optional[str]:
        if not response.strip():
            return "silence"
        if "?" in response:
            return "questioning"
        if any(word in response.lower() for word in ["don't know", "not sure", "maybe", "perhaps"]):
            return "uncertainty"
        if len(response.strip()) < 5:
            return "brevity"
        return None

    def respond_to_signal(self, signal: str, state: Dict[str, Any]):
        responses = {
            "silence": ["Take your time.", state.get("help_message", "")],
            "uncertainty": ["Uncertainty is natural.", state.get("help_message", "")],
            "brevity": ["Could you tell me more?", state.get("help_message", "")],
            "questioning": ["Let's clarify first to understand your situation."]
        }
        for line in responses.get(signal, []):
            if line:
                print(line)

    def transition(self, state: Dict[str, Any]) -> Optional[str]:
        state_id = state["id"]
        self.attempts[state_id] = 0
        max_attempts = self.config.get("max_attempts", 3)

        while self.attempts[state_id] < max_attempts:
            print(f"\n【{state.get('title', 'Question')}】")
            print(state["prompt"])
            if self.attempts[state_id] > 0 and state.get("help_message"):
                print(state["help_message"])
            response = input("> ").strip()
            signal = self.listen(response, state_id)

            if signal:
                self.attempts[state_id] += 1
                self.signals.append((state_id, signal))
                self.respond_to_signal(signal, state)
                if self.attempts[state_id] >= 2:
                    print("Skip this question? (y/n)")
                    if input("> ").lower() == "y":
                        return "[skipped]"
                continue
            return response

        print("Max attempts reached, moving forward.")
        return None

    def reflect(self):
        print("\nThank you for sharing your responses.")
        if self.signals:
            print("Detected signals:")
            for signal in set(s for _, s in self.signals):
                print(f"  - {signal}: {sum(1 for _, sig in self.signals if sig == signal)} time(s)")

    def flow(self, states: list) -> Dict[str, Any]:
        for state in states:
            response = self.transition(state)
            if response is None:
                break
            self.memory[state["id"]] = response
        self.reflect()
        return self.memory


example_flow = {
    "max_attempts": 3,
    "states": [
        {
            "id": "opening",
            "title": "Opening",
            "prompt": "What brings you here today? (e.g., a question, a problem, just exploring)",
            "help_message": "No wrong answers. Share what comes to mind."
        },
        {
            "id": "depth",
            "title": "Going Deeper",
            "prompt": "Tell me more about that.",
            "help_message": "Consider: When? Where? Who? How did it feel?"
        },
        {
            "id": "reflection",
            "title": "Reflection",
            "prompt": "What would change if this were resolved?",
            "help_message": "Imagine the future outcome."
        }
    ]
}

if __name__ == "__main__":
    machine = EmpathicStateMachine(example_flow)
    memory = machine.flow(example_flow["states"])
    with open("naas_memory.json", "w", encoding="utf-8") as f:
        json.dump(memory, f, ensure_ascii=False, indent=2)
    print("Responses saved to naas_memory.json")
