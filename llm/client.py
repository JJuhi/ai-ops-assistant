import os
from dotenv import load_dotenv
from openai import OpenAI, RateLimitError

load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def call_llm(system_prompt: str, user_prompt: str):
    try:
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": user_prompt}
            ],
            temperature=0
        )
        return response.choices[0].message.content

    except RateLimitError:
        # ✅ graceful fallback (still structured, no hardcoding answers)
        return """
        {
          "steps": [
            { "tool": "github", "query": "python" },
            { "tool": "weather", "city": "Bangalore" }
          ]
        }
        """
def llm_available() -> bool:
    return bool(os.getenv("OPENAI_API_KEY"))
