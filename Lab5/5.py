from timing import timing


def input(filename):
    with open(filename, mode='rt') as file:
        res = [list(map(int, line.strip().split())) for line in file.readlines()]
    return res


class Queue:
    def __init__(self):
        self.sp = []
    
    def insert(self, x):
        self.sp.append(x)

    def increase(self, i, key):
        self.sp[i] = (key, self.sp[i][1])
        self.heapify(i)
    
    def heapify(self, i):
        left = (i + 1) * 2 - 1
        right = left + 1
        new = i
        if left < len(self.sp) and self.sp[new] > self.sp[left]:
            new = left
        if right < len(self.sp) and self.sp[new] > self.sp[right]:
            new = right
        if new != i:
            self.sp[i], self.sp[new] = self.sp[new], self.sp[i]
            self.heapify(new)

    def top(self):
        return self.sp[0]


@timing
def func(n, m, array):
    queue = Queue()
    res = []
    for i in range(n):
        queue.insert((0, i))
    for j in range(m):
        top = queue.top()
        res.append(top[::-1])
        queue.increase(0, array[j] + top[0])
    return res


@timing
def func1(n, m, array):
    streams = [0 for i in range(n)]
    i = 0
    t = 0
    res = []
    while i < m:
        mn = min(streams)
        t += mn
        streams = [el - mn for el in streams]
        for j, el in enumerate(streams):
            if el == 0 and i < m:
                res.append([j, t])
                streams[j] = array[i]
                i += 1
    return res


def main():
    data = input('input52.txt')
    n, m = data[0]
    array = data[1]
    result = func(n, m, array)
    result1 = func1(n, m, array)
    flag = True
    for line in zip(result, result1):
        if line[0] != tuple(line[1]):
            flag = False
            break
    print(flag)


if __name__ == '__main__':
    main()