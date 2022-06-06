from _1 import randomized_quick_sort, generate_array
from time import perf_counter
from random import shuffle


def anti_quick_sort(n):
    if n == 1:
        return [1]
    
    a = [0] * n
    a[0] = 2
    a[1] = 1

    for i in range(2, n):
        a[i] = i + 1
        a[i // 2], a[i] = a[i], a[i // 2]
    return a


def qsort (left, right):
    key = a [(left + right) // 2]
    i = left
    j = right
    while i <= j:
        while a[i] < key: # first while
            i += 1
        while a[j] > key : # second while
            j -= 1
        if i <= j :
            a[i], a[j] = a[j], a[i]
        i += 1
        j -= 1

    if left < j:
        qsort(left, j)
    if i < right:
        qsort(i, right)


def main():
    global a
    n = 10 ** 5
    a = sorted([i for i in range(n)], reverse=True)
    shuffle(a)
    # the worst
    t_start = perf_counter()
    qsort(0, n - 1)
    print('Время работы худшего случая: ' + str(perf_counter() - t_start) + ' секунд')
    if a == sorted(a):
        print('Успешно')
    # our
    a = anti_quick_sort(n)
    # print(a)
    t_start = perf_counter()
    qsort(0, n - 1)
    print('Время работы anti quick sort: ' + str(perf_counter() - t_start) + ' секунд')
    if a == sorted(a):
        print('Успешно')


if __name__ == '__main__':
    main()