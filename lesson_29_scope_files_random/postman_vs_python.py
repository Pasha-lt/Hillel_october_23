import requests
import json

url = "https://postman-rest-api-learner.glitch.me//info"

# payload = json.dumps({
#   "name": "Add your name in the body"
# })

payload = {"name": "Add your name in the body"}

headers = {
  'Content-Type': 'application/json'
}

response = requests.request("POST", url, headers=headers, json=payload)

print(response.text)
