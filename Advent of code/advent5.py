def read_file(file):
    seat_list = []
    for line in file:
        seat_list.append(line.strip('\n'))
    return seat_list


def decode(str):
    row, row_f, row_b = 0, 0, 127
    column, column_l, column_r = 0, 0, 7
    i = 0
    for letter in str:
        if i <= 6:
            if letter == 'F':
                row_b -= (row_b - row_f) // 2 + 1
                i += 1
            elif letter == 'B':
                row_f = row_f + (row_b - row_f) // 2 + 1
                i += 1
            else:
                print(f'Wrong letter "{letter}" in seat code')
            if i == 7:
                row = row_f
        else:
            if letter == 'L':
                column_r -= (column_r - column_l) // 2 + 1
                i += 1
            elif letter == 'R':
                column_l = column_l + (column_r - column_l) // 2 + 1
                i += 1
            else:
                print('Wrong letter in seat code')
            if i == 10:
                column = column_l
                # print(f'letter = {letter}, i = {i}, column = {column}')
        # print(f'"{letter}" {row_f} - {row_b}, {column_l} - {column_r}')
    return row, column


def max_seat_id(seat_list):
    max = 0
    for seat in seat_list:
        row, column = decode(seat)
        seat_id = row * 8 + column
        if seat_id > max:
            max = seat_id
    return max


def make_seat_id_list(seat_list):
    seat_id_list = []
    for seat in seat_list:
        row, column = decode(seat)
        seat_id = row * 8 + column
        seat_id_list.append(seat_id)
    return seat_id_list


def qsort(arr):
    if len(arr) <= 1:
        return arr
    else:
        return qsort([x for x in arr[1:] if x < arr[0]]) + \
               [arr[0]] + \
               qsort([x for x in arr[1:] if x >= arr[0]])


with open('input5.txt', 'r') as file_in:
    seat_list = read_file(file_in)

print(max_seat_id(seat_list))

seat_id_list = make_seat_id_list(seat_list)
seat_id_list_sorted = qsort(seat_id_list)
print(seat_id_list_sorted)

for x in range(seat_id_list_sorted[-1]):
    if ((x not in seat_id_list_sorted) and
       ((x-1) in seat_id_list_sorted) and
       ((x+1) in seat_id_list_sorted)):
        print(x)
