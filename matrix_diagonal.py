import string

symbols = string.ascii_lowercase
size = int(input())
matrix = [['.'] * size for i in range(size)]

for i in range(size):
    for j in range(size):
        k = min(abs(i - j), abs(i + j - (size - 1)))
        matrix[i][j] = symbols[k % 26]

for i in range(size):
    for j in range(size):
        print(matrix[i][j], end='')
    print()
# import string
# alf = string.ascii_lowercase
# n = int(input('n = '))
# a = [[0] * n for i in range(n)]
# for i in range(n):
#     for j in range(n):
#         k = min(abs(i-j), abs(i+j-n+1))
#         a[i][j] = alf[k % 26]
# for row in a:
#     print(row)
#     print()
