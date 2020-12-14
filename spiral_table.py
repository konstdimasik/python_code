# Выведите таблицу размером n×n, заполненную числами от 1 до n^2
# по спирали, выходящей из левого верхнего угла и закрученной по часовой стрелке

size = 4

keys = []  # создание списка пар ключей (длина шага - направление)
key1, key2 = size, 1
keys.append([key1, key2])
for s in range(1, 2 * size - 1):
    if s % 2 == 1:
        key1 = key1 - 1
    else:
        key2 = key2 * (-1)
    keys.append([key1, key2])

step, move_counter, i, j = 1, 0, 0, 0
table = [[0 for j in range(size)] for i in range(size)]

while step <= size * size:
    table[i][j] = step
    if step == size * size:
        break
    keys[move_counter][0] -= 1
    if keys[move_counter][0] == 0:
        move_counter += 1
    if move_counter % 2 == 0:
        j += keys[move_counter][1]
    else:
        i += keys[move_counter][1]
    step += 1

for i in range(size):  # вывод таблицы
    for j in range(size):
        print(table[i][j], end=' ')
    print()

# n=int(input())
# t=[[0]*n for i in range (n)]
# i,j=0,0
# for k in range(1, n*n+1):
#   t[i][j]=k
#   if k==n*n: break
#   if i<=j+1 and i+j<n-1: j+=1
#   elif i<j and i+j>=n-1: i+=1
#   elif i>=j and i+j>n-1: j-=1
#   elif i>j+1 and i+j<=n-1: i-=1
# for i in range(n):
#   print(*t[i])
