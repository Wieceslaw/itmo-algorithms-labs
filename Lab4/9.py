from time import perf_counter


class Node:
    def __init__(self, el):
        self.el = el
        self.next = None
        self.prev = None
    
    def connect_left(self, left_node):
        self.prev = left_node
        left_node.next = self

    def connect_right(self, right_node):
        self.next = right_node
        right_node.prev = self

    def insert_right(self, right_node):
        self.next.connect_left(right_node)
        self.connect_right(right_node)

    def insert_left(self, left_node):
        self.prev.connect_right(left_node)
        self.connect_left(left_node)
    

class LinkedList:
    def __init__(self):
        self.first = None
        self.last = None
        self.centr = None
        self.length = 0

    def len(self):
        return self.length 

    def append(self, el):
        node = Node(el)
        if self.length == 0:
            self.first = node
            self.last = node
            self.centr = node
        else:
            if self.length % 2 == 0:
                self.centr = self.centr.next
            self.last.connect_right(node)
            self.last = node
        self.length += 1

    def popleft(self):
        if self.length == 1:
            result = self.first.el
            self.first = None
            self.last = None
            self.centr = None
            self.length = 0
            return result
        elif self.length > 1:
            result = self.first.el
            self.first.next.prev = None
            self.first = self.first.next
            if self.length % 2 == 0:
                self.centr = self.centr.next
            self.length -= 1
            return result

    def put_central(self, el):
        node = Node(el)
        self.centr.insert_right(node)
        if self.length % 2 == 0:
            self.centr = node
        self.length += 1

    def __str__(self):
        result = 'None'
        next = self.first
        while next != None:
            if next == self.centr:
                result += ' <-> (' + str(next.el) + ')'                
            else:
                result += ' <-> ' + str(next.el)
            next = next.next
        return result + ' <-> None'

    def to_list(self):
        result = []
        next = self.first
        while next != None:
            result.append(next.el)
            next = next.next
        return result


def input(file_name):
    with open(file_name, mode='rt') as file:
        result = [line.strip() for line in file.readlines()]
    return result


def main():
    array = input('input9.txt')
    queue = LinkedList()
    t_start = perf_counter()
    for el in array:
        # print(queue, '|', el)
        if el == '-':
            print(queue.popleft())
            # queue.popleft()
        if el.split()[0] == '+':
            queue.append(el.split()[1])
        if el.split()[0] == '*':
            queue.put_central(el.split()[1])
    print('Время работы: ' + str(perf_counter() - t_start) + ' секунд')


if __name__ == '__main__':
    main()