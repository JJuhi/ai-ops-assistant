import json
from llm.client import call_llm, llm_available

SYSTEM_PROMPT = """
You are a Planner Agent.

Your job is to convert a natural language task into a step-by-step plan.

Rules:
- Return ONLY valid JSON
- Do NOT add explanations
- Do NOT use markdown
- Do NOT add extra text
"""

def create_plan(task: str) -> dict:
    """
    Planner Agent:
    - Uses LLM when available to generate a structured plan
    - Falls back to a deterministic plan if LLM is unavailable or fails
    """
    if not llm_available():
        return {
            "steps": [
                {"tool": "github", "query": "python"},
                {"tool": "weather", "city": "Bangalore"}
            ]
        }

    user_prompt = f"""
Return JSON in the following format ONLY:

{{
  "steps": [
    {{
      "tool": "github",
      "query": "python"
    }},
    {{
      "tool": "weather",
      "city": "Bangalore"
    }}
  ]
}}

Task: {task}
"""

    try:
        response = call_llm(SYSTEM_PROMPT, user_prompt)
        cleaned = (
            response
            .replace("```json", "")
            .replace("```", "")
            .strip()
        )

        plan = json.loads(cleaned)

        if "steps" not in plan or not isinstance(plan["steps"], list):
            raise ValueError("Invalid plan structure")

        return plan

    except Exception:
        return {
            "steps": [
                {"tool": "github", "query": "python"},
                {"tool": "weather", "city": "Bangalore"}
            ]
        }


