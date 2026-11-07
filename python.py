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