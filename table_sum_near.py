# Напишите программу, на вход которой подаётся прямоугольная матрица в виде
# последовательности строк, заканчивающихся строкой, содержащей
# только строку "end" (без кавычек)
#
# Программа должна вывести матрицу того же размера, у которой каждый
# элемент в позиции i, j равен сумме элементов первой матрицы на позициях
#  (i-1, j), (i+1, j), (i, j-1), (i, j+1). У крайних символов соседний элемент
#   находится с противоположной стороны матрицы.
#
# В случае одной строки/столбца элемент сам себе является
#  соседом по соответствующему направлению.

m = []
while True:  # cчитывание данных
    str_in = [i for i in input().split()]
    if str_in == ['end']:
        break
    m.append(str_in)

rows = len(m)
columns = len(m[0])

for i in range(rows):  # вывод новой таблицы
    for j in range(columns):
        x = int(m[i][j - 1]) + int(m[i][j + 1 - columns]) + \
            int(m[i - 1][j]) + int(m[i + 1 - rows][j])
        print(x, end=' ')
    print()

# my first variant:a
# def sum_near(i, j, r, c):  # подсчет суммы соседей
#     return int(m[i][j - 1]) + int(m[i][(j + 1) % c]) + int(m[i - 1][j]) + int(m[(i + 1) % r][j])
#
#
# str_in = input()
# m = []
#
# while str_in != 'end':  # cчитывание данных
#     m.append(str_in.split())
#     str_in = input()
#
# rows = len(m)
# columns = len(m[0])
#
# ms = [[sum_near(i, j, rows, columns) for j in range(columns)] for i in range(rows)]
#
# for i in range(rows):  # вывод новой таблицы
#     for j in range(columns):
#         print(ms[i][j], end=' ')
#     print()
