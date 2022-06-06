from _1 import generate_array
from random import randint
from time import perf_counter


def partition(a):
    l = 0
    r = len(a)
    x = a[l][0]
    j = l
    for i in range(l + 1, r):
        if a[i][0] <= x:
            j += 1
            a[j], a[i] = a[i], a[j]
    a[l], a[j] = a[j], a[l]
    return a, j


def randomized_quick_sort(a):
    if len(a) > 1:
        k = randint(1, len(a) - 1)
        a[0], a[k] = a[k], a[0]
        a, j = partition(a)
        x = a[j]
        al = randomized_quick_sort(a[:j])
        ar = randomized_quick_sort(a[j + 1:])
        return al + [x] + ar
    return a


def distance(x, y):
    return (x ** 2 + y ** 2) ** 0.5


def nearest(a, k):
    distance_a = [(distance(x, y), f"[{x}, {y}]") for x, y in a]
    return randomized_quick_sort(distance_a)[:k]


def main():
    n = 10 ** 5
    m = 10 ** 9
    k = randint(0, n)
    a = list(zip(generate_array(n, m), generate_array(n, m)))
    t_start = perf_counter()
    result = nearest(a, k)
    print('Время работы: ' + str(perf_counter() - t_start) + ' секунд')
    # for _, el in result:
    #     print(el)


if __name__ == '__main__':
    main()