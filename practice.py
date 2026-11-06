class Vehicle:
    def start(self):
        print("Vehicle is starting")
class Car(Vehicle):
    def drive(self):
        print("Car is driving")

my_car1 = Car()

my_car1.start()
my_car1.drive()


class Employee:
    def work(self):
        print("Employee is working")
class Developer(Employee):
    def work(self):
        print("Developer is writing code")

developer1 = Developer()
developer1.work()


numbers = []
for i in range(5):
    number = int(input("Enter a number:"))
    numbers.append(number)
for number in numbers:
    if number >= 80:
        print(number, "-Grade A")
    elif number >= 70:
        print(number, "-Grade B")
    elif number >= 60:
        print(number, "-Grade C")
    elif number >= 50:
        print(number, "-Grade D")
    else: 
        print(number, "-Grade F")

    if number % 2 == 0:
        print(number, "is even")
    else:
        print(number, "is odd")

total = sum(numbers)
print(total)

largest_number = max(numbers)
print(largest_number)

smallest_number = min(numbers)
print(smallest_number)

average = total / len(numbers)
print(average)


