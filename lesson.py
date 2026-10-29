import json
print("===== STUDENT REGISTRATION SYSTEM ====")
print("1. Create Ticket")
print("2. View Tickets")
print("3. Exit")

choice = input("Enter your choice: ")
if choice == "1":
    student_name = input("Enter your name: ")
    student_id = input("Enter your id: ")
    student_age = input("Enter your age: ")
    issue = input("Describe your regristration problem: ")

    ticket = {
        "student_name": student_name,
        "student_id": student_id,
        "student_age": student_age,
        "issue": issue,
        "status": "open"
    }
    try:
        with open("tickets.json", "r") as file:
            tickets = json.load(file)
            if isinstance(tickets, dict):
                tickets = [tickets]
                
    except fileNotFoundError:
        tickets = []
    tickets.append(ticket)    

    with open("tickets.json", "w") as file:
        json.dump(tickets, file, indent=4)
    print("ticket created successfully!")

elif choice == "2":
    with open("tickets.json", "r") as file:
        ticket = json.load(file)
    for key, value in ticket.items():
        print(f"{key}: {value}")

elif choice == "3":
    print("Thank you for using the student registration system. Goodbye!")