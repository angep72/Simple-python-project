import requests
response = requests.get("http://127.0.0.1:5000/get-users")
result = response.json()
print (result["users"][0]["email"])