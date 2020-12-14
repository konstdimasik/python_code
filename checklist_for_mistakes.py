right_words, mistakes = set(), set()
n = int(input())
for _ in range(n):
    right_words.add(input().lower())
m = int(input())
for _ in range(m):
    words = input().lower().split()
    for word in words:
        if word not in right_words:
            mistakes.add(word)
print(*mistakes, sep='\n')


# dic = {input().lower() for i in range(int(input()))}
#
# wrd = set()
# for w in range(int(input())):
#     wrd |= {i.lower() for i in input().split()}
#
# print(*wrd.difference(dic), sep="\n")
