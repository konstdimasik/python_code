number = int(input())

while not number % 10:
    number = number // 10

zero_counter = 0
for digit in str(number):
    if digit == '0':
        zero_counter += 1

print(zero_counter)
