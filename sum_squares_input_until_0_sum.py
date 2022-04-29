numbers = []
numbers.append(int(input()))
if numbers[0] == 0:
    print(0)
else:
    sum_numbers = numbers[0]
    i = 0
    while sum_numbers != 0:
        i += 1
        numbers.append(int(input()))
        sum_numbers += numbers[i]
#        print(f'i={i} number={numbers[i]} sum={sum_numbers}')
    sum_squares = 0
    for j in range(i + 1):
        sum_squares += numbers[j] * numbers[j]
    print(sum_squares)

# variant 2
# s=[int(input())]
# while sum(s)!=0:
#    s.append(int(input()))
# print(sum([i**2 for i in s]))

# variant3
# s, d = 0, 0
# while True:
#    a = int(input())
#    s += a
#    d += a*a
#    if s == 0:
#        break
# print(d)
