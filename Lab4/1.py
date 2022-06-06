from random import randint
from time import perf_counter


def func(commands):
    stack = []
    result = []
    for command in commands:
        if command == '-' and len(stack) > 0:
            result.append(stack.pop())
        elif command.split()[0] == '+':
            stack.append(command.split()[1])
    return result


def generate_input(m):
    return ['+ ' + str(randint(-10000, 10000)) if randint(0, 1) == 0 else '-' for _ in range(m)]


def main():
    array = generate_input(10 ** 6)
    # array = ['+ 1', '+ 10', '-', '+ 2', '+ 1234', '-']
    t_start = perf_counter()
    func(array)
    print('Время работы: ' + str(perf_counter() - t_start) + ' секунд')
    # for el in func(array):
    #     print(el)


if __name__ == '__main__':
    main()