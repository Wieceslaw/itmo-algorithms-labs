class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None

    def connect_left(self, left_node):
        self.prev = left_node
        left_node.next = self

    def connect_right(self, right_node):
        self.next = right_node
        right_node.prev = self


class DoublyLinkedList:
    def __init__(self) -> None:
        self.first = None
        self.last = None
        self.lenght = 0

    def __str__(self):
        result = 'None <-> '
        node = self.first
        while node != None:
            result += f'{node.value.__repr__()} <-> '
            node = node.next
        return result + 'None'

    def __contains__(self, value):
        node = self.first
        while node != None:
            if node.value == value:
                return True
            node = node.next
        return False

    def pop(self):
        if self.lenght == 1:
            result = self.last.value
            self.last = None
            self.first = None
            self.lenght -= 1
            return result
        elif self.lenght > 1:
            result = self.last.value
            self.last = self.last.prev
            self.last.next = None
            self.lenght -= 1
            return result

    def popleft(self):
        if self.lenght == 1:
            result = self.first.value
            self.last = None
            self.first = None
            self.lenght -= 1
            return result
        elif self.lenght > 1:
            result = self.first.value
            self.first = self.first.next
            self.lenght -= 1
            return result
    
    def append(self, value):
        node = Node(value)
        if self.lenght == 0:
            self.first = node
            self.last = node
        else:
            self.last.connect_right(node)
            self.last = node
        self.lenght += 1

    def appendleft(self, value):
        node = Node(value)
        if self.lenght == 0:
            self.first = node
            self.last = node
        else:
            self.first.connect_left(node)
            self.first = node
        self.lenght += 1

    def popbefore(self, key):
        needle = None
        node = self.first
        while node != None:
            if node.value == key:
                needle = node
                break
            node = node.next
        if needle:
            result = needle.prev
            if result:
                if result == self.first:
                    self.first = needle
                    needle.prev = None
                else:
                    needle.prev = result.prev
                    result.prev.next = needle
                return result.value


    def appendbefore(self, key, value):
        needle = None
        node = self.first
        while node != None:
            if node.value == key:
                needle = node
                break
            node = node.next
        if needle:
            new_node = Node(value)
            if needle == self.first:
                self.first = new_node
                new_node.connect_right(needle)
            else:
                new_node.connect_left(needle.prev)
                new_node.connect_right(needle)

    def check_nodes(self):
        node = self.first
        print('=======')
        while node != None:
            print(f'{node.prev} <-> {node.next}')
            node = node.next
        print('=======')

def main():
    dlst = DoublyLinkedList()
    dlst.append('1')
    dlst.append('2')
    print(dlst)
    dlst.appendleft('3')
    print(dlst)
    dlst.append(3)
    print(dlst)
    print('3' in dlst)
    print(3 in dlst)
    print('4' in dlst)
    print(dlst)
    dlst.pop()
    print(dlst)
    dlst.popleft()
    dlst.appendleft('3')
    dlst.appendleft('4')
    dlst.append('5')
    print(dlst)
    dlst.popbefore('3')
    print(dlst)
    dlst.appendbefore('5', '123')
    print(dlst)
    dlst.appendbefore('3', '67')
    print(dlst)
    dlst.appendbefore('2', '88')
    print(dlst)


if __name__ == '__main__':
    main()