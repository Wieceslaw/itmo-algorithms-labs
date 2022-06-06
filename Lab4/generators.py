from random import randint


def generate_3(file_name, flag):
    n = 500
    m = 10 ** 4
    if flag:
        results = [''.join([['[]', '()'][randint(0, 1)] for _ in range(m // 2)]) + '\n' for _ in range(n)]
    if not flag:
        results = [''.join(['()[]'[randint(0, 3)] for _ in range(m)]) + '\n' for _ in range(n)]
    with open(file_name, mode='wt') as file:
        file.writelines(results)


def generate_9(file_name):
    results = []
    n = 10 ** 5
    k = 0
    array = []
    i = 1
    for _ in range(n):
        if k == 0:
            results.append([f'+ {i}', f'* {i}'][randint(0, 1)] + '\n')
            k += 1
            i += 1
        else:
            results.append([f'+ {i}', f'* {i}', '-'][randint(0, 2)] + '\n')
            k -= 1
    with open(file_name, mode='wt') as file:
        file.writelines(results)


def main():
    # generate_3('input3_false.txt', False)
    # generate_3('input3_true.txt', True)
    generate_9('input9.txt')


if __name__ == '__main__':
    main()