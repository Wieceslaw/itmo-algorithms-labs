from time import perf_counter
from random import randint


def partition(a):
    x = a[0]
    j = 0
    for i in range(1, len(a)):
        if a[i] <= x:
            j += 1
            a[j], a[i] = a[i], a[j]
    a[0], a[j] = a[j], a[0]
    return a, j


def create_arrays():
    test_arrays = []
    for n in [10 ** 3, 10 ** 4, 10 ** 5]:
        test_arr1 = sorted([randint(10 ** 9, 10 ** 10 - 1) for i in range(n)], reverse=True)
        test_arr2 = sorted([randint(10 ** 9, 10 ** 10 - 1) for i in range(n)])
        test_arr3 = [randint(10 ** 9, 10 ** 10 - 1) for i in range(n)]
        test_arrays.append([test_arr1, test_arr2, test_arr3])
    return test_arrays


def randomized_quicksort_partition(a):
    if len(a) > 1:
        k = randint(1, len(a) - 1)
        a[0], a[k] = a[k], a[0]
        a, j = partition(a)
        l = randomized_quicksort_partition(a[:j])
        r = randomized_quicksort_partition(a[j+1:])
        return l + [a[j]] + r
    return a


def partition3(arr, pivot):
    less, equal, greater = [], [], []
    for val in arr:
        if val  < pivot: less.append(val)
        if val == pivot: equal.append(val)
        if val  > pivot: greater.append(val)
    return less, equal, greater


def randomized_quicksort_partition3(arr):
    if len(arr) <= 1: return arr
    less, equal, greater = partition3(arr, arr[randint(1, len(arr) - 1)])
    return randomized_quicksort_partition3(less) + equal + randomized_quicksort_partition3(greater)


def pugalo_sort(a, r):
    res = []
    sub_arrays = [[a[i] for i in range(j, len(a), + r)] for j in range(r)]
    for i in range(len(sub_arrays)):
        sub_arrays[i] = randomized_quicksort_partition3(sub_arrays[i])
    while len(res) != len(a):
        for i in range(len(sub_arrays)):
            if len(sub_arrays[i]) != 0:
                res.append(sub_arrays[i].pop(0))
    return res == sorted(a)


def main():
    k = 2
    array = [2, 1, 3]

    k = 3
    array = [1, 5, 3, 4, 1]

    t_start = perf_counter()
    print('ДА' if pugalo_sort(array, k) else 'НЕТ')
    print('Время работы: ' + str(perf_counter() - t_start) + ' секунд')


if __name__ == '__main__':
    main()