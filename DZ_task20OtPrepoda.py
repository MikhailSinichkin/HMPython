data = {'AEIOULNSTRАВЕИНОРСТ': 1,
        'DGДКЛМПУ': 2,
        'B, C, M, P, Б, Г, Ё, Ь, Я': 3,
        'F, H, V, W, Y, Й, Ы': 4,
        'K, Ж, З, Х, Ц, Ч': 5,
        'J, X, Ш, Э, Ю': 8,
        'QZФЩЪ': 10}
word = input("Введите слово: ").upper()
# print(word.upper(), word.lower())
count = 0
for char in word:
    for key in data:
        if char in key:
            count += data[key]
print(count)