from time import perf_counter

def radix_sort(a, n, f):
    c = [0] * 27
    b = [0] * (n + 1)

    for i in range(1, n + 1):
        c[a[i][f]] += 1
    
    for i in range(1, 27):
        c[i] += c[i - 1]

    for i in range(n, 0, -1):
        b[c[a[i][f]]] = a[i]
        c[a[i][f]] -= 1
    return b


def transpose(matrix):
    rows = len(matrix)
    columns = len(matrix[0])

    matrix_T = []
    for j in range(columns):
        row = []
        for i in range(rows):
           row.append(matrix[i][j])
        matrix_T.append(row)

    return matrix_T


def main():
    k = 10 ** 6 # sort iterations
    m = 50 # length of strings
    n = 10 ** 6 # number of strings
    file_name = 'lines.txt'
    t_start = perf_counter()
    array = [0] + transpose([[i + 1 for i in range(m)]] + [[ord(s) - 96 for s in line.strip()] for line in open(file_name, 'r').readlines()])
    print(len(array))
    print('Время получения массива: ' + str(perf_counter() - t_start) + ' секунд') 

    for i in range(1, k + 1):
        array = radix_sort(array, m, n - i + 1)[::]

    # for i in range(1, n + 1):
    #     print(array[i][0])
    print('Время алгоритма: ' + str(perf_counter() - t_start) + ' секунд') 


if __name__ == '__main__':
    main()