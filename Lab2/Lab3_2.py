from random import randint
from time import perf_counter


def merge(a, p, q, r):
    L = []
    R = []
    for i in range(p, q):
        L.append(a[i])
    for j in range(q, r):
        R.append(a[j])
    for i in range(len(L) + len(R)):
        if len(L) > 0 and len(R) > 0:
            if L[0] < R[0]:
                a[p + i] = (L.pop(0))
            else:
                a[p + i] = (R.pop(0))
        elif len(L) > 0:
            a[p + i] = (L.pop(0))
        elif len(R) > 0:
            a[p + i] = (R.pop(0))
    print(p + 1, r, a[p], a[r - 1])


def merge_sort(a, p, r):
    if p < r and r - p > 1:
        q = (p + r) // 2
        merge_sort(a, p, q)
        merge_sort(a, q, r)
        merge(a, p, q, r)


def main():
    a = generate_array(10, 100)
    print("Исходный массив:", *a)
    t_start = perf_counter()
    merge_sort(a, 0, len(a))
    print('Время работы: ' + str(perf_counter() - t_start) + ' секунд')
    print(*a)


def generate_array(n, m):
    a = []
    for _ in range(n):
        a.append(randint(-m, m))
    return a


if __name__ == '__main__':
    main()