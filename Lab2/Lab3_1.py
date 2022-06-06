from random import randint
from time import perf_counter


def merge(L, R):
    ans = []
    for _ in range(len(L) + len(R)):
        if len(L) > 0 and len(R) > 0:
            if L[0] < R[0]:
                ans.append(L.pop(0))
            else:
                ans.append(R.pop(0))
        elif len(L) > 0:
            ans.append(L.pop(0))
        elif len(R) > 0:
            ans.append(R.pop(0))
    return ans


def merge_sort(a):
    if len(a) > 1:
        return merge(merge_sort(a[:len(a) // 2]), merge_sort(a[len(a) // 2:]))
    else:
        return a


def main():
    tester(merge_sort, 1000, 10 ** 9)


def tester(func, n, m):
    a = sorted(generate_array(n, m), reverse=True)
    print('Алгоритм: ', str(func).split()[1])
    print(f'Исходный массив размером {n} c числами в пределах ({-m}, {m}):')
    t_start = perf_counter()
    result = func(a)
    print('Время работы: ' + str(perf_counter() - t_start) + ' секунд')
    if result == sorted(a):
        print(f'Отсортировано успешно.')


def generate_array(n, m):
    a = []
    for _ in range(n):
        a.append(randint(-m, m))
    return a


if __name__ == '__main__':
    main()