def reverse_list(items):
    reverse_list = []
    for i in range(len(items)-1, -1, -1):
        reverse_list.append(items[i])
    return reverse_list
print(reverse_list([1, 2, 3, 4]))
print(reverse_list(["a", "b", "c"]))



