examples = [1, 1, 5, 5, 9, 4, 4, 3, 3, 3, 3]


def find_unpaired(items):
    prev = items[0]
    counter = 1
    for index in range(1, len(items)):
        print(f'index = {index}, item = {items[index]}, counter = {counter}')
        if items[index] == prev:
            counter += 1
            prev = items[index]
            continue
        if counter == 2:
            counter = 1
            prev = items[index]
            continue
        return index - 1


print(find_unpaired(examples))
