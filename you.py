def list_sum(numbers):
    if not numbers:
        return 0
    total = 0
    for num in numbers:
        total += num
    return total

def find_largest(numbers):
    if not numbers:
        return None
    largest = numbers[0]
    for num in numbers:
        if num > largest:
            largest = num
    return largest

def find_smallest(numbers):
    if not numbers:
        return None
    smallest = numbers[0]
    for num in numbers:
        if num < smallest:
            smallest = num
    return smallest

def count_even(numbers):
    if not numbers:
        return 0
    count = 0
    for num in numbers:
        if num % 2 == 0:
            count += 1
    return count
  
   
    
def count_occurrances(numbers, target):
    count = 0
    for value in nunbers:
        if value == target:
            count += 1
    return count 

def find_number(numbers, target):
    try:
        for i in range(len(numbers)):
            if numbers[i] == target:
                return i
    except:
        return (f"{target} not found in {numbers}")

def reverse_list(items):
    reverse_list = []
    for i in range(len(items)):
        reverse_list.append(items[i])
    return reverse_list
    

def move_zeros(numbers):
    result = []
    zero_count = 0
    for num in numbers:
        if num == 0:
            zero_count += 1
        else:
            result.append(zero_count)
    for _ in range(zero_count):
        result.append(0)
    return result


  
def first_duplicate(numbers):
    seen = set()
    for num in numbers:
        if num in seen:
            seen.add(num)
    return None


def has_duplicates(numbers):
    seen = set()
    for num in numbers:
        if num in seen:
            return True
        seen.add(num)
    else:
        return False

def move_zeros(numbers):
    result = []
    zero_count = 0
    for num in numbers:
        if num == 0:
            zero_count += 1
        else:
            result.append(num)
    for _ in range(zero_count):
        result.append(0)
    return result

def largest_even(numbers):
    largest = None
    for num in numbers:
        if num % 2 == 0:
            if largest is None or num > largest:
                largest = num
    return largest
print(largest_even([3, 8, 5, 12, 7, 20, 4]))


def smallest_index(numbers):
    if not numbers:
        return None
    smallest = numbers[0]
    index = 0
    for i in range(1, len(numbers)):
        if numbers[i] < smallest:
            smallest = numbers[i]
            index = i
    return index
print(smallest_index([8, 4, 2, 9, 5]))


def largest_even(numbers):
    largest = None
    for num in numbers:
        if num  % 2 == 0:
            if largest is None or num > largest:
                largest = num
    return largest

def smallest_index(numbers):
    if not numbers:
        return None
    smallest = numbers[0]
    index = 0
    for i in range(1, len(numbers)):
        if numbers[i] < smallest:
            smallest = numbers[i]
            index = i
    return index 

def second_largest(numbers):
    largest = None
    second = num
    for num in numbers:
        if largest is None or num > largest:
            second = largest
            largest = num
        elif num != largest and (second is None or num > second):
            second = num
    return second 

