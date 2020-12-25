def read_file(file):
    rule_dict = {}
    for line in file:
        color = ''
        i = 0
        line_list = line.strip('.\n').split(' ')
        for word in line_list:
            word = word.strip(',').strip(' ')
            if word == 'contain':
                continue
            if word.isdigit():
                num = word
                continue
            if word == 'bags' or word == 'bag':
                if i == 0:
                    key_color = color.strip(' ')
                    color = ''
                    i += 1
                    continue
                value_color = [num] + [color.strip(' ')]
                if key_color in rule_dict:
                    value_color_in = value_color + rule_dict[key_color]
                    rule_dict[key_color] = value_color_in
                else:
                    rule_dict[key_color] = value_color
                color = ''
                num = '0'
                continue
            color += word + ' '
    return rule_dict


def shiny_count(bag_color):
    counter = 0
    for each_color in rule_dict[bag_color]:
        if each_color == '0':
            amount = '0'
            continue
        if each_color.isdigit():
            amount = each_color
            continue
        if each_color not in rule_dict:
            counter += int(amount)
        else:
            counter += int(amount) * (1 + shiny_count(each_color))
    return counter


with open('input7.txt', 'r') as file_in:
    rule_dict = read_file(file_in)

# for key, value in rule_dict.items():
#     print(f'{key}_________{value}')

print(shiny_count('shiny gold'))
