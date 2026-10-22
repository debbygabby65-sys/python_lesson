def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b
    
def divide(a, b):
    return  a / b

num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

choice = input("Choose 1 for addition or 2 for subtraction or 3 for mutiplication or 4 for division: ")  

if choice == "1":
    ans = add(num1, num2)
    print(ans)

elif choice == "2":
    sub = subtract(num1, num2)
    print(sub)

elif choice == "3":
    sen = multiply(num1, num2)
    print(sen)

elif choice == "4":
    result = divide(num1, num2)
    
else:
    print("invalid choice")
