class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self):
        self.first = None
        self.lenght = 0
    
    def __str__(self):
        result = ''
        node = self.first
        while node != None:
            result += f'{str(node.value)} -> '
            node = node.next
        return result + 'None'
    
    def __contains__(self, value):
        node = self.first
        while node != None:
            if node.value == value:
                return True
            node = node.next
        return False

    def popleft(self):
        if self.lenght == 1:
            result = self.first.value
            self.fisrt = None
            self.lenght -= 1
            return result
        elif self.lenght > 1:
            result = self.first.value
            self.first = self.first.next
            self.lenght -= 1
            return result

    def appendleft(self, value):
        node = Node(value)
        if self.lenght == 0:
            self.first = node
        else:
            node.next = self.first
            self.first = node
        self.lenght += 1

    def popafter(self, key):
        needle = None
        node = self.first
        while node != None:
            if node.value == key:
                needle = node
                break
            node = node.next
        if needle:
            result = needle.next
            needle.next = result.next
            return result.value

    def appendafter(self, key, value):
        needle = None
        node = self.first
        while node != None:
            if node.value == key:
                needle = node
                break
            node = node.next
        if needle:
            new_node = Node(value)
            new_node.next = needle.next
            needle.next = new_node


def main():
    lst = LinkedList()
    lst.appendleft('1')
    print(lst)
    lst.appendleft('2')
    print(lst)
    lst.appendleft('3')
    print(lst)
    lst.popleft()
    print(lst)
    print('1' in lst)
    print(1 in lst)
    print(lst)
    lst.appendafter('1', '3')
    print(lst)
    lst.popafter('2')
    print(lst)


if __name__ == '__main__':
    main()