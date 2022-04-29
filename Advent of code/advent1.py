def qsort(arr):
    if len(arr) <= 1:
        return arr
    else:
        return qsort([x for x in arr[1:] if x < arr[0]]) + \
            [arr[0]] + \
            qsort([x for x in arr[1:] if x >= arr[0]])


list_input = []
with open('input1.txt', 'r') as file_in:
    for line in file_in:
        list_input.append(int(line))

list_sort = qsort(list_input)

i, j, k = 0, 1, 2
while i < len(list_sort):
    for j in range(i, len(list_sort)):
        for k in range(j, len(list_sort)):
            if list_sort[i] + list_sort[j] + list_sort[k] == 2020:
                print(f'sum = {list_sort[i] + list_sort[j] + list_sort[k]}\n'
                      f'mul = {list_sort[i] * list_sort[j] * list_sort[k]}\n')
            if list_sort[i] + list_sort[j] + list_sort[k] > 2020:
                break
            k += 1
        j += 1
    i += 1
