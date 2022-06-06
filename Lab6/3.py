class ChainSet:
    def __init__(self, m):
        self.m = m
        self.table = [None] * m

    def add(self, value):
        index = self.hash(value)
        if self.table[index] is None:
            self.table[index] = [value]
            return
        if value in self.table[index]:
            return
        self.table[index].append(value)

    def delete(self, value):
        index = self.hash(value)
        if self.table[index] is None:
            return
        for i, el in enumerate(self.table[index]):
            if el == value:
                del self.table[index][i]
                if len(self.table[index]) == 0:
                    self.table[index] = None
                break

    def find(self, value):
        index = self.hash(value)
        if self.table[index] is None:
            return False
        return value in self.table[index]

    def check(self, index):
        if self.table[index] is None:
            return ''
        return self.table[index]

    def hash(self, string):
        return (sum(ord(el) * (263 ** i) for i, el in enumerate(string)) % 1000000007) % self.m 


def func(m, n, commands):
    _set = ChainSet(m)
    result = []
    for com in commands:
        if com[0] == 'add':
            _set.add(com[1])
        elif com[0] == 'del':
            _set.delete(com[1])
        elif com[0] == 'find':
            if _set.find(com[1]):
                result.append('yes')
            else:
                result.append('no')
        elif com[0] == 'check':
            result.append(' '.join(_set.check(int(com[1]))[::-1]))
    return result


def input(filename):
    with open(filename, mode='rt') as file:
        m, n, *result = [line.strip().split() for line in file.readlines()]
    return int(m[0]), int(n[0]), result


def main():
    m, n, commands = input('33.txt')
    result = func(m, n, commands)
    for el in result:
        print(el)

if __name__ == '__main__':
    main()