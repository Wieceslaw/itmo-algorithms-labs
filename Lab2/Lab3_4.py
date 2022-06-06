from generate_array import generate_array


def binary_search(a, l, h, v):
    if len(a[l: h]) > 1:
        md = l + (h - l) // 2
        if v == a[md]:
            return md
        elif v > a[md]:
            return binary_search(a, md, h, v)
        else:
            return binary_search(a, l, md, v)
    if len(a[l: h]) == 1:
        return l if a[l] == v else -1 
    return -1


def main():
    a = sorted(generate_array(10, 100, neg=False))
    b = generate_array(10, 100, neg=False)
    # a = [1, 5, 8, 12, 13]
    # b = [8, 1, 23, 1, 11]
    print('Исходный массив:', *a)
    print('Массив с числами для поиска:', *b)
    for el in b:
        print(binary_search(a, 0, len(a), el), end=' ')


if __name__ == '__main__':
    main()