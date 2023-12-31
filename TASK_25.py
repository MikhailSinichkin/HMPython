# Задача №25. Решение в группах
# Напишите программу, которая принимает на вход
# строку, и отслеживает, сколько раз каждый символ
# уже встречался. Количество повторов добавляется к
# символам с помощью постфикса формата _n.
# Input: a a a b c a a d c d d
# Output: a a_1 a_2 b c a_3 a_4 d c_1 d_1

string = input("Enter a string: ")

unique_chars = dict()
output_string = ""

char_list = string.split()

for char in char_list:
    if char in unique_chars:
        unique_chars[char] += 1
        output_string += f"{char}_{unique_chars[char]} "
    else:
        unique_chars[char] = 0
        output_string += char + " "

print(output_string)


