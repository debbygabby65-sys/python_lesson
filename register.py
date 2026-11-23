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
    selected_customer = details["name"]
    print(details["name"])
    print(details["phone"])
    print(details["age"])
    product_count = 1
    while product_count <= 3:    
        product_name = input("Enter the product name: ")
        price = float(input("Enter your price: "))
        quantity = int(input("Enter your quantity: "))

        inventory[product_name] = {
            "price":  price,
            "quantity":  quantity
        }
        product_count += 1

    print("=============== PRODUCT INVENTORY ============")

    for product_name, details in  inventory.items():
        print(details)
    product_name = input("Enter your product name: ")

    if product_name in inventory:
        details = inventory[product_name]
        print("product:", product_name)
        print("Price:", details["price"])
        print("Quantity:", details["quantity"])

    product_name = input("Enter the product name: ")
    if product_name in inventory:

        purchase_quantity = int(input("Enter how many units you want to buy: "))
        if purchase_quantity > 0:
            details = inventory[product_name]

            if purchase_quantity <= details["quantity"]:
                details["quantity"] = details["quantity"] - purchase_quantity
                print("purchase successful")
                print("Available stock:", details["quantity"])
                total_amount = details["price"] * purchase_quantity
                print(selected_customer)
                print(product_name)
                print(details["price"])
                print(purchase_quantity)
                print(f"{total_amount:,.2f}")
            else:
                print("Insufficient stock")
                print("Available stock:", details["quantity"]) 
        else:
            print("Invalid purchase quantity!")        
    else:
        print("product not found!")

else:
    print("Customer not found")

