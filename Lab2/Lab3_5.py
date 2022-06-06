from random import randint, shuffle
from time import perf_counter
from generate_array import generate_array


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
    a = generate_array(9, 100)
    a += [-100] * 10
    shuffle(a)
    print('Исходный массив: ', *a)
    result = merge_sort(a)
    central_el = result[round(len(result) // 2)]
    count = 0
    for el in result:
        if el == central_el:
            count += 1
    if count > (len(result) / 2):
        print(1)
    else:
        print(0)


if __name__ == '__main__':
    main()