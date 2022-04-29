# def main():
#     a, b = (int(x) for x in input().split())
#
#     print(a + b)
#
#
# main()
#
#
# def main():
#     with open('input.txt', 'r') as file_in:
#         a, b = (int(x) for x in file_in.readline().split())
#
#     with open('output.txt', 'w') as file_out:
#         file_out.write(str(a + b))
#
#
# main()
#
#
# import sys
#
# j = sys.stdin.readline().strip()
# s = sys.stdin.readline().strip()
#
# result = 0
# for ch in s:
#     if ch in j:
#         result += 1
#
# print result


def main():
    with open('input.txt', 'r') as file_in:
        r = int(file_in.readline().strip())
        i = int(file_in.readline().strip())
        c = int(file_in.readline().strip())

    match i:
        case 0:
            if r != 0:
                result = 3
            else:
                result = c
        case 1:
            result = c
        case 4:
            if r != 0:
                result = 3
            else:
                result = 4
        case 6:
            result = 0
        case 7:
            result = 1
        case _:
            result = i

    with open('output.txt', 'w') as file_out:
        file_out.write(str(result))


main()
