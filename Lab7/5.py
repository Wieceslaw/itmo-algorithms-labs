sl = {}

def lcs(a, b, c, i, j, k):
    if (i, j, k) in sl:
        res = sl[(i, j, k)]
    elif i == -1 or j == -1 or k == -1:
        res = 0
    elif a[i] == b[j] == c[k]:
        res = lcs(a, b, c, i - 1, j - 1, k - 1) + 1
    else:
        res = max(
            lcs(a, b, c, i - 1, j, k),
            lcs(a, b, c, i, j - 1, k), 
            lcs(a, b, c, i, j, k - 1))
    sl[i, j, k] = res
    return res


def input(filename):
    with open(filename, mode='rt') as file:
        result = [list(map(int, line.strip().split())) 
        for line in file.readlines()]
    return result


def main():
    _, a, _, b, _, c = input('input.txt')
    result = lcs(a, b, c, len(a) - 1, len(b) -1, len(c) - 1)
    with open('output.txt', mode='wt') as file:
        file.write(str(result))
    # print(a, b, c)
    # print(result)


if __name__ == "__main__":
    main()


