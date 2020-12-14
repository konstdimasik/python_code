def read_file(file):
    group_list = []
    group = []
    for line in file:
        if line == '\n':
            group_list.append(group)
            group = []
            continue
        sep = line.strip('\n')
        group += sep
    group_list.append(group)
    return group_list


def read_file2(file):
    group_list = []
    group = []
    for line in file:
        if line == '\n':
            group_list.append(group)
            group = []
            continue
        sep = line.strip('\n')
        group.append(sep)
    group_list.append(group)
    return group_list


def count_anyone_answers(list):
    answers = set()
    counter = 0
    for group in list:
        for answer in group:
            if answer not in answers:
                answers.add(answer)
        counter += len(answers)
        answers.clear()
    return counter


def sum_count_everyone_answers(list):
    counter = 0
    for group in list:
        counter += count_everyone_answers2(group)
    return counter


def count_everyone_answers2(group):
    answers = set(group[0])
    for i in range(1, len(group)):
        for letter in set(group[0]):
            if letter not in set(group[i]):
                answers.discard(letter)
    return len(answers)


with open('input6.txt', 'r') as file_in:
    group_list = read_file2(file_in)

print(group_list)

print(sum_count_everyone_answers(group_list))
