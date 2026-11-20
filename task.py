customer_name = input("Enter your name: ")
account_balance = float(input("Enter you account balance: "))
withdrawal_amount = float(input("Enter your withdral amount: "))

if withdrawal_amount > 0 and  withdrawal_amount <= account_balance:
    remaining_balance = account_balance - withdrawal_amount
    print("Remaining balance:", remaining_balance)
else:
    print("Invalid withdrawal")
print(customer_name)
