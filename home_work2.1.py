# Уставшие от необычно теплой зимы, жители решили узнать,
# действительно ли это самая длинная оттепель за всю историю
# наблюдений за погодой. Они обратились к синоптикам, а те, в
# свою очередь, занялись исследованиями статистики за
# прошлые годы. Их интересует, сколько дней длилась самая
# длинная оттепель. Оттепелью они называют период, в
# который среднесуточная температура ежедневно превышала
# 0 градусов Цельсия. Напишите программу, помогающую
# синоптикам в работе.
# Пользователь вводит число N – общее количество
# рассматриваемых дней (1 ≤ N ≤ 100). В следующих строках
# располагается N целых чисел.
# Каждое число – среднесуточная температура в
# соответствующий день. Температуры – целые числа и лежат в
# диапазоне от –50 до 50

# flag = False
# while not flag:
#     period = int(input('Period: '))
#     if not (period > 100 or period < 1):
#         flag = True
#     else:
#         print('Период должен быть от 1 до 100')
# 1
# start = 0
# end = period
# step = 1
# count = 0
# mx_count = 0
# for i in range(start, end, step):
#     temperature = int(input('Temperature: '))
#     if temperature > 0:
#         count += 1
#     else:
#         if count > mx_count:
#             mx_count = count
#         count = 0
# print(f'Максимальная оттепель {mx_count}')

from random import randint

flag = False
while not flag:
    period = int(input('Period: '))
    if not (period > 100 or period < 1):
        flag = True
    else:
        print('Период должен быть от 1 до 100')
1
start = 0
end = period
step = 1
count = 0
mx_count = 0
for i in range(start, end, step):
    temperature = randint(-50, 50)
    print(f'Temperature: {temperature}')
    if temperature > 0:
        count += 1
    else:
        if count > mx_count:
            mx_count = count
        count = 0
print(f'Максимальная оттепель {mx_count}')
