size = 5
l = [[0] * size for i in range(size)]

print(l)
l[0][0] = -1
print(l)
# lambda x: x > 1 and x < 4
# def shiny_count(bag_color, set_color):
#     for each_color in rule_dict[bag_color]:
#         set_color.add(each_color)
#         if each_color in rule_dict:
#             shiny_count(each_color, set_color)
#     return


def cache_args(func):
    cache = dict()

    def caching(*args):
        if args in cache:
            return cache[args]
        else:
            cache[args] = func(*args)
            return cache[args]

    return caching


@cache_args
def long_heavy(num):
    print(f"Долго и сложно {num}")
    return num**num


print(long_heavy(1))
# Долго и сложно 1
# 1
print(long_heavy(1))
# 1
print(long_heavy(2))
# Долго и сложно 2
# 4
print(long_heavy(2))
# 4
print(long_heavy(2))
# 4


###################

def cache3(func):
    cache = {'func': func(), 'count': 0}

    def decorator():
        if cache['count'] < 3:
            cache['count'] += 1
            return cache['func']
        cache['count'] = 1
        return func()

    return decorator


@cache3
def heavy():
    print('Сложные вычисления')
    return 1


print(heavy())
# Сложные вычисления
# 1
print(heavy())
# 1
print(heavy())
# 1

# Опять кеш устарел, надо вычислять заново
print(heavy())
# Сложные вычисления
# 1
