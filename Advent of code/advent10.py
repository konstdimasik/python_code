def read_file(file):
    num_list = []
    for line in file:
        number = int(line.strip('\n'))
        num_list.append(number)
    return num_list


def qsort(arr):
    if len(arr) <= 1:
        return arr
    else:
        return qsort([x for x in arr[1:] if x < arr[0]]) + \
               [arr[0]] + \
               qsort([x for x in arr[1:] if x >= arr[0]])


def find_jolt(num_list):
    i = 0
    jolt = 0
    jolt1 = 0
    jolt2 = 0
    jolt3 = 0
    for i in range(len(num_list)):
        if num_list[i] - jolt == 1:
            jolt1 += 1
            jolt = num_list[i]
        if num_list[i] - jolt == 2:
            jolt2 += 1
            jolt = num_list[i]
        if num_list[i] - jolt == 3:
            jolt3 += 1
            jolt = num_list[i]
        if num_list[i] - jolt > 3:
            return f'Wrong jolt adapter {num_list[i]}'
    return jolt1, jolt3


def find_ways(min, num_list, max, check_list):
    counter = 0

    for i in range(min, max):
        print(f'i = {i}, num_list[i] = {num_list[i]}, num_list[max-1] = {num_list[max-1]}, check_list = {check_list}')
        if num_list[i] == num_list[max - 1]:

            counter += 1
            break
        if num_list[i] + 1 in num_list:
            check_list.append(num_list[i] + 1)
            print(f'i = {i}, num_list[i] + 1 = {num_list[i] + 1}, check_list = {check_list}')
            start = num_list.index(num_list[i] + 1)
            counter += find_ways(start, num_list, max, check_list)
        elif num_list[i] + 2 in num_list:
            check_list.append(num_list[i] + 2)
            print(f'i = {i}, num_list[i] + 2 = {num_list[i] + 2}, check_list = {check_list}')
            start = num_list.index(num_list[i] + 2)
            counter += find_ways(start, num_list, max, check_list)
        elif num_list[i] + 3 in num_list:
            check_list.append(num_list[i] + 3)
            print(f'i = {i}, num_list[i] + 3  = {num_list[i] + 3 }, check_list = {check_list}')
            start = num_list.index(num_list[i] + 3)
            counter += find_ways(start, num_list, max, check_list)
        else:
            break
    return counter


with open('input10_00.txt', 'r') as file_in:
    num_list = read_file(file_in)

print(num_list)
num_list = qsort(num_list)
max = max(num_list)
num_list.append(max+3)
print(num_list)
jolt1, jolt3 = find_jolt(num_list)
mult = jolt1 * jolt3
print(f'mult = {mult}')
check_list = []
counter = find_ways(0, num_list, len(num_list), check_list)
print(f'counter = {counter}')
