from random import randint
from time import perf_counter


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


def main():
    test_arrays = create_arrays()
    print('partition            partition3')
    for i in range(3):
        for j in range(3):
            start = perf_counter()
            randomized_quicksort_partition(test_arrays[i][j])
            end = perf_counter()
            start3 = perf_counter()
            randomized_quicksort_partition3(test_arrays[i][j])
            end3 = perf_counter()
            print(end - start, end3 - start3)


if __name__ == '__main__':
    main()