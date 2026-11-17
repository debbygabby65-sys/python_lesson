import requests

url = "https://jsonplaceholder.typicode.com/posts"

params = {
    "userId": 3
}
response = requests.get(url, params=params)
if response.status_code == 200:
    data = response.json()
    for post in data:
        print("post Id", post["id"])
        print("Title", post["title"])
else:
    print("Request failed", response.status_code)


url = "https://jsonplaceholder.typicode.com/posts"

params = {
    "userId": 3,
    "id": 25
}

response = requests.get(url, params=params)
if response.status_code == 200:
    data = response.json()
    for post in data:
        print("post Id", post["id"])
        print("Title", post["title"])
        print("userId", post["userId"])
else:
    print("Request failed", response.status_code)