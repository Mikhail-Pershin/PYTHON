#Задача №33
# Хакер Василий получил доступ к классному
# журналу и хочет заменить все свои минимальные
# оценки на максимальные. Напишите программу,
# которая заменяет оценки Василия,
# но наоборот: все максимальные – на минимальные.

s = input().split()
min1 = min(s, key=int)
max1 = max(s, key=int)
print(*[min1 if i == max1 else i for i in s])