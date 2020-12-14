def read_file(file):
    rule_dict = {}
    for line in file:
        color = ''
        i = 0
        line_list = line.strip('.\n').split(' ')
        # print(line_list)
        for word in line_list:
            word = word.strip(',').strip(' ')
            if word.isdigit() or word == 'contain':
                continue
            if word == 'bags' or word == 'bag':
                if i == 0:
                    value_color = [color.strip(' ')]
                    color = ''
                    i += 1
                    continue
                key_color = color.strip(' ')
                if key_color in rule_dict:
                    value_color_in = value_color + rule_dict[key_color]
                    # print(f'in dict {key_color}_{value_color_in}')
                    rule_dict[key_color] = value_color_in
                else:
                    rule_dict[key_color] = value_color
                    # print(f'not in dict {key_color}_{value_color}')
                color = ''
                continue
            color += word +' '
    return rule_dict


# def shiny_count(bag_color, set_color):
#     for each_color in rule_dict[bag_color]:
#         set_color.add(each_color)
#         if each_color in rule_dict:
#             shiny_count(each_color, set_color)
#     return

def shiny_count(bag_color):
    counter = 0
    for each_color in rule_dict[bag_color]:
        if each_color not in rule_dict:
            counter += 1
            print(f'color = {each_color}, counter = {counter}')
        else:
            counter += 1 + shiny_count(each_color)
            print(f'color = {each_color}, counter = {counter}')
    return counter


with open('input0.txt', 'r') as file_in:
    rule_dict = read_file(file_in)

for key, value in rule_dict.items():
    print(f'{key}_________{value}')

# set_color = set()
# shiny_count('shiny gold', set_color)
# print(len(set_color))

print(shiny_count('shiny gold'))
