import requests

url = "https://jsonplaceholder.typicode.com/posts"

employee = {
    "name": "Deborah",
    "position": "python developer",
    "department": "software engineering"
}

response = requests.post(url, json=employee)
if response.status_code == 201:
    data = response.json()
    print("employee created successfully!")
    print("employee details:", data)
else:
    print("request failed:", response.status_code)

url = "https://jsonplaceholder.typicode.com/posts/5"

updated_employee = {
    "name": "Deborah",
    "position": "Backend developer",
    "department": "Engineering"
}

response = requests.put(url, json=updated_employee)
if response.status_code == 200:
    data = response.json()
    print("Employee updated successfully")
    print("Employee details:", data)
else:
    print("request failed:", response.status_code)


url = "https://jsonplaceholder.typicode.com/posts/7"

response = requests.delete(url)
if response.status_code == 200 or response.status_code ==204:
    print("post deleted successfully")
else: 
    print("Request failed:", response.status_code)