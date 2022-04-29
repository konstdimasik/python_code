def main():
    with open('input.txt', 'r') as file_in:
        n = int(file_in.readline().strip())
        i = [int(x) for x in file_in.readline().strip().split()]
    result = i[n // 2]


    with open('output.txt', 'w') as file_out:
        file_out.write(str(result))


main()

# плюс сортировка если неотсортированы входные данные
