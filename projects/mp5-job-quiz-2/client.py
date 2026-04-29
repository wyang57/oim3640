import requests

API_KEY = "acGmN-xDyg1-SYaW5-lyV7T"

def fetch_careers(keyword):
    url = f"https://services.onetcenter.org/ws/online/occupations?keyword={keyword}&start=0&end=5"
    response = requests.get(url, auth=(API_KEY, ""))

    if response.status_code != 200:
        return ["There was a problem with the request."]

    data = response.json()
    results = []

    for item in data.get("occupation", []):
        title = item.get("title", "Unknown")
        code = item.get("code", "")
        results.append(f"{title} ({code})")

    return results
