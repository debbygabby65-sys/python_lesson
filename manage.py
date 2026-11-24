print("==============================")
print("    WELCOME TO DEBBY HOTEL")
print("==============================")

guests = {}
rooms = {}
count = 1
while count <= 3:
    name = input("Enter your full name: ")
    phone_number = input("Enter your phone number: ")
    age = int(input("Enter your age: "))
    number_of_nights = int(input("Enter number of night u intend to stay: "))
    
    if name == "":
        print("Name must not be empty")
    elif len(phone_number) != 11:
        print("Invalid phone number")
    elif age < 18:
        print("you are an underage")
    elif number_of_nights <= 0:
        print("Number must be greater than  zero")
    else:
        print(" Guest infomartion validated successfully!")
        guest_number = 100 + count
        guest_id = "GST" + str(guest_number)
        print("guest_id:", guest_id)
        count += 1
        guests[guest_id] = {
            "name": name,
            "phone": phone_number,
            "Age": age,
            "Nights": number_of_nights

        }

print("============ REGISTERED HOTEL GUESTS ============")
for guest_id, details in guests.items():
    print("guest id", guest_id)
    print(details["name"])
    print(details["phone"])
    print(details["Age"])
    print(details["Nights"])

room_count = 1
while room_count <= 3:
    Room_number = int(input("Enter your room number: "))
    room_type = ["single", "double", "suite"]
    Room_type = input("Enter your room type: (Single, Double, Suite)").strip().lower()
        
    if Room_type in room_type :
        print("Valid room type")
        price = float(input("Enter price per night: "))
        if price <= 0:
            print("price must be greater than zero")
            
        else:
            print("Price accepted")
            availability = "Available"
            room_number = 100 + room_count
            room_id = "ROOM" + str(room_number)
            print("room_id", room_id)
            room_count += 1
            
            rooms[room_id] = {
            "Room_number":  Room_number,
            "Room_type":  Room_type,
            "Price":  price,
            "availability":  availability,
        }
    else:
        print("Invalid room type")
for room_id, details in rooms.items():
    print("room_id", room_id)
    print(details["Room_number"])   
    print(details["Room_type"]) 
    print(details["Price"])
    print(details["availability"])

guest_id = input("Enter your guest id: ")   
if guest_id in guests :
    print("Available rooms")
    for room_id, details in rooms.items():
        if details["availability"] == "Available":
            print(room_id, details["Room_type"], details["Price"])
    room = input("Enter the room you want: ")
    if room in rooms:
        print("Room exist")

        if rooms[room]["availability"] == "Available":
            print("Room is available")
            rooms[room]["availability"] = "Occupied"
            rooms[room]["Guest_ID"] = guest_id
            print("Room successfully booked.")
            total_cost = rooms[room]["Price"] * guests[guest_id]["Nights"]
            
            print("========== BOOKING CONFIRMATION =========")
            
            print("Number of Nights:", guests[guest_id]["Nights"])
            print("Total Accommodation Cost:", total_cost)
 
            print("Guest ID:", guest_id)
            print("Guest Name:", guests[guest_id]["name"])
            print("Phone Number:", guests[guest_id]["phone"])
            print("Room ID:", room)
            print("Room Number:", rooms[room]["Room_number"])
            print("Room Type:", rooms[room]["Room_type"])
            print("Price per Night:", rooms[room]["Price"])
            print("Booking Status:", rooms[room]["availability"])

        else:
            print("Room is occupied")
    else:
        print("Room does not exist")
else:
    print("Guest not found")                                 