# receive customer's name
#  receive customer's price
# calculate the total 
# validate it using if, else
# display the customer's name and final amount
#  Ask for the quantity purchased.
#  Multiply the price by the quantity to get the total.
#  Check whether the total is ₦50,000 or more. If it is, calculate a 10% discount; otherwise, keep the original total.


customer_name = input("Enter your name: ")
customer_price = float(input("Enter your price: "))
quantity = int(input("Enter your quantity: "))

total = customer_price * quantity
if total >= 50000:
    discount = total * 0.10
    final_amount = total - discount
else:
    final_amount = total
    print(customer_name)                   
    print(final_amount)
    