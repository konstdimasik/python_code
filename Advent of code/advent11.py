import copy

def read_file(file):
    seat_matrix = []
    for line in file:
        line = line.strip('\n')
        new_line = []
        for letter in line:
            new_line.append(letter)
        seat_matrix.append(new_line)

    return seat_matrix


def print_matrix(matrix):
    for row in matrix:
        for each in row:
            print(each, end='')
        print()
    print()

def seating(seat_matrix):
    height = len(seat_matrix)
    weight = len(seat_matrix[0])
    new_seat_matrix = copy.deepcopy(seat_matrix)
    change = 0
    counter = 0
    for y in range(height):
        for x in range(weight):
            occupied_counter = near(seat_matrix, y, x)
            if seat_matrix[y][x] == 'L' and occupied_counter == 0:
                new_seat_matrix[y][x] = '#'
                change = 1
                counter += 1
            if seat_matrix[y][x] == '#' and occupied_counter >= 4:
                change = 1
                new_seat_matrix[y][x] = 'L'
            if seat_matrix[y][x] == '#' and occupied_counter < 4:
                counter += 1
    return new_seat_matrix, change, counter


def near(seat_matrix, y_p, x_p):
    height = len(seat_matrix)
    weight = len(seat_matrix[0])
    counter = 0
    for y in (y_p - 1, y_p, y_p + 1):
        for x in (x_p - 1, x_p,  x_p +1):
            if y < 0 or x < 0 or x >= weight or y >= height or (x == x_p and y == y_p):
                continue
            if seat_matrix[y][x] == '#':
                counter += 1
    return counter


def direction(seat_matrix, y_p, x_p):
    height = len(seat_matrix)
    weight = len(seat_matrix[0])
    counter = 0
    directions = [[-1, -1], [-1, 0], [-1, 1], [0, 1],
             [1, 1], [1, 0], [1, -1], [0, -1]]
    for dx, dy in directions:
        x = x_p + dx
        y = y_p + dy
        if y < 0 or x < 0 or x >= weight or y >= height:
            continue
        while seat_matrix[y][x] == '.':
            x += dx
            y += dy
            if y < 0 or x < 0 or x >= weight or y >= height or (x == x_p and y == y_p):
                x -= dx
                y -= dy
                break
        if seat_matrix[y][x] == '#':
                    counter += 1
    return counter


def seating2(seat_matrix):
    height = len(seat_matrix)
    weight = len(seat_matrix[0])
    new_seat_matrix = copy.deepcopy(seat_matrix)
    change = 0
    counter = 0
    for y in range(height):
        for x in range(weight):
            occupied_counter = direction(seat_matrix, y, x)
            if seat_matrix[y][x] == 'L' and occupied_counter == 0:
                new_seat_matrix[y][x] = '#'
                change = 1
                counter += 1
            if seat_matrix[y][x] == '#' and occupied_counter >= 5:
                change = 1
                new_seat_matrix[y][x] = 'L'
            if seat_matrix[y][x] == '#' and occupied_counter < 5:
                counter += 1
    return new_seat_matrix, change, counter


with open('input11.txt', 'r') as file_in:
        seat_matrix = read_file(file_in)

print_matrix(seat_matrix)
# print(len(seat_matrix))
# print(len(seat_matrix[0]))

change = 1
while change == 1:
    seat_matrix, change, counter = seating2(seat_matrix)
    # print_matrix(seat_matrix)
print_matrix(seat_matrix)
print(f'counter # = {counter}')
