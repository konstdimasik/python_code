from urllib.request import urlopen

from bs4 import BeautifulSoup

contents = urlopen("https://stepik.org/media/attachments/lesson/209719/2.html").read().decode('utf-8')

soup = BeautifulSoup(contents, 'lxml')
tags = soup.find_all(['code', 'p'])
code_list = []
for tag in tags:
    code_list.append(tag.text)

code_dict = dict()
i = 1
max_code = []
for code in code_list:
    if code in code_dict:
        code_dict[code] += 1
        if code_dict[code] == i:
            max_code.append(code)
        elif code_dict[code] > i:
            i = code_dict[code]
            max_code = [code]
    else:
        code_dict[code] = 1
print(max_code)
