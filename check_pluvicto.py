import requests

url = "https://us.pluvicto.com/api/location-finder"

response = requests.post(url, json={})
data = response.json()

count = len(data)

print("Number of locations:", count)
print("YES" if count > 557 else "NO")
