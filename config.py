settings = {
    "APIURL": "https://debbygabby.com",
    "email": "debbygabby@gmail.com"
}

def check_config():
    if settings["APIURL"] != "" and settings["email"] != "":
        return True
    return False


f