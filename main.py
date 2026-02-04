from fastapi import FastAPI
from pydantic import BaseModel
from agents.planner import create_plan
from agents.executor import Executor
from agents.verifier import verify

app = FastAPI()
executor = Executor()

class TaskRequest(BaseModel):
    task: str

@app.post("/run")
def run(req: TaskRequest):
    plan = create_plan(req.task)        # Planner
    results = executor.execute(plan)    # Executor
    final = verify(req.task, plan, results)  # Verifier
    return {"result": final}


