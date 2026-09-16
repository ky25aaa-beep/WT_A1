import requests

TOKEN = "NWZmMWJhZDUtMWVjYi00Mzg2LWJlYzMtNWQ1ZGUxZmE1Yjc4YmIwMTY1NTctNWI2_PE93_c18e13ae-5575-4bc0-ae01-e48905f14f17"

headers = {
    "Authorization": f"Bearer {TOKEN}",
    "Content-Type": "application/json"
}

response = requests.get(
    "https://webexapis.com/v1/rooms",
    headers=headers
)

response.raise_for_status()

for room in response.json()["items"]:
    print(room["title"])
    print(room["id"])
    print()