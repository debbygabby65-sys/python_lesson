secrete_number = 7
guess = 5
while guess != secrete_number:
    print("Wrong guess")
    guess = int(input("Enter your guess: "))
    if guess > secrete_number:
        print("Too high")
    elif guess < secrete_number:
        print("Too low")
    else:
        print("Congratulations! you guessed correctly")


correct_password = "debbygabby65@"
password = input("enter your password: ")
while password != correct_password:
    print("Wrong password")
    password = input("Try again: ")


if password != correct_password:
    print("incorrect password")
else:
    print("Access granted")

