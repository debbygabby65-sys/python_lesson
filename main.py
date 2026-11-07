# import config
# result = config.check_config()
# print(result) 

import json

student = {
    "name": "Debby",
    "age": 20,
    "course": "python"
}
result = json.dumps(student)
print(result)

import json

user = {
    "name": "Debby",
    "email": "debby@gmail.com",
    "role": "admin"
 }
with open("user.json", "w") as file:
    json.dump(user, file, indent=4)

with open("user.json", "r") as file:
    result = json.load(file)
print(result)
print(result["name"])