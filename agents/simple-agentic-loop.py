"""
Simple Tool-Calling Agent Loop (First-Principles Implementation)
Demonstrates tool invocation, execution reflection, and stop conditions.
"""
import json

TOOLS = {
    "get_weather": lambda loc: f"Sunny, 22°C in {loc}",
    "calculate_metric": lambda a, b: str(float(a) * float(b))
}

def simulate_llm_response(prompt: str):
    if "weather in Lahore" in prompt:
        return {"action": "call_tool", "tool": "get_weather", "arg": "Lahore"}
    return {"action": "final_answer", "answer": "I have completed the task."}

def run_agent_loop(goal: str, max_steps: int = 5):
    print(f"[AGENT] Goal: {goal}")
    for step in range(1, max_steps + 1):
        print(f"--- Step {step} ---")
        decision = simulate_llm_response(goal)
        if decision["action"] == "final_answer":
            print(f"[AGENT] Result: {decision['answer']}")
            break
        elif decision["action"] == "call_tool":
            tool_name = decision["tool"]
            arg = decision["arg"]
            output = TOOLS[tool_name](arg)
            print(f"[AGENT] Executed tool '{tool_name}' -> '{output}'")
            goal = f"Observed: {output}. Provide final answer."

if __name__ == "__main__":
    run_agent_loop("Check the weather in Lahore and summarize.")
