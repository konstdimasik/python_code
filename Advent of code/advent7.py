def read_file(file):
    rule_dict = {}
    for line in file:
        color = ''
        i = 0
        line_list = line.strip('.\n').split(' ')
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
                    rule_dict[key_color] = value_color_in
                else:
                    rule_dict[key_color] = value_color
                color = ''
                continue
            color += word + ' '
    return rule_dict


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


with open('input7.txt', 'r') as file_in:
    rule_dict = read_file(file_in)

# for key, value in rule_dict.items():
#     print(f'{key}_________{value}')

print(shiny_count('shiny gold'))
