first = int(input())
second = int(input())
quantity = int(input())

if second % quantity:
    min_second = second // quantity + 1
else:
    min_second = second // quantity

if first > min_second:
    print("Yes")
else:
    print("No")
