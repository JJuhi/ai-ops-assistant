# AI Operations Assistant – GenAI Intern Assignment

## Overview
This project implements an **AI Operations Assistant** that accepts a natural language task, plans the required steps, executes real API calls, and produces a complete end-to-end result using a **multi-agent architecture**.

The system runs locally on localhost, uses an **LLM for structured planning**, integrates **real third-party APIs**, and follows clean separation of responsibilities across agents.

---

## Setup Instructions (Run Locally)

### Prerequisites
- Python 3.10 or above
- Git
- Internet connection (for API calls)

### Steps

```bash
Step 1. Clone the repository:
git clone  https://github.com/JJuhi/ai-ops-assistant.git
cd ai_ops_assistant

Step 2. (Optional) Create and activate a virtual environment:
python -m venv venv
venv\Scripts\activate

Step 2. Install required dependencies:
pip install -r requirements.txt

Step 3. Create environment variables file:
cp .env.example .env

Step 4. Add your API keys inside .env.

Step 5. Run the application locally:
python -m uvicorn main:app

Step 6. After starting the server, open the following URL in your browser:
http://127.0.0.1:8000/docs


###Example Prompts to Test the System

Use the /run endpoint with a JSON body:
{
  "task": "Find trending Python GitHub repositories and weather in Bangalore"
}

## Additional Example Prompts
1. Find trending Python GitHub repositories and weather in Bangalore
2. Show top JavaScript GitHub repositories and weather in London
3. Get popular AI repositories and current weather in New York
4. Find trending backend projects and weather in Berlin
5. List top open-source tools and weather in Tokyo


---

# ✅ SECTION 3: ENVIRONMENT VARIABLES (`.env.example`)

```md
## Environment Variables

Create a `.env` file based on `.env.example`.

Example `.env.example`:
```env
OPENAI_KEY=your_openai_key_here
OPENWEATHER_KEY=your_openweather_key_here

---

# ✅ SECTION 4: ARCHITECTURE EXPLANATION (AGENTS + TOOLS)

```md
## Architecture Explanation (Agents + Tools)

The system follows a modular multi-agent architecture where each agent has a well-defined responsibility.

### Agents

**Planner Agent**
- Converts the user task into a structured execution plan
- Uses an LLM to decide which tools are required
- Outputs a strict JSON plan

**Executor Agent**
- Executes each step in the plan
- Calls external tools and APIs
- Aggregates intermediate results

**Verifier Agent**
- Validates executor output
- Formats a clean final response
- Ensures completeness and consistency

### Tools

**GitHub Tool**
- Uses GitHub Search API
- Fetches popular repositories based on topic and stars

**Weather Tool**
- Uses OpenWeather API
- Fetches real-time weather data for a given city

## Integrated APIs

The project integrates the following real third-party APIs:

1. OpenAI API  
   - Used by the Planner agent for task decomposition and planning

2. GitHub Search API  
   - Used to fetch trending repositories

3. OpenWeather API  
   - Used to retrieve live weather data

## Known Limitations / Trade-offs

- LLM usage depends on API quota availability
- Planner fallback uses deterministic logic when quota is exceeded
- External API rate limits may affect response time
- No persistent database is used (stateless design)
- Designed for clarity and evaluation rather than production scale

## Evaluation Notes

- The project runs locally with a single command
- No responses are hardcoded
- All outputs are generated dynamically
- Multi-agent design is clearly separated
- External APIs are used in real time


