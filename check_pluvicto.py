import requests

url = "https://us.pluvicto.com/api/location-finder"

try:
    response = requests.post(url, json={}, timeout=10)

    # sprawdzamy czy odpowiedź jest OK
    if response.status_code != 200:
        print("API returned status:", response.status_code)
        print("NO")
        exit(0)

    try:
        data = response.json()
    except ValueError:
        print("API did not return valid JSON")
        print("NO")
        exit(0)

    count = len(data)
    print("Number of locations:", count)
    print("YES" if count > 575 else "NO")

except Exception as e:
    print("Request failed:", str(e))
    print("NO")
