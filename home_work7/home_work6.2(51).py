# 51. Напишите функцию same_by(characteristic, objects), которая проверяет, все ли объекты имеют одинаковое значение некоторой характеристики, 
# и возвращают True, если это так. Если значение характеристики для разных объектов отличается - то False. Для пустого набора объектов, 
# функция должна возвращать True. Аргумент characteristic - это функция, которая принимает объект и вычисляет его характеристику.
# В качестве примера характеристики можно взять проверку четности из лекции, а можно придумать свою.
# Ввод:
# 1 2 3 4 5
# lambda: x%2 == 0
# Вывод:
# False


spisok = input("Введите список чисел: ")
spisok = list(map(int,spisok.split()))

# print(all(map(lambda x: x % 2 == 0, spisok)))

def same_by(characteristic, objects):
    new = list(filter(characteristic, objects))
    if new == objects:
        return True
    return False

def char(x):
    return x % 2 == 0

print(same_by(char, spisok))
