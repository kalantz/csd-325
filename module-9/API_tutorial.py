import requests
import json

def jprint(obj):
    text = json.dumps(obj, sort_keys=True, indent=4)
    print(text)

try:
    response = requests.get("http://api.open-notify.org/astros.json")
    print(response.status_code)
    jprint(response.json())
except requests.exceptions.ConnectionError as e:
    print(f"Connection error occurred: {e}")