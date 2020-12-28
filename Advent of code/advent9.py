def read_file(file):
    num_list = []
    for line in file:
        number = int(line.strip('\n'))
        num_list.append(number)
    return num_list


def find_weakness(num_list):
    i = 25
    set_preamble = set()
    while i < len(num_list):
        counter = 0
        preamble = num_list[i-25:i]
        for each_num in preamble:
            set_preamble = set(preamble)
            set_preamble.discard(each_num)
            if num_list[i] - each_num in set_preamble:
                counter += 1
        if counter == 0:
            return num_list[i]
        set_preamble.clear()
        i += 1
    return 'List dont have weekness'


def find_sum(num_list, weak_num):
    weak_sum = []
    for i in range(len(num_list)):
        sum = 0
        j = i
        while sum <= weak_num:
            if sum == weak_num:
                return weak_sum
            sum += num_list[j]
            weak_sum.append(num_list[j])
            j += 1
        weak_sum = []
    return 'List dont have sum == weak_num'


with open('input9.txt', 'r') as file_in:
    num_list = read_file(file_in)

# print(num_list)
weak_num = find_weakness(num_list)
print(weak_num)
weak_sum = find_sum(num_list, weak_num)
print(weak_sum)
min_num = min(weak_sum)
max_num = max(weak_sum)
print(f'min_max_sum = {min_num + max_num}')
