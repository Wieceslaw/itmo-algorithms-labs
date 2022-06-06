import time
from random import randint


def main():
    tester(swap, 55, 112)


def tester(func, n, m):
    a = generate_array(n, m)
    print('Алгоритм: ', str(func).split()[1])
    print(f'Исходный массив размером {n} c числами в пределах ({-m}, {m}):', *a)
    t_start = time.perf_counter()
    result = func(a)
    print('Время работы: ' + str(time.perf_counter() - t_start) + ' секунд')
    print("Результат:")
    print(*result)
    if result == sorted(a):
        print(f'Отсортировано успешно.')


def generate_array(n, m):
    a = []
    for _ in range(n):
        a.append(randint(-m, m))
    return a


# task №1
def insertion_sort(a):
    for j in range(1, len(a)):
        key = a[j]
        i = j - 1
        while i >= 0 and a[i] > key:
            a[i + 1] = a[i]
            i -= 1
        a[i + 1] = key
    return a


# task №2
def insertion_sort_plus(a):
    output = a.copy()
    for j in range(0, len(a)):
        key = a[j]
        i = j - 1
        while i >= 0 and a[i] > key:
            a[i + 1] = a[i]
            i -= 1
        a[i + 1] = key
        output[j] = i + 2
    return output, a


# task №3
def insertion_sort_reverse(a):
    for j in range(1, len(a)):
        key = a[j]
        i = j - 1
        while i >= 0 and a[i] > key:
            a[i + 1] = a[i]
            i -= 1
        a[i + 1] = key
    for i in range(len(a) // 2):
        key = a[i]
        a[i] = a[len(a) - i - 1]
        a[len(a) - i - 1] = key
    return a


# task №4
def linear_search(a, v):
    k = 0
    sp = []
    for i in range(len(a)):
        if a[i] == v:
            k += 1
            sp.append(i)
    if len(sp) > 1:
        return k, sp
    elif len(sp) == 1:
        return sp[0],
    else:
        return -1,


# task №5
def selection_sort(a):
    for j in range(len(a) - 1):
        min_i = len(a) - 1
        for i in range(j + 1, len(a)):
            if a[i] < a[min_i]:
                min_i = i
        if a[j] > a[min_i]:
            a[j], a[min_i] = a[min_i], a[j]
    return a


# task №6
def bubble_sort(a):
    for i in range(1, len(a)):
        for j in range(i, 0, -1):
            if a[j] < a[j - 1]:
                a[j], a[j - 1] = a[j - 1], a[j]
    return a


# task №7
def sortland(m):
    a = [(m[i], i) for i in range(len(m))]
    for i in range(1, len(a)):
        for j in range(i, 0, -1):
            if a[j][0] < a[j - 1][0]:
                a[j], a[j - 1] = a[j - 1], a[j]
    return [i + 1 for i in [a[0][1], a[len(a) // 2][1], a[-1][1]]]


# task №8
def swap(a):
    for j in range(len(a) - 1):
        min_i = len(a) - 1
        for i in range(j + 1, len(a)):
            if a[i] < a[min_i]:
                min_i = i
        if a[j] > a[min_i]:
            print(f'Swap elements at indices {j + 1} and {min_i + 1}')
            a[j], a[min_i] = a[min_i], a[j]
    return a


# task №9
def binary_sum(a, b):
    m = sum([a[::-1][i] * 2 ** i for i in range(len(a))])
    m += sum([b[::-1][i] * 2 ** i for i in range(len(b))])
    sp = []
    while m >= 1:
        sp.append(m % 2)
        m //= 2
    return sp[::-1]


# task №10
def palindrom(a):
    # ===============доделать================
    return a


if __name__ == '__main__':
    main()