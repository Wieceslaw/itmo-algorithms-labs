from random import randint
from time import perf_counter


def generate_commands(m):
    result = []
    for _ in range(m):
        a = randint(1, 3)
        if a == 1:
            result.append('max')
        if a == 2:
            result.append('pop')
        if a == 3:
            result.append('push %d' % randint(0, 10 ** 5))
    return result


class Stack:
    def __init__(self):
        self.maxes = []
        self.elements = []
    
    def push(self, n):
        if len(self.maxes) == 0:
            self.maxes.append(n)
        elif len(self.maxes) > 0:
            if n > self.maxes[-1]:
                self.maxes.append(n)
            else:
                self.maxes.append(self.maxes[-1])
        self.elements.append(n)

    def pop(self):
        if len(self.elements) > 0:
            self.maxes.pop()
            return self.elements.pop()

    def max(self):
        if len(self.maxes) > 0:
            return self.maxes[-1]


def main():
    commands = generate_commands(4 * 10 ** 5)
    # commands = ['push 2', 'push 1', 'max', 'pop', 'max']
    # commands = ['push 1', 'push 2', 'max', 'pop', 'max']
    # commands = ['push 1', 'push 7', 'pop']
    commands = ['push 2', 'push 3', 'push 9', 'push 7', 'push 2', 'max', 'max', 'max', 'pop', 'max']
    # commands = ['push 7', 'push 1', 'push 7', 'max','pop', 'max']
    steck = Stack()
    t_start = perf_counter()
    for command in commands:
        if command == 'max':
            # print(steck.max())
            steck.max()
        elif command == 'pop':
            steck.pop()
        elif command.split()[0] == 'push':
            steck.push(command.split()[1])
    print('Время работы: ' + str(perf_counter() - t_start) + ' секунд')


if __name__ == '__main__':
    main()