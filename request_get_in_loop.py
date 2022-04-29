# Имеется набор файлов, каждый из которых, кроме последнего, содержит
# имя следующего файла. Первое слово в тексте последнего файла: "We".
# Скачайте предложенный файл.
# В нём содержится ссылка на первый файл из этого набора.
# Все файлы располагаются в каталоге по адресу:
# https://stepic.org/media/attachments/course67/3.6.3/
# Загрузите содержимое ﻿последнего файла из набора, как ответ на это задание.

import requests

with open('dataset_3378_3.txt', 'r') as file_in:
    url = file_in.read().strip()
while True:
    r = requests.get(url)
    text_in = r.text
    first_word = text_in.split()[0]
    if first_word == 'We':
        break
    url = 'https://stepic.org/media/attachments/course67/3.6.3/' + text_in

print(text_in)
