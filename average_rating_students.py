dict_students = {}
average_sum_math = 0.0
average_sum_phy = 0.0
average_sum_rus = 0.0
counter_stud = 0
with open('dataset_3363_4.txt', 'r') as file_in:
    for line in file_in:
        str_in = line.strip().split(';')
        dict_students[str_in[0]] = [int(str_in[1]), int(str_in[2]), int(str_in[3])]
# print(dict_students)

with open('out.txt', 'w') as file_res:
    for student in dict_students:
        average_sum_stud = 0.0
        quantity = len(dict_students[student])
        for i in range(quantity):
            average_sum_stud += dict_students[student][i] / quantity
        file_res.write(f'{average_sum_stud}\n')
        average_sum_math += dict_students[student][0]
        average_sum_phy += dict_students[student][1]
        average_sum_rus += dict_students[student][2]
        counter_stud += 1
    file_res.write(f'{average_sum_math / counter_stud} {average_sum_phy / counter_stud} {average_sum_rus / counter_stud}')
