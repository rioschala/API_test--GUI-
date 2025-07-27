import requests

try:
    response = requests.get("https://naas.isalman.dev/no", timeout=10)
    print("Status code:", response.status_code)
    print("Response text:", response.text[:200])  # show first 200 chars
except requests.exceptions.RequestException as e:
    print("Request failed:", e)