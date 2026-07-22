lst = [11, 5, 8, 32, 15, 3, 20, 132, 21, 4, 555, 9, 20]

# Вариант 1: цикл for с условием

print("Элементы меньше 30 и делящиеся на 3:")
for num in lst:
    if num < 30 and num % 3 == 0:
        print(num)

# Вариант 2 (альтернативный) – list comprehension и вывод через распаковку

# result = [num for num in lst if num < 30 and num % 3 == 0]
# print(*result, sep="\n")