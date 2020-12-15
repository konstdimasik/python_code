# Напишите программу, которая считывает строку с числом nn, которое
# задаёт количество чисел, которые нужно считать. Далее считывает n строк
# с числами x_i, по одному числу в каждой строке. Итого будет n+1n+1 строк.
#
# При считывании числа x_i программа должна на отдельной строке вывести
# значение f(x_i). Функция f(x) уже реализована и доступна для вызова.
#
# Функция вычисляется достаточно долго и зависит только от переданного
# аргумента xx. Для того, чтобы уложиться в ограничение по времени, нужно
# избежать повторного вычисления значений.
def f(x):
    return x*x*x

n = int(input())
dict = {}
for i in range(n):
    x = int(input())
    if x in dict:
        print(dict[x])
    else:
        y = f(x)
        dict[x] = y
        print(y)

# a = [int(input()) for i in range(int(input()))]
# b = {x:f(x) for x in set(a)}
# [print(b[i]) for i in a]