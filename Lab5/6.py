from timing import timing


def input(filename):
    res = []
    with open(filename, mode='rt') as file:
        for line in file.readlines():
            line = line.strip().split()
            if len(line) == 1:
                if line[0].isdigit():
                    res.append(int(line[0]))
                else:
                    res.append(line[0])
            elif len(line) == 2:
                res.append([line[0], int(line[1])])
            elif len(line) == 3:
                res.append([line[0], int(line[1]), int(line[2])])
    return res


class PriorityQueue:
    def __init__(self):
        self.a = []

    def parent(self, i):
        return (i - 1) // 2

    def left_child(self, i):
        return 2 * i + 1

    def right_child(self, i):
        return 2 * i + 2

    def min(self):
        return self.a[0]
    
    def extract_min(self):
        if len(self.a) < 1:
            return None
        res = self.min()
        self.a[0] = self.a[-1]
        del self.a[-1]
        self.heapify(0)
        return res

    def decrease(self, i, key):
        if key[0] > self.a[i][0]:
            return None
        self.a[i] = key
        while i > 0 and self.a[self.parent(i)][0] > self.a[i][0]:
            self.a[i], self.a[self.parent(i)] = self.a[self.parent(i)], self.a[i]
            i = self.parent(i)
    
    def heapify(self, i):
        left = self.left_child(i)
        right = self.right_child(i)
        if left < len(self.a) and self.a[left][0] < self.a[i][0]:
            smallest = left
        else:
            smallest = i
        if right < len(self.a) and self.a[right][0] < self.a[smallest][0]:
            smallest = right
        if smallest != i:
            self.a[i], self.a[smallest] = self.a[smallest], self.a[i]
            self.heapify(smallest)

    def insert(self, key):
        self.a.append((10e10, 0))
        self.decrease(len(self.a) - 1, key)

    def change(self, i, key):
        j = [j for j in range(len(self.a)) if self.a[j][1] == i][0]
        self.decrease(j, key)
    
    def __str__(self):
        return self.a.__str__()


@timing
def func(n, array):
    queue = PriorityQueue()
    res = []
    for i, command in enumerate(array):
        print(queue)
        if len(command) == 1:
            mn = queue.extract_min()
            if mn is not None:
                res.append(mn[0])
            else:
                res.append('*')
        elif len(command) == 2:
            queue.insert((command[1], i))
        elif len(command) == 3:
            queue.change(command[1] - 1, (command[2], None))
    return res


def main():
    data = input('input6.txt')
    n = data[0]
    array = data[1:]
    res = func(n, array)
    for el in res:
        print(el)
    

if __name__ == '__main__':
    main()