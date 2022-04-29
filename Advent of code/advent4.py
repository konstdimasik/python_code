passport_fieds = ('byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid')
ecl_variants = ('amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth')


def read_file(file):
    passport_list = []
    person = []
    for line in file:
        if line == '\n':
            passport_list.append(person)
            person = []
            continue
        sep = line.strip('\n').split(' ')
        person += sep
    passport_list.append(person)
    return passport_list


def passports_check(list):
    counter = 0
    for passport in list:
        if (passport_check_present(passport) == 7
                and passport_check_valid(passport) == 7):
            counter += 1
    return counter


def passport_check_present(passport):
    field_counter = 0
    for field in passport:
        if field.split(':')[0] in passport_fieds:
            field_counter += 1
    return field_counter


def passport_check_valid(passport):
    field_counter = 0
    for field in passport:
        field_name = field.split(':')[0]
        field_value = field.split(':')[1]
        if field_name == 'byr':
            if 1920 <= int(field_value) <= 2002:
                field_counter += 1
        elif field_name == 'iyr':
            if 2010 <= int(field_value) <= 2020:
                field_counter += 1
        elif field_name == 'eyr':
            if 2020 <= int(field_value) <= 2030:
                field_counter += 1
        elif field_name == 'hgt':
            if field_value_check_hgt(field_value):
                field_counter += 1
        elif field_name == 'hcl':
            if field_value_check_hlc(field_value):
                field_counter += 1
        elif field_name == 'ecl':
            if field_value in ecl_variants:
                field_counter += 1
        elif field_name == 'pid':
            if field_value.isdigit() and len(field_value) == 9:
                field_counter += 1
        elif field_name == 'cid':
            continue
        else:
            print(f'Wrong field_name: {field_name}')
    return field_counter


def field_value_check_hgt(field_value):
    height, measure = '', ''
    for letter in field_value:
        if letter.isdigit():
            height += letter
        else:
            measure += letter
    if measure == 'cm':
        if 150 <= int(height) <= 193:
            return True
    elif measure == 'in':
        if 59 <= int(height) <= 76:
            return True
    return False


def field_value_check_hlc(field_value):
    i = 0
    for letter in field_value:
        if i == 0 and letter == '#':
            i += 1
            continue
        if letter.isdigit() or ('a' <= letter <= 'f'):
            i += 1
    if i == 7:
        return True
    return False


with open('input4.txt', 'r') as file_in:
    passports_list = read_file(file_in)

print(passports_list)

print(f'valid passports counter = {passports_check(passports_list)}')
