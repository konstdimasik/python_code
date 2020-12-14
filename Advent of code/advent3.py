def read_file(file):
    list_slope = []
    for line in file:
        list_slope.append(line.strip('\n'))
    return list_slope


def slope_check(list, right, down):
    counter = 0
    x, y = 0, 0
    while y < len(list):
        if list[y][x] == '#':
            counter += 1
        x += right
        y += down
        if x >= len(list[0]):
            x = x - len(list[0])
    return counter


with open('input3.txt', 'r') as file_in:
    slope_list = read_file(file_in)

route_list = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]
multiply = 1
for route in route_list:
    tree_counter = slope_check(slope_list, route[0], route[1])
    # print(f'route {route} = {tree_counter}')
    multiply *= tree_counter

print(f'multiply = {multiply}')
