# Требуется определить, можно ли от шоколадки размером n
# × m долек отломить k долек, если разрешается сделать один разлом по
# прямой между дольками (то есть разломить шоколадку на два
# прямоугольника).
# 3 2 4 -> yes
# 3 2 1 -> no

k = input("Введите количество долек, которое хотим отломить: ")
n = input("Введите количество рядов в шоколодке: ")
m = input("Введите количество столбиков в шоколодке: ")
k = int(k)
n = int(n)
m = int(m)
sum = m * n
if sum > k:
    print(k, n, m, f"-> yes")
else:
    print(k, n, m, f"-> no")