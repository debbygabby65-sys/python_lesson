prices = []  
for i in range(5):
    prices_of_items = float(input("Enter price of item: "))
    prices.append(prices_of_items)

for price in prices:
    print(price)

total = sum(prices)
print("Total: ", total)

if total >= 10000:
    print("there is discount")
    
    discount = total * 0.10
    final_amount = total - discount

    print("Discount", discount)
    print("Final_amount: ", final_amount)

else:
    print("there is no discount")
    print("final_total: ", total)

