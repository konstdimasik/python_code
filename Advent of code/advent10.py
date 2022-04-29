import time

global cache

caсhe = {}


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


def find_ways(min, num_list, max):
    counter = 0
    if num_list[min] == num_list[max - 1]:
        counter += 1
    if min in caсhe:
        return caсhe[min]
    else:
        if num_list[min] + 1 in num_list:
            start = num_list.index(num_list[min] + 1)
            counter += find_ways(start, num_list, max)
        if num_list[min] + 2 in num_list:
            start = num_list.index(num_list[min] + 2)
            counter += find_ways(start, num_list, max)
        if num_list[min] + 3 in num_list:
            start = num_list.index(num_list[min] + 3)
            counter += find_ways(start, num_list, max)
        caсhe[min] = counter
        return counter


with open('input10.txt', 'r') as file_in:
    num_list = read_file(file_in)

num_list.append(0)
max = max(num_list)
num_list.append(max + 3)
print(num_list)
num_list = qsort(num_list)
print(num_list)

jolt1, jolt3 = find_jolt(num_list)
mult = jolt1 * jolt3
print(f'mult = {mult}')
arrangment_list = []
t0 = time.time()
counter = find_ways(0, tuple(num_list), len(num_list))
t1 = time.time()
print("Time elapsed: ", t1 - t0)
print(f'counter = {counter}')
