# Хакер Василий получил доступ к классному журналу и хочет заменить все свои минимальные оценки на максимальные. 
# Напишите программу, которая заменяет оценки Василия, но наоборот: все максимальные – на минимальные.
# [1, 2, 3, 1, 2, 1, 5, 4, 5] -> [1, 2, 3, 1, 2, 1, 1, 4, 1]

# from random import randint
# a = input("Введите количество оценок в журнале: ")
# a = int(a)
# list_1 = [] 
# while len(list_1) < a:
#     i = randint(1, 5)
#     list_1.append(i)
# print(list_1)
# for i in range(1, len(list_1)):
#     if list_1[i] > 4:
#         list_1[i] = 1
# print(list_1)


def zamena(marks: list[int])->list[int]:
    """Рекурсивная замена максимальных оценок минимальными"""
    for i in range(1, len(marks)):
        if marks[i] > 4:
            marks[i] = 1
    return(marks)

print(zamena([1, 5, 3, 5, 5, 1, 4, 5]))