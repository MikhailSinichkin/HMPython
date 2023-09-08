# Задача №19. Решение в группах
# Дана последовательность из N целых чисел и число
# K. Необходимо сдвинуть всю последовательность
# (сдвиг - циклический) на K элементов вправо, K –
# положительное число.
# Input: [1, 2, 3, 4, 5] k = 3
# Output: [4, 5, 1, 2, 3]
# Примечание: Пользователь может вводить значения
# списка или список задан изначально.


n = [1, 2, 3, 4, 5] 
#   [0, 1, 2, 3, 4]    
#   [3, 4, 5, 1, 2]
k = 12
k %= len(n)

d = n[-k:] + n[:-k]
print(d)






