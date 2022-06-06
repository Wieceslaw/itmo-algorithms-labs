from random import randint
from collections import deque
from time import perf_counter


def func(m, array):
    queue = deque(array)
    for _ in range(m):
        if len(queue) == 0:
            return -1
        el = queue.popleft() - 1
        if el > 0:
            queue.append(el)
    return queue


def generate_array(n):
    return [randint(1, 10 ** 6) for _ in range(n)]


def main():
    array = generate_array(10 ** 5)
    m = 10 ** 8

    # array = [1, 2, 3]
    # m = 2

    # array = [2, 5, 2, 3]
    # m = 5

    t_start = perf_counter()
    result = func(m, array)
    print('Время работы: ' + str(perf_counter() - t_start) + ' секунд')
    # print(*result)


if __name__ == '__main__':
    main()