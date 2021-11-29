def print_formatted(number):
    length = len(format(number, 'b'))
    for i in range(1, number + 1):
        print(f'{i:{length}d} {i:{length}o} {i:{length}X} {i:{length}b}')


if __name__ == '__main__':
    n = 20
    print_formatted(n)
