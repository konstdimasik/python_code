def modify_list(l):
    for i in range(len(l)-1, -1, -1):
        if l[i] % 2 == 1:
            l.remove(l[i])
        else:
            l[i] = l[i] // 2

lst = [1, 2, 3, 4, 5, 6]
print(modify_list(lst))  # None
print(lst)               # [1, 2, 3]
modify_list(lst)
print(lst)
