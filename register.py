print("=======================================")
print("   WELCOME TO DEBBY SUPERMARKET")
print("=======================================")

customers = {}
inventory = {}
count = 1
while count <= 3:
    customer_name = input("Enter  your name: ") 
    phone_number = input("Enter your phone number: ")
    age = int(input("Enter your age: "))

    if customer_name == "":
        print("Customer name is required.")
    elif len(phone_number) != 11:
        print("Invalid phone number")
    elif age < 18:
        print("Registration denied.")
    else:
        print("registration successful")
        
        print("CUSTOMER REGISTRATION DETAILS")
        
        print("Customer:", customer_name)
        print("Phone number:", phone_number)
        print("Customer age:", age)
        customer_number = 100 + count
        customer_id = "CUS" + str(customer_number)
        print("customer_id:", customer_id)

        customers[customer_id] = {
        "name":  customer_name,
        "phone":  phone_number,
        "age":  age
    }
    count += 1
    
for customer_id, details in customers.items():
    print(customer_id, details)

customer_id = input("Enter your customer_id: ")
if customer_id in customers:
    details = customers[customer_id]
    print(details["name"])
    print(details["phone"])
    print(details["age"])
else:
    print("Customer not found")
    product_name = input("Enter the product name: ")
    price = float(input("Enter your price: "))
    quantity = int(input("Enter your quantity: "))
    inventry = {
        "product":  product_name,
        "price":  price,
        "quantity":  quantity
    }

