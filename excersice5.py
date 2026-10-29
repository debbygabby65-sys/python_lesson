def count_occurrances(numbers, target):
    counter = 0
    for value in numbers:
        if value == target:
            counter += 1
    return counter
print(count_occurrances([2, 5, 2, 8, 2], target = 2))
print(count_occurrances([1, 4, 7], target = 10))
