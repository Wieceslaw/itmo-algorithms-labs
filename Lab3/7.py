from time import perf_counter


def radix_sort(a, k):
    a = a[::-1]
    pos = [i for i in range(len(a[0]))]
    for i in range(k):
        line = ''.join([a[i][j] for j in pos])
        char_dict = {chr(chr_i): [] for chr_i in range(97, 123)}
        for i, el in enumerate(line):
            char_dict[el].append(pos[i])
        pos = []
        for el in char_dict.values():
            pos += el
    return list(map(lambda x: x + 1, pos))

 
def main():
    # example = [
    #     'bab',
    #     'bba',
    #     'baa'
    # ]
    t_start = perf_counter()
    with open('1.txt', 'r') as file:
        array = [line.strip() for line in file.readlines()]
    k = 1
    result = radix_sort(array, k)
    print('Время работы: ' + str(perf_counter() - t_start) + ' секунд')  
    print('Result:', result)


if __name__ == '__main__':
    main()