from collections import deque
from timing import timing


def input(filename):
    with open(filename, mode='rt') as file:
        result = [list(map(int, i.strip().split())) for i in file.readlines()]
    return result


@timing
def func(array):
    s, n = array[0]
    array = deque([(array[i][0], array[i][1], i - 1)\
     for i in range(1, n + 1)])
    queue = deque([array.popleft() for _ in range(s)])
    t = 0
    res = [0 for _ in range(n)]
    while bool(queue):
        a, p, i = queue.popleft()
        t = max(a, t)
        res[i] = t
        t += p
        if bool(array):
            new_el = array.popleft()
            while new_el[0] < t:
                res[new_el[-1]] = -1
                if bool(array):
                    new_el = array.popleft()
                else:
                    break
            if new_el[0] >= t:
                queue.append(new_el)
    return res


def main():
    array = input('input3.txt')
    result = func(array)
    print(result)


if __name__ == '__main__':
    main()