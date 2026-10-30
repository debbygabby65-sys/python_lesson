def count_duplicates(numbers):
    seen = set()
    count = 0
    for num in numbers:
        if num in seen:
            count += 1
        else:
            seen.add(num)
    return count
print(count_duplicates([1, 2, 2, 3, 3, 3]))
print(count_duplicates([4, 5, 6]))

def unique_numbers(numbers):
    result = []
    for number in numbers:
        if number not in result:
            result.append(number)
    return result

print(unique_numbers([1, 2, 2, 3, 4, 4, 5]))
print(unique_numbers([7, 7, 7, 8, 8]))

def separate_even_odd(numbers):
    even = []
    odd = []
    for number in numbers:
        if number % 2 == 0:
            even.append(number)
        else:
            odd.append(number)
    return even, odd
print(separate_even_odd([1, 2, 3, 4, 5, 6]))


