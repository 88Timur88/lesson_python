# Даны два неупорядоченных набора целых чисел (может быть, с повторениями). 
# Выдать без повторений в порядке возрастания все те числа, которые встречаются в обоих наборах.
# Пользователь вводит 2 числа. n — кол-во элементов первого множества. 
# m — кол-во элементов второго множества. Затем пользователь вводит сами элементы множеств.
from random import randint
a = input("Введите первое число: ")
b = input("Введите второе число: ")
a = int(a)
b = int(b)
c = input("Введите количество чисел в первом множестве: ")
d = input("Введите количество чисел во втором множестве: ")
c = int(c)
d = int(d)
list_1 = [] 
while len(list_1) < c:
    i = randint(a, b)
    list_1.append(i)
list_2 = [] 
while len(list_2) < d:
    i = randint(a, b)
    list_2.append(i)
print(list_1)
print(list_2)
e = set(list_1)
f = set(list_2)
g = list(e.union(f))
g.sort()
print(*g)

