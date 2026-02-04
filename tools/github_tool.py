import requests

_CACHE = {}

def search_repos(query: str):
    if query in _CACHE:
        return _CACHE[query]

    url = "https://api.github.com/search/repositories"
    params = {
        "q": query,
        "sort": "stars",
        "order": "desc",
        "per_page": 3
    }

    response = requests.get(url, params=params, timeout=10)
    response.raise_for_status()

    data = response.json()

    result = {
        "github_repos": [
            {
                "name": repo["name"],
                "stars": repo["stargazers_count"],
                "url": repo["html_url"]
            }
            for repo in data.get("items", [])
        ]
    }
    _CACHE[query] = result
    return result

