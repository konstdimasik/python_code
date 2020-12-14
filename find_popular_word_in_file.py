import timeit
a = timeit.default_timer()

dict_words = {}
max_n = 0
set_max = set()
with open('dataset_3363_3.txt', 'r') as file:
    list_words = file.read().lower().strip().split()
# print(list_words)

for word in list_words:
    if word in dict_words:
        dict_words[word] += 1
    else:
        dict_words[word] = 1
# print(dict_words)

for word, n in dict_words.items():
    if n > max_n:
        set_max.clear()
        set_max.add(word)
        max_n = n
    elif n == max_n:
        set_max.add(word)

word_min_of_max = 'z'
for word in set_max:
    if word < word_min_of_max:
        word_min_of_max = word
print(word_min_of_max, max_n)

print(timeit.default_timer() - a)

# str_in = ''
# with open('dataset_3363_3.txt') as file:
#     for line in file:
#         str_in += line.strip().lower()
#
# list_words = str_in.split()
# dict_words = {}
# for word in list_words:
#     if word in dict_words:
#         dict_words[word] += 1
#     else:
#         dict_words[word] = 1
# print(len(dict_words))
#
# max_n = 0
# set_max = set()
# for word, n in dict_words.items():
#     if n > max_n:
#         set_max.clear()
#         set_max.add(word)
#         max_n = n
#     elif n == max_n:
#         set_max.add(word)
#
# word_min = 'z'
# for word in set_max:
#     if word < word_min:
#         word_min = word
#
# print(word_min, max_n)
