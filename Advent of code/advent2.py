def read_file(file):
    list_pass = []
    for line in file:
        first_sep = line.strip('\n').split(':')
        min = int(first_sep[0].split('-')[0])
        max = int(first_sep[0].split('-')[1].split(' ')[0])
        letter = first_sep[0].split('-')[1].split(' ')[1]
        passw = first_sep[1].strip()
        list_pass.append([min, max, letter, passw])
        # print(f'{line} {min}  {max}  {letter}  {passw}\n'
        #       f'{type(min)}  {type(max)}  {type(letter)}  {type(passw)}\n')
    return list_pass


def pass_check_1(list):
    counter = 0
    for row in list:
        i = 0
        for letter in row[3]:
            if letter == row[2]:
                i += 1
        if row[0] <= i <= row[1]:
            counter += 1
    return counter


def pass_check_2(list):
    counter = 0
    for row in list:
        i = 1
        check = 0
        for letter in row[3]:
            if (i == row[0] or i == row[1]) and letter == row[2]:
                check += 1
                # print(f'{row[3]}__{i}={row[0]}or{row[1]}__{letter}={row[2]}__{check}')
            i += 1
        if check == 1:
            counter += 1
            # print(f'__{check}__{counter}')
    return counter


with open('input2.txt', 'r') as file_in:
    pass_list = read_file(file_in)

print(pass_list[:10])

print(f'counter1 = {pass_check_1(pass_list)}')
print(f'counter2 = {pass_check_2(pass_list)}')
