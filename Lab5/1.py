from timing import timing


def input(file_name):
    with open(file_name, mode='rt') as file:
        result = [int(line.strip()) for line in file.readlines()]
    return result


@timing
def func(a):
    flag = True
    n = len(a)
    for i in range(n):
        if (2 * i + 1) < n:
            if a[i] > a[2 * i + 1]:
                flag = False
                break
        elif (2 * (i + 1)) < n:
            if a[i] > a[2 * (i + 1)]:
                flag = False
                break
    return flag


def main():
    array = input('input1.txt')
    # array = [1, 0, 1, 2, 0]
    # array = [1, 0, 1, 2, 0]
    result = func(array)
    if result:
        print('YES')
    else:
        print('NO')

if __name__ == '__main__':
    main()
