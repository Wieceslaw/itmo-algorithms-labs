from random import randint
from time import perf_counter


def generate_array(n, m, neg=True):
    a = []
    for _ in range(n):
        if neg:
            a.append(randint(-m, m))
        else:
            a.append(randint(1, m))
    return a


def partition(a):
    l = 0
    r = len(a)
    x = a[l]
    j = l
    for i in range(l + 1, r):
        if a[i] <= x:
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


def tester():
    n = 10 ** 5
    m = 10 ** 9
    a = generate_array(n, m)
    
    # the worst
    t_start = perf_counter()
    result = randomized_quick_sort(sorted(a, reverse=True))
    print('Время работы худшего случая: ' + str(perf_counter() - t_start) + ' секунд')
    if result == sorted(a):
        print('Успешно')

    # the best
    t_start = perf_counter()
    result = randomized_quick_sort(sorted(a))
    print('Время работы лучшего случая: ' + str(perf_counter() - t_start) + ' секунд')
    if result == sorted(a):
        print('Успешно')

    # avarage
    t_start = perf_counter()
    result = randomized_quick_sort(a)
    print('Время работы среднего случая: ' + str(perf_counter() - t_start) + ' секунд')
    if result == sorted(a):
        print('Успешно')


def main():
    tester()


if __name__ == '__main__':
    main()