# AI Operations Assistant – GenAI Intern Assignment

## Overview
This project implements an **AI Operations Assistant** that accepts a natural language task, plans the required steps, executes real API calls, and produces a complete end-to-end result using a **multi-agent architecture**.

The system runs locally on localhost, uses an **LLM for structured planning**, integrates **real third-party APIs**, and follows clean separation of responsibilities across agents.

---

## Setup Instructions (Run Locally)

### Prerequisites
- Python 3.9 or higher
- Git
- OpenAI API key
- OpenWeather API key

### Steps to take

```bash
git clone <your-github-repository-url>
cd ai_ops_assistant
pip install -r requirements.txt
cp .env.example .env
python -m uvicorn main:app
After starting the server, open the following URL in your browser: http://127.0.0.1:8000/docs

###Example Prompts to Test the System

Use the /run endpoint with a JSON body:
{
  "task": "Find trending Python GitHub repositories and weather in Bangalore"
}

Additional example prompts:-
- Find popular Python GitHub repositories and weather in Delhi
- Show trending open-source Python projects and weather in Mumbai
- Get top Python repositories and current weather in Chennai
- List popular GitHub Python repositories and Bangalore weather


###Environment Variables (.env.example)
Create a .env file using .env.example and provide the following values:
- OPENAI_API_KEY=your_openai_api_key
- OPENWEATHER_API_KEY=your_openweather_api_key

## Architecture Explanation (Agents + Tools)

The system follows a **multi-agent architecture** where each agent has a clear and isolated responsibility. This design improves modularity, reliability, and ease of evaluation.

### Agents

**Planner Agent**
- Converts the user’s natural language task into a structured JSON execution plan
- Uses an LLM to reason about required steps and tool selection
- Ensures output follows a strict schema
- Gracefully falls back to a deterministic plan if LLM access or quota is unavailable

**Executor Agent**
- Executes each step defined in the plan
- Calls the appropriate tools and third-party APIs
- Collects raw results from external services

**Verifier Agent**
- Validates the executor’s results for completeness
- Formats a clean, user-friendly final response
- Deterministic and quota-safe to ensure reliable end-to-end execution

### Tools

**GitHub Tool**
- Integrates with the GitHub Search API
- Fetches popular repositories based on stars and query parameters

**Weather Tool**
- Integrates with the OpenWeather API
- Fetches live weather data for a given city

###Integrated APIs

- GitHub Search API
- OpenWeather API
All APIs are real and live. No mocked data or hard-coded responses are used.

###Limitations / Tradeoffs

- LLM usage is limited to the planning phase; the system degrades gracefully when LLM access or quota is unavailable.
- API response caching is in-memory and resets when the application restarts.
- The system is optimized for small task graphs and single-node execution.
