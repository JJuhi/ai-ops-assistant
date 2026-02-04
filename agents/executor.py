from tools.github_tool import search_repos
from tools.weather_tool import get_weather

class Executor:
    def execute(self, plan: dict):
        results = []

        for step in plan["steps"]:
            if step["tool"] == "github":
                results.append(search_repos(step["query"]))

            elif step["tool"] == "weather":
                results.append(get_weather(step["city"]))

        return results
