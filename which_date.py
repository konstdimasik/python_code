# def main():
#     x, y, z = (int(x) for x in input().strip().split())
#     result = 0
#     if 1 <= x <= 31 and 1 <= y <= 12:
#         result += 1
#     if 1 <= y <= 31 and 1 <= x <= 12:
#         result += 1
#     print(result % 2)
#
#
# main()


def main():
    a, b, c = map(int, input().split())
    if a == b:
        print(1)
    elif b <= 12 and a <= 12:
        print(0)
    else:
        print(1)


main()
