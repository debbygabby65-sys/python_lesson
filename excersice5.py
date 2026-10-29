def count_occurrances(numbers, target):
    count = 0
    for num in numbers:
        if count == "target":
            count += 1
    return target
print(count_occurrances([2, 5, 2, 8, 2], target = 3))
print(count_occurrances([1, 4, 7], target = 0))
