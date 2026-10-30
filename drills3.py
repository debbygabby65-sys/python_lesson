def find_largest(numbers):
    
    largest = numbers[0]
    for number in numbers:
        if number > largest:
            largest = number
    return largest
print(find_largest([4, 9, 2, 15, 7]))
print(find_largest([20, 5, 12]))

def find_smallest(numbers):
    smallest = numbers[0]
    for num in numbers:
        if num < smallest:
            smallest = num
    return smallest
print(find_smallest([4, 9, 2, 15, 7]))
print(find_smallest([20, 5, 12]))

def calculate_sum(numbers):
    total = 0
    for number in numbers:
        total += number
    return total

print(calculate_sum([2, 4, 6, 8]))
print(calculate_sum([10, 20, 30]))

def calculate_average(numbers):
    total = 0
    for num in numbers:
        total += num
    count = len(numbers)
    average = total / count
    
    return average

print(calculate_average([10, 20, 30]))
print(calculate_average([5, 10, 15, 20]))

def calculate_average(numbers):
    if not numbers:
        return 0
    total = 0
    for number in numbers:
        total += number
    count = len(numbers)
    average = total / count
    return average

print(calculate_average([10, 20, 30]))
print(calculate_average([5, 10, 15, 20]))

