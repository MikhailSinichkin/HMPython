# функция для нахождения суммы делителей числа
def sum_of_divisors(n):
    divisors = [1] # начинаем со 1, потому что любое число делится на 1
    for i in range(2, int(n**0.5)+1):                                    
        if n % i == 0:
            divisors.append(i)                                                         
            if i != n//i: # добавляем второй делитель, если он отличается от первого    
                divisors.append(n//i)
    return sum(divisors)

k = int(input("Введите число k: "))

# создаем пустой список для хранения найденных пар дружественных чисел
friendly_pairs = []

# перебираем все числа от 1 до k-1
for n in range(1, k):
    m = sum_of_divisors(n) # находим сумму делителей числа n
    if m > n and sum_of_divisors(m) == n: # проверяем, являются ли числа дружественными
        friendly_pairs.append((n,m)) # добавляем пару в список

# выводим найденные пары
for pair in friendly_pairs:
    print(pair[0], pair[1])