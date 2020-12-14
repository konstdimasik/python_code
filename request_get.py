# прочитали урл в файле, обратились по адресу, скачали текст,
# сделали построчный список и вывели его длину( посчитали кол-во строк)
import requests

with open('dataset_3378_2.txt','r') as file_in:
    url = file_in.read().strip()
print(url)
r = requests.get(url)
text_in = r.text
print(text_in)
print('_______________')
sum_line = (text_in.strip().split())
print(sum_line)
print(len(sum_line))
