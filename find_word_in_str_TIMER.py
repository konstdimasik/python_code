# Программа должна считывать одну строку со стандартного ввода и выводить
# для каждого уникального слова в этой строке число его повторений
# (без учёта регистра) в формате "слово количество" (см. пример вывода).
# Порядок вывода слов может быть произвольным, каждое уникальное
# слово﻿ должно выводиться только один раз.
import timeit
a = timeit.default_timer()

str_in = [i for i in input().split()]
d = {}
for word in str_in:
    word_l = word.lower()
    if word_l in d:
        d[word_l] += 1
    else:
        d[word_l] = 1

for key, value in d.items():
    print(key, value)

print(timeit.default_timer() - a)

a = timeit.default_timer()
s = input().lower().split()
for i in set(s):
    print(i, s.count(i))
print(timeit.default_timer() - a)
