n = int(input())
counter, steps = 1, 1
while steps <= n:
    for i in range(counter):
        if steps == n + 1:
            break
        print(counter, end=' ')
        steps += 1
    counter += 1
