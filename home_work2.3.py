# Иван Васильевич пришел на рынок и решил
# купить два арбуза: один для себя, а другой для тещи.
# Понятно, что для себя нужно выбрать арбуз
# потяжелей, а для тещи полегче. Но вот незадача:
# арбузов слишком много и он не знает как же выбрать
# самый легкий и самый тяжелый арбуз? Помогите ему!
# Пользователь вводит одно число N – количество
# арбузов. Вторая строка содержит N чисел,
# записанных на новой строчке каждое. Здесь каждое
# число – это масса соответствующего арбуза

from random import randint
flag = False
while not flag:
    N = int(input('Количество арбузов: '))
    if N > 2:
        flag = True
    else:
        print('Должно юыть как минимум два арбуза')
ivan = 1
mother = 30000
for i in range(0, N, 1):
    massa = randint(1, 30000)
    print(massa)
    if massa > ivan:
        ivan = massa
    elif massa < mother:
        mother = massa

print(f'Арбуз для Ивана весом: {ivan}кг., для Тещи: {mother}кг')