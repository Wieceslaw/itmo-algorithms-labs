from random import randint


class Set:
    def __init__(self, n):
        self.m = n
        self.p = self.first_prime(n)
        self.table = [None] * n
        self.a1 = randint(1, self.p - 1)
        self.b1 = randint(0, self.p - 1)
        self.a2 = randint(0, self.p - 1)
        self.b2 = randint(0, self.p - 1)

    def first_prime(self, n):
        prime = False
        while not prime:
            n += 1
            flag = True
            for i in range(2, int(n ** 0.5)):
                if n % i == 0:
                    flag = False
            if flag:
                prime = True
        return n

    def h(self, x, a, b):
        return ((a * x + b) % self.p) % self.m
    
    def h1(self, x):
        return self.h(x, self.a1, self.b1)
    
    def h2(self, x):
        return self.h(x, self.a2, self.b2)

    def hash(self, x, i):
        return (self.h1(x) + (i * self.h2(x))) % self.m

    def insert(self, key, value):
        del_j = None
        for i in range(self.m):
            j = self.hash(key, i)
            if self.table[j] == (key, value):
                return
            elif self.table[j] == None:
                self.table[j] = (key, value)
                return
            elif self.table[j] == 'DELETED' and del_j is not None:
                del_j = j
        if del_j is not None:
            self.table[del_j] = (key, value)
        assert True ('Error')
        
    def remove(self, key):
        for i in range(self.m):
            j = self.hash(key, i)
            if self.table[j][0] == key:
                self.table[j] = 'DELETED'
                return
            elif self.table[j] is None:
                return 
        # assert True ('Not found')

    def __contains__(self, key):
        for i in range(self.m):
            j = self.hash(key, i)
            if self.table[j][0] == key:
                return True
            elif self.table[j] is None:
                return False
        return False

    def __str__(self):
        return self.table.__str__()


def input(filename):
    with open(filename, mode='rt') as file:
        result = [line.strip().split() 
        for line in file.readlines()]
    return result


def main():
    sl = {}
    n, *result = input('input.txt')
    for line in result:
        if line[0] == 'add':
            sl[line[1]] = line[2]
        elif line[0] == 'find':
            if line[1] in sl:
                print(sl[line[1]])
            else:
                print('not found')
        elif line[0] == 'del':
            if line[1] in sl:
                del sl[line[1]]


if __name__ == '__main__':
    main()