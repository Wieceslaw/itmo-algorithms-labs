from random import randint
from math import ceil


def generate1(filename):
    result = [1]
    n = 10 ** 6
    for i in range(1, n):
        parent = result[ceil(i / 2 - 1)]
        if randint(0, 1):
            result.append(parent)
        else:
            result.append(parent + randint(1, 50))

    with open(filename, mode='wt') as file:
        file.writelines([str(i) + '\n' for i in result])


def generate5(filename):
    result = [[10 ** 2, 10 ** 5], [randint(0, 10 ** 9) for _ in range(10 ** 5)]]
    with open(filename, mode='wt') as file:
        file.writelines([' '.join([str(i) for i in el]) + '\n' for el in result])


def main():
    # generate1('input1.txt')
    generate5('input52.txt')


if __name__ == '__main__':
    main()