def count_positive_negative(numbers):
    positive = 0
    negative = 0
    for number in numbers:
        if number > 0:
             positive += 1
        elif number < 0:
            negative += 1
    return positive, negative
print(count_positive_negative([2, -4, 6, -8, 0, 10]))

def count_even_odd(numbers):
    even = 0
    odd  = 0
    for num in numbers:
        if num % 2 == 0:
            even += 1
        else:
            odd += 1
    return even, odd

print(count_even_odd([1, 2, 3, 4, 5, 6, 8]))

def numbers_above_average(numbers):
    result = []
    total = 0
    for number in numbers:
        total += number
    count = len(numbers)
    average = total / count
    for number in numbers:
        if number > average:
            result.append(number)
    return result

print(numbers_above_average([10, 20, 30, 40, 50]))  

def numbers_below_average(numbers):
    result = []
    total = 0
    for num in numbers:
        total += num
    count = len(numbers)
    average = total / count
    for num in numbers:
        if num < average:
            result.append(num)
    return result
print(numbers_below_average([10, 20, 30, 40, 50]))