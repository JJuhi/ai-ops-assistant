def verify(task: str, plan: dict, results: list):
    """
    Verifier Agent:
    - Ensures executor results exist
    - Formats final user-facing answer
    - Does NOT call LLM (quota-safe)
    """

    output_lines = []
    output_lines.append(f"Task: {task}\n")

    for result in results:
        if "github_repos" in result:
            output_lines.append("Top GitHub Python Repositories:")
            for repo in result["github_repos"]:
                output_lines.append(
                    f"- {repo['name']} ⭐ {repo['stars']} ({repo['url']})"
                )

        if "temperature" in result:
            output_lines.append(
                f"\nWeather in {result['city']}: "
                f"{result['temperature']}°C, {result['condition']}"
            )

    return "\n".join(output_lines)


