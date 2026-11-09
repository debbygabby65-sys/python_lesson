import requests

BASE_URL = "https://jsonplaceholder.typicode.com"

def get_post(post_id):
    url = f"{BASE_URL}/posts/{post_id}"
    response = requests.get(url)

    return response.json()

post = get_post(5)
print(post)

url = "https://jsonplaceholder.typicode.com/posts/500"

def get_post(post_id):
    response = requests.get(url)

    print("status", response.status_code)
    print("data", response.json())

    try: 

       response.raise_for_status()
       print("no error detected")
       
    except requests.exceptions.RequestException as error:
        print("error caught", error)

get_post(500)
print(post)