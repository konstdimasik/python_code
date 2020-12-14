str_code, str_decode, str_in1, str_in2 = (input() for i in range(4))

dict_code = dict(zip(str_code, str_decode))
dict_decode = dict(zip(str_decode, str_code))

for i in str_in1:
    print(dict_code[i], end='')
print()
for i in str_in2:
    print(dict_decode[i], end='')

# key, code, encode, decode = ( input() for _ in range(4) )
# print(*[ code[key.index(c)] for c in encode ], sep='')
# print(*[ key[code.index(c)] for c in decode ], sep='')

# a,b,c,d=input(),input(),input(),input()
# print(''.join(b[a.index(i)] for i in c))
# print(''.join(a[b.index(i)] for i in d))

# my first variant
# dict_code = {}
# dict_decode = {}
# str_code = input()
# str_decode = input()
# for i in range(len(str_code)):
#     dict_code[str_code[i]] = str_decode[i]
#     dict_decode[str_decode[i]] = str_code[i]
#
# str_in1 = input()
# str_in2 = input()
#
# for i in str_in1:
#     print(dict_code[i], end='')
# print()
# for i in str_in2:
#     print(dict_decode[i], end='')
