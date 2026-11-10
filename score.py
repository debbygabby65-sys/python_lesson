students = {
    "Debby": 100,
    "solo": 88,
    "joy": 77,
    "Gabby": 50
}
for name, score in students.items():
    if score >= 80:
        print(f"{name}, {score}, Grade A")
    elif score >= 70:
        print(f"{name}, {score}, Grade B")
    elif score >= 60:
        print(f"{name}, {score}, Grade C")
    elif  score >= 50:
        print(f"{name}, {score}, Grade D")
    else:
        print(f"{name}, {score}, Grade F")
score = students[name]
name = input("Enter your name: ")
if name in students:
    print(f"{name}, {students[name]}")
else:
    print("Name not found")

total = sum(students.values())
number_of_score = len(students.values())
average = total / number_of_score
print("average", average)

highest_score = max(students.values())
print("highest_score", highest_score)
