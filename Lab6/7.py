def func(line, stones):
    sl = {}
    for i, el in enumerate(line):
        if el in sl:
            sl[el].append(i)
        else:
            sl[el] = [i]
    count = 0
    for stone in stones:
        for stone0 in sl[stone[0]]:
            for stone1 in sl[stone[1]]:
                if stone0 < stone1:
                    count += 1
    return count


n, k = map(int, input().split())
line = input()
stones = [input() for _ in range(k)]
result = func(line, stones)
print(result)