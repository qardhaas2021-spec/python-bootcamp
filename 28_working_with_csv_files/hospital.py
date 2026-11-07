import json
import requests



Response = requests.get("https://data.gov.ie/api/3/action/package_search?q=hospital")

data = json.loads(Response.text)

print(data)


for item in data["result"]["results"]:
    print(item["title"])