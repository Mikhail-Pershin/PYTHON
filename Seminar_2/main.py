# По данному целому неотрицательному n вычислите
# значение n!. N! = 1 * 2 * 3 * … * N
# (произведение всех чисел от 1 до N) 0! = 1
# Решить задачу используя цикл while

# n = int(input())
# fac = 1
# while n:
#     fac *= n
#     n -= 1
# print(fac)

# N = int(input('Введите число: '))
# num = 2
# fact = 1

# while num<=N:
#     fact *= num 
#     num +=1
# print(fact)



# Дано натуральное число A > 1.
# Определите, каким по счету числом Фибоначчи
# оно является, то есть выведите такое число n,
# что φ(n)=A. Если А не является числом Фибоначчи, выведите число -1.

# 1  2  3  4  5  6  7   8   9  10  11
# 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55,

# n = int(input())

# m1 = 0
# m2 = 1
# i = 2
# while m2 <= n:
#     if m2 == n:
#         print(i)
#         break
#     m1, m2 = m2, m1 + m2
#     i += 1
# else:
#     print(-1)

# Уставшие от необычно теплой зимы, жители решили узнать,
# действительно ли это самая длинная оттепель за всю
# историю наблюдений за погодой. Они обратились к синоптикам,
# а те, в свою очередь, занялись исследованиями статистики
# за прошлые годы. Их интересует, сколько дней длилась самая
# длинная оттепель. Оттепелью они называют период,
# в который среднесуточная температура ежедневно
# превышала 0 градусов Цельсия. Напишите программу,
# помогающую синоптикам в работе.

# Пользователь вводит число N – общее количество
# рассматриваемых дней (1 ≤ N ≤ 100).
# В следующих строках располагается N целых чисел.
# Каждое число – среднесуточная температура в соответствующий день.
# Температуры – целые числа и лежат в диапазоне от –50 до 50

# n = int(input())
# count, max = 0, 0
# for i in range(n):
#     t = int(input())
#     if t < 0:
#         max, count = count, 0
#     count += 1
# print(max)

# n= int(input('Введите количество дней: '))
# count = 0
# max_count = 0

# for n in range (n):
#     temp = int(input('Введите температуру: '))
#     if temp>0:
#         count+=1
#     elif temp<=0:
#         count = 0
#     if count>max_count:
#         max_count=count
# print(max_count)


# Иван Васильевич пришел на рынок и решил купить
# два арбуза: один для себя, а другой для тещи.
# Понятно, что для себя нужно выбрать арбуз потяжелей,
# а для тещи полегче. Но вот незадача: арбузов слишком
# много и он не знает как же выбрать самый легкий
# и самый тяжелый арбуз? Помогите ему!

# Пользователь вводит одно число N – количество арбузов.
# Вторая строка содержит N чисел, записанных на новой
# строчке каждое. Здесь каждое число – это масса соответствующего арбуза

# number = 0
# while number <= 0:
#     number = int(input("Input number: "))

# max_num = 0
# min_num = 999

# for i in range(number):
#     watermelon = int(input(f"Input {i+1} watermelon's weight: "))
#     if watermelon > max_num:
#         max_num = watermelon
#     if watermelon < min_num:
#         min_num = watermelon

# print(max_num, min_num)