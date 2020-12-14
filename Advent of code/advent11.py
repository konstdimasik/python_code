def read_file(file):
    seat_matrix = []
    for line in file:
        line = line.strip('\n')
        new_line = []
        for letter in line:
            new_line.append(letter)
        seat_matrix.append(new_line)

    return seat_matrix


def seating(seat_matrix):
    weight = len(seat_matrix[0])
    hight = len(seat_matrix)
    new_seat_matrix = [[]]
    for y in range(hight):
        for x in range(weight):
            if seat_matrix[y][x] == '.':
                new_seat_matrix[y][x] = seat_matrix[y][x]
                continue
            if seat_matrix[y][x] == 'L':
                new_seat_matrix[y][x] = empty(seat_matrix,y, x)
            if seat_matrix[y][x] == '#':
                new_seat_matrix[y][x] = occupied(y, x)


def empty(seat_matrix, y, x):
    weight = len(seat_matrix[0])
    hight = len(seat_matrix)
    





with open('input11_0.txt', 'r') as file_in:
        seat_matrix = read_file(file_in)

print(seat_matrix)
