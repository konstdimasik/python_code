place = [0,0]
for _ in range(int(input())):
    list_moves = input().split()
 #   print(list_moves)
    if list_moves[0] == 'север':
        place[1] += int(list_moves[1])
    elif list_moves[0] == 'восток':
        place[0] += int(list_moves[1])
    elif list_moves[0] == 'юг':
        place[1] += -int(list_moves[1])
    elif list_moves[0] == 'запад':
        place[0] += -int(list_moves[1])
#    print(list_moves[0],list_moves[1], place[0], place[1])
print(*place)

# dict = {'север': 0, 'юг': 0, 'запад': 0, 'восток': 0}
# for _ in range(int(input())):
#     key, value = input().split()
#     dict[key] += int(value)
# print(dict['восток'] - dict['запад'], dict['север'] - dict['юг'])
