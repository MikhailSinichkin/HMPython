# Задача №37. Решение в группах
# 15 минут
# Дано натуральное число N и
# последовательность из N элементов.
# Требуется вывести эту последовательность в
# обратном порядке.
# Примечание. В программе запрещается
# объявлять массивы и использовать циклы
# (даже для ввода и вывода).
# Input: 2 -> 3 4
# Output: 4 3

# def reversN(n):
#     if n > 0:
#         num = int(input("Enter a number "))
#         reversN(n-1)
#         print (num , end=" ")


# n = int(input("Enter a number "))
# reversN(n)

def f(n):
    if n == 0:
        return ""
    k = int(input("Введите число"))
    return f(n-1) + f" {k}"
n = int(input("Введите количество чисел"))
print(f(n))
