def add_numbers(numbers):
    seen = set()
    for num in numbers:
        seen.add(num)
    return seen
print(add_numbers([10, 20, 30, 10, 40]))

def has_duplicates(numbers):
    seen = set()
    for num in numbers:
        if num in seen:
            return True
        else:
            seen.add(num)
    return False
print(has_duplicates([4, 7, 2, 7, 5]))
print(has_duplicates([1, 2, 3, 4]))    

def first_duplicate(numbers):
    seen = set()
    for num in numbers:
        if num in seen:
            return num
        else:
            seen.add(num)
    return None
print(first_duplicate([4, 7, 2, 7, 5]))
print(first_duplicate([1, 2, 3, 4]))
print(first_duplicate([5, 5, 3]))
