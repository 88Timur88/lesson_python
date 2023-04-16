# Требуется вывести все целые степени двойки (т.е. числа вида 2^k), не превосходящие числа N.

# Пример:
# Ввод: 13 -> 1, 2, 4, 8

N = int(input("Введите число N: "))

flag = False
while not flag:
    if not (N < 0):
        flag = True
    else:
        print('Введенное число должно быть больше нуля')
        break
k = 0
rez = 0
while rez < N:
    rez =  2 ** k
    if rez < N:
        print(rez)
        k += 1