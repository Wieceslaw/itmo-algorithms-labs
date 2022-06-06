from _1 import randomized_quick_sort, generate_array
from time import perf_counter


def h_index(a):
    a = randomized_quick_sort(a)[::-1]
    for i, el in enumerate(a):
        if el <= i + 1:
            break
    return min(el, i + 1)


def main():
    n = 5000
    citations = 1000
    a = generate_array(n, citations, neg=False)
    t_start = perf_counter()
    result = h_index(a)
    print('Время работы: ' + str(perf_counter() - t_start) + ' секунд')
    print(result)


if __name__ == '__main__':
    main()