print("===========================================")
print("     WELCOME TO DEBBY HOSPITAL")
print("===========================================")

patients = {}
doctors = {}
appointments = {}
counter = 1
while counter <= 3:
    name = input("Enter your full name: ")
    phone_number = input("Enter your phone number ").strip()
    age = int(input("Enter your age: "))
    gender = input("Enter your gender: ").strip().lower()
    print(name)
    print(phone_number)
    print(age)
    print(gender)

    if name == "":
        print("Name must not be empty")
    elif len(phone_number) != 11:
        print("Number must contain 11 characters")
    elif age < 18:
        print("Age must be 18 and above")
    elif gender not in ["male", "female"]:
        print("Gender must be a male or female")
    else:
        print("patient information validate successfully!")

        patient_number = 100 + counter
        patient_id = "PAT" + str(patient_number)
        print(patient_id)
        counter += 1

        patients[patient_id] = {
            "name": name,
            "phone": phone_number,
            "age": age,
            "gender": gender
        }


print("========= REGISTERED HOSPITAL PATIENTS ========")

for patient_id, details in patients.items():
    print("patient_id", patient_id)
    print(details["name"])
    print(details["phone"])
    print(details["age"])
    print(details["gender"])

doctor_counter = 1
while doctor_counter <= 3:
    name = input("Enter your full name: ")
    phone_number = input("Enter your phone number: ").strip()
    age = int(input("Enter your age: "))
    medical_specialisation = input("Enter your medical specialisation: ")
    print(name)
    print(phone_number)
    print(age)
    print(medical_specialisation)

    if name == "":
        print("name must not be empty")
    elif len(phone_number) != 11:
        print("Invalid phone number")
    elif age < 25:
        print("Age must be 25 and above")
    elif medical_specialisation == "":
        print("medical specialisation must not be empty")
    else:
        print("doctor validated successfully!")

        doctor_number = 100 + doctor_counter
        doctor_id = "DOC" + str(doctor_number)
        print(doctor_id)
        doctor_counter += 1
        
        doctors[doctor_id] = {
            "name": name,
            "phone": phone_number,
            "age": age,
            "specialisation": medical_specialisation
        }
print("========= REGISTERED HOSPITAL DOCTORS =========")
for doctor_id, details in doctors.items():
    print("doctor_id", doctor_id)
    print(details["name"])
    print(details["phone"])
    print(details["age"])
    print(details["specialisation"])

appointment_counter = 1
while appointment_counter <= 3:
    patient_id = input("Enter your patient id: ")
    doctor_id = input("Enter your doctor id: ") 
    date = input("Enter your date: ")
    time = input("Enter your time: ")
    print(patient_id)
    print(doctor_id)
    print(date)
    print(time)
