import requests

url = "https://jsonplaceholder.typicode.com/users/2"

headers = {
    "Accept": "application/json"
}
response = requests.get(url, headers=headers)
if response.status_code == 200:
    data = response.json()
    print("Request successfully!")
    print(f"{data['name']}, {data['email']}, {data['phone']}")
else:
    print("Request failed:", response.status_code)


url = "https://jsonplaceholder.typicode.com/users/1"

api_key = "debby_test_123"
headers = {
    "Authorization": f"Bearer {api_key}"
}
response = requests.get(url, headers=headers)
if response.status_code == 200:
    data = response.json()
    print("Request successfully")
    print(F"{data['name']}, {data['email']}")
else:
    print("Request failed:", response.status_code)