print("===========================================")
print("     WELCOME TO DEBBY HOSPITAL")
print("===========================================")

patients = {}
doctors = {}
appointments = {}
payments = {}
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

    if patient_id not in patients:
        print("patient ID not found")
    elif doctor_id not in doctors:
        print("doctor ID not found")
    else:
        print("Verification successful!")

        appointment_number = 100 + appointment_counter
        appointment_id = "APPT" + str(appointment_number)
        print(appointment_id)
        appointment_counter += 1

        appointments[appointment_id]= {
            "patient_id": patient_id,
            "doctor_id":  doctor_id,
            "date":  date,
            "time": time,
            "status": "booked"
        }
for appointment_id, details in appointments.items():
    print("appointment_id", appointment_id)
    print(details["patient_id"])
    print(details["doctor_id"])
    print(details["date"])
    print(details["time"])
    print(details["status"])

payment_counter = 1
while payment_counter <= 3:
    appointment_id = input("Enter your appointment id: ")
    payment_amount = float(input("Enter your payment amount: "))
    payment_method = input("Enter your payment method: ")

    if appointment_id not in appointments:
        print("appointment_id not found")
    else:
        print("Appointment verified successfully!")
        payment_number = 100 + payment_counter
        payment_id = "PAY" + str(payment_number)
        print(payment_id)
        payment_counter += 1

        payments[payment_id] = {
            "appointment_id": appointment_id,
            "amount": payment_amount,
            "payment_method": payment_method,
            "status": "paid"
        }

for payment_id, details in payments.items():
    print("payment_id", payment_id)
    print(details["appointment_id"])
    print(details["amount"])
    print(details["payment_method"])
    print(details["status"])

patient_id = input("Enter patient id: ")
if patient_id not in patients:
    print("patient id not found")
else:
    print(patients[patient_id]["name"])
    print(patients[patient_id]["phone"])
    print(patients[patient_id]["age"])
    print(patients[patient_id]["gender"])
    for appointment_id, details in appointments.items():
        
        print("appointment_id", appointment_id)
        print(details["doctor_id"])
        print(details["date"])
        print(details["time"]) 
        print(details["status"])                    