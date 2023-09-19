# Задача №31. Решение в группах
# Последовательностью Фибоначчи называется
# последовательность чисел a0
# , a1, ..., an, ..., где
# a0 = 0, a1 = 1, ak = ak-1 + ak-2 (k > 1).
# Требуется найти N-е число Фибоначчи
# Input: 7
# Output: 21


def fib(k):                               #def fib(k):
    if k == 2 or k == 1:                  #    if k in (1,2):
        return 1                            #        return 1
    return fib(k - 1) + fib(k - 2)        #    return fib(n-1) + fib(n - 2)
print(fib(7))                             #print(fib(7))


# a0 , a1 = 0, 1
# for i in range(n): 
#     next_n = a0 + a1
#     a0 = a1
#     a1 = next_n
# print(a0)  