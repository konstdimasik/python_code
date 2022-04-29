dict_school = {}
with open('school_TVS_input.txt', 'r') as file:
    for line in file:
        str_in = line.strip().split('\t')
        if int(str_in[0]) not in dict_school:
            dict_school[int(str_in[0])] = [str_in[1:3]]
        else:
            dict_school[int(str_in[0])] += [str_in[1:3]]

for i in range(1, 12):
    aver_sum = 0.0
    if i not in dict_school:
        print(f'{i} -')
    else:
        for j in range(len(dict_school[i])):
            aver_sum += float(dict_school[i][j][1])
        print(f'{i} {aver_sum / len(dict_school[i])}')
