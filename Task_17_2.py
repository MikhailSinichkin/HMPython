numbers = [1, 1, 2, 0, -1, 3, 4, 4]
help_list = []
for i in range(len(numbers)):
    if numbers[i] not in help_list:
        help_list.append(numbers[i])
print(help_list)