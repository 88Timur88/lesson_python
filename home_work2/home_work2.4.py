# На столе лежат n монеток. Некоторые из них лежат вверх решкой, а некоторые – гербом. Определите минимальное число монеток, 
# которые нужно перевернуть, чтобы все монетки были повернуты вверх одной и той же стороной. 
# Выведите минимальное количество монет, которые нужно перевернуть. С клавиатуры вводятся число монет и сами монеты построчно.
# Пример:
# Ввод: 1 1 1 1 0 0 -> 2
from random import randint
flag = False
while not flag:
    n = int(input('Количество монет: '))
    if n > 2:
        flag = True
    else:
        print('Должно быть как минимум две монеты')
reshka = 1
orel = 0
count1 = 0
count2 = 0
for i in range(n):
    x = randint(0, 1)
    print(x)
    if x == 1:
        count1 += 1
    else:
        count2 +=1
if count1 > count2:
    print(f' -> {count2}')
else:
    print(f' -> {count1}')