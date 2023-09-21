# Задача №51. Решение в группах
# Напишите функцию same_by(characteristic, objects), которая
# проверяет, все ли объекты имеют одинаковое значение
# некоторой характеристики, и возвращают True, если это так.
# Если значение характеристики для разных объектов
# отличается - то False. Для пустого набора объектов, функция
# должна возвращать True. Аргумент characteristic - это
# функция, которая принимает объект и вычисляет его
# характеристику.
# Ввод: Вывод:
# values = [0, 2, 10, 6] same
# if same_by(lambda x: x % 2, values):
# print(‘same’)
# else:
# print(‘different’)

values = [0, 2, 10, 6, 5]
def same_by(characteristic, objects):
    value2 = list(map(characteristic, objects))
    for i in range(len(value2)):
        if value2[i-1] != value2[i]:
            return False
    return True
if same_by(lambda x: x % 2, values):
    print("same")
else:
    print("different")
        