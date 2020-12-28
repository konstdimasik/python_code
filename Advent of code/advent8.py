import copy


def read_file(file):
    operation_list = []
    for line in file:
        sep = line.strip('\n').split(' ')
        operation_list.append(sep)
    return operation_list


def find_loop(operation_list):
    """
    Идем последовательно по списку операций, запоминаем:
    последнюю позицию до цикла, сумму к этому моменту и
    список последовательно выполненыех команд
    """
    positions_set = set()
    positions_list = []
    sum = 0
    position = 0
    while True:
        if position in positions_set:
            break
        if position == len(operation_list):
            return sum, -1, positions_list
        if operation_list[position][0] == 'nop':
            positions_set.add(position)
            positions_list.append(position)
            position += 1
            continue
        if operation_list[position][0] == 'jmp':
            positions_set.add(position)
            positions_list.append(position)
            position += int(operation_list[position][1])
            continue
        if operation_list[position][0] == 'acc':
            positions_set.add(position)
            positions_list.append(position)
            sum += int(operation_list[position][1])
            position += 1
    return sum, position, positions_list


def find_corrupted(operation_list, positions_list):
    """
    Последовательно идем с конца по списку выполненых команд,
    пробуем подменять команды и проверяем дойдем ли до конца списка операций
    """
    i = len(positions_list) - 1
    while i >= 0:
        position = positions_list[i]
        if operation_list[position][0] == 'nop':
            new_oper_list = copy.deepcopy(operation_list)
            new_oper_list[position][0] = 'jmp'
            accum, position, pos_list = find_loop(new_oper_list)
            if position == -1:
                return accum
        if operation_list[position][0] == 'jmp':
            new_oper_list = copy.deepcopy(operation_list)
            new_oper_list[position][0] = 'nop'
            accum, position, pos_list = find_loop(new_oper_list)
            if position == -1:
                return accum
        i -= 1


with open('input8.txt', 'r') as file_in:
    operation_list = read_file(file_in)

accum, position, positions_list = find_loop(operation_list)
print(f'accum = {accum}, position = {position}, pos_list = {positions_list}')
accum2 = find_corrupted(operation_list, positions_list)
print(f'accum2 = {accum2}')
