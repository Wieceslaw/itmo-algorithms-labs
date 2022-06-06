def input(filename):
    with open(filename, mode='rt') as file:
        result = [line.strip() for line in file.readlines()]
    return result


def func(A, B):
    sl = {}
    for j in range(len(B)):
        for i in range(len(A)):
            if A[i] == '*':
                sl[(i, j)] = 2
            elif A[i] == B[j] or A[i] == '?':
                sl[(i, j)] = 1
            else:
                sl[(i, j)] = 0

    def f(A, B, i, j):
        if i == j == -1:
            return 1
        elif i == -1 or j == -1:
            return 0
        elif sl[(i, j)] == 1:
            return f(A, B, i - 1, j - 1)
        elif sl[(i, j)] == 2:
            return f(A, B, i - 1, j - 1) or \
                   f(A, B, i, j - 1) or \
                   f(A, B, i - 1, j)
        else:
            return 0

    return f(A, B, len(A) - 1, len(B) - 1)


def main():
    word1, word2 = input('input.txt')
    result = func(word1, word2)
    with open('output.txt', mode='wt') as file:
        if result:
            file.write('YES')
        else:
            file.write('NO')
    # print(word1)
    # print(word2)
    # if result:
    #     print('YES')
    # else:
    #     print('NO')


if __name__ == '__main__':
    main()