#Задача №31  Фибоначчи
# Последовательностью Фибоначчи называется
# последовательность чисел a0, a1, ..., an, ...,
# где # a0 = 0, a1 = 1, ak = ak-1 + ak-2 (k > 1).
# Требуется найти N-е число Фибоначчи

def fib(num):
    if num in [0, 1]:
        return 1
    return fib(num - 1) + fib(num  - 2)

n = int(input())

print(fib(n))