import json
import requests

products = {
    "name": "Laptop",
    "price": 500000,
    "brand": "HP"
}

url = "https://jsonplaceholder.typicode.com/posts"
response = requests.post(url, json=products)
print(response.status_code)
print(response.json())
           
url = "https://jsonplaceholder.typicode.com/posts"

headers = {
    "content-type": "application/json"
}

products = {
    "name": "phone",
    "price": 300000
}
response = requests.post(url, json=products, headers=headers)
print(response.status_code)
print(response.json())


url = "https://jsonplaceholder.typicode.com/posts"

params = {
    "userId": 2
}
response = requests.get(url, params=params)
print(response.status_code)
print(response.json())


url = "https://jsonplaceholder.typicode.com/posts/1"

post = {
    "title": "My python journey",
    "body": "I am learning API development",
    "userId": 1
}
response = requests.put(url, json=post)
print(response.status_code)
print(response.json())


url = "https://jsonplaceholder.typicode.com/posts/5"
response = requests.delete(url)
print(response.status_code)