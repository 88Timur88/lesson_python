# Задача 32: Определить индексы элементов массива (списка), значения которых принадлежат
# заданному диапазону (т.е. не меньше заданного минимума и не больше заданного максимума)

# Input:
# 1, 3, 7, 10, 5, 8 - рассматриваемый список
# 4 - начало диапазона
# 8 - конец
# Output:
# 2(7), 4(5), 5(8)

min = int(input("Введите минимальное значение: "))
max = int(input("Введите максимальное значение: "))

from random import randint
a = int(input("Введите чисел в массиве журнале: "))
list_1 = []
while len(list_1) < a:
    i = randint(1, 10)
    list_1.append(i)
    list_1 = map(int, list_1)
print(list_1)

for i in range(len(list_1)):
    if min <= list[i] <= max:
        print(i)

