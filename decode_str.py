with open('dataset_3363_2.txt') as file:
    str_in = file.readline()
    str_in = str_in.strip()
print(str_in)
tempalpha = ''
tempdigit = ''
switcher = 0
out_str = ''
for j in range(len(str_in)):
    if str_in[j].isalpha():
        if switcher == 1:
            for i in range(int(tempdigit)):
                out_str += tempalpha
            tempalpha = ''
            tempdigit = ''
        tempalpha += str_in[j]
        switcher = 0
    else:
        tempdigit += str_in[j]
        switcher = 1
        if j == len(str_in) - 1:
            for i in range(int(tempdigit)):
                out_str += tempalpha

with open('out.txt', 'w') as ouf:
    ouf.write(out_str)

# m, s, n = '', '', 0
# with open('dataset_3363_2.txt', 'r+') as f:     # открываем файл в режиме чтение и запись
#     for i in f.readline():                      # читаем строку и перебираем
#         if '0' <= i <= '9':                     # если число
#             n += i                              # соединяем числа в строку
#             continue
#         m += s * int(n)                         # преобразуем число в соответствующее количество символов
#         s, n = i, ''
#     f.seek(0)                                   # перемещаем указатель в начало файла для перезаписи
#     f.write(m)                                  # записываем преобразованную строку в файл
