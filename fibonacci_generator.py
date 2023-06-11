def fibonacci(n):
    if n == 1:
        yield 0
    elif n == 2:
        counter = 0
        while counter < n:
            yield counter
            counter += 1
    else:
        first = 0
        second = 1
        counter = 0
        while counter < n:
            if counter == 0:
                yield 0
                counter += 1
            elif counter == 1:
                yield 1
                counter += 1
            else:
                next = first + second
                yield next
                first = second
                second = next
                counter += 1
#                 
# def fibonacci(n, a=0, b=1):
#     for _ in range(n):
#         yield a
#         a, b = b, a + b

n = int(input('n?'))
i = 0
gen = fibonacci(n)
while i < n:
    print(next(gen))
    i += 1