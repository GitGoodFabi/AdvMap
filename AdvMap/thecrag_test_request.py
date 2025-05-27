# thecrag_test_request.py
import requests

url = "https://www.thecrag.com/api/search"
params = {
    "q": "Helicopter",
    "type": "route"
}
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0 Safari/537.36'
}

response = requests.get(url, params=params, headers=headers)

print(f"Status code: {response.status_code}")
print("Response text:")
print(response.text[:1000])  # only show the first 1000 chars
