list_1 = [1, 2, 3, 4, 5]
k = 6

result = [abs(i - k) for i in list_1]
print(list_1[result.index(min(result))])