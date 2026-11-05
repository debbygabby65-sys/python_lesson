class Car:
    def start(self):
        print("the car is starting")
my_car = Car()
my_car.start()

class Phone:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
    def introduce(self):
        print(self.brand)
        print(self.model)
phone1 = Phone("Samsung", "S24")
phone1.introduce()

class Laptop:
    def __init__(self, brand, ram, storage):
        self.brand = brand
        self.ram = ram
        self.storage = storage
    def display_info(self):
        print(self.brand)
        print(self.ram)
        print(self.storage)
laptop1 = Laptop("HP", 16, 512)
laptop1.display_info()

class Employee:
    def __init__(self, name, department, salary):
        self.name = name
        self.department = department
        self.salary = salary
    def display_info(self):
        print(f"MY name is {self.name} iam in {self.department} department, i earn {self.salary}  monthly!")
employee1 = Employee("Deborah", "IT", 150000)
employee2 = Employee("Raphael", "Finance", 200000)
employee3 = Employee("Joy", "Marketing", 180000)


employee1.display_info()
employee2.display_info()
employee3.display_info()

class Student:
    school = "Greenfield Academy"
    def __init__(self, name, age):
        self.name = name
        self.age = age
student1 = Student("Deborah", 20)
student2 = Student("John", 22)

print(student1.name)
print(student1.age)
print(student1.school)

print(student2.name)
print(student2.age)
print(student2.school)

    