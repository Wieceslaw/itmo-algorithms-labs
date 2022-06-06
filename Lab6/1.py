from random import random, randint, choice


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

    def insert(self, value):
        del_j = None
        for i in range(self.m):
            j = self.hash(value, i)
            if self.table[j] == value:
                return
            elif self.table[j] == None:
                self.table[j] = value
                return
            elif self.table[j] == 'DELETED' and del_j is not None:
                del_j = j
        if del_j is not None:
            self.table[del_j] = value
        # assert True ('Error')
        
    def remove(self, value):
        for i in range(self.m):
            j = self.hash(value, i)
            if self.table[j] == value:
                self.table[j] = 'DELETED'
                return
            elif self.table[j] is None:
                return 
        # assert True ('Not found')

    def __contains__(self, value):
        for i in range(self.m):
            j = self.hash(value, i)
            if self.table[j] == value:
                return True
            elif self.table[j] is None:
                return False
        return False

    def __str__(self):
        return self.table.__str__()


def func(n, commands):
    st = Set(n)
    result = []
    k = 0
    for com in commands:
        if com[0] == 'A':
            st.insert(com[1])
        elif com[0] == '?':
            result.append(com[1] in st)
        elif com[0] == 'D':
            st.remove(com[1])
    return result
    

def input(filename):
    with open(filename, mode='rt') as file:
        result = [(line.strip().split()[0], int(line.strip().split()[1])) 
        if len(line.strip()) != 1 else int(line.strip()) for line in file.readlines()]
    return result


def main():
    n, *commands = input('input.txt')
    result = func(n, commands)
    for el in result:
        if el:
            print('Y')
        else:
            print('N')


if __name__ == '__main__':
    main()