def check_api(config):
    if config["APIURL"] != "" and config["email"] != "":
        return True
    else:
        return False

config = {
    "APIURL": "https://debbygabby.com",
    "email": "debbygabby65@gmail.com"

}  
print(check_api(config))

def convert_age(age):
    try:
        converted_age = int(age)
        return converted_age
    except ValueError:
        return "Invalid age entered"

print(convert_age("20"))
print(convert_age("Debby"))
print(convert_age("15"))


def check_number(number):
    try:
        number = int(number)
    except ValueError:
        return "Invalid number"
    else:
        return "Valid number"

print(check_number("45"))
print(check_number("Debby"))
print(check_number("100"))

def check_price(price):
    try:
        price = float(price)
        if price < 0:
            raise ValueError("price cannot be negative")
        return "price accepted"

    except ValueError as error:
        return str(error)
     

print(check_price("500"))
print(check_price("-100"))
print(check_price("Debby"))

with open("student.txt", "w") as file:
    file.write("My name is Debby")

with open("student.txt", "a") as file:
    file.write("\nI am learning python")

with open("student.txt", "a") as file:
    file.write("\nI am learning API development")

with open("student.txt", "a") as file:
    file.write("\nMy goal is to become a python developer")
    
with open("student.txt", "r") as file:
    content = file.read()
print(content)
