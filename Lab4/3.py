from time import perf_counter


def input(file_name):
    with open(file_name, mode='rt') as file:
        result = [line.strip() for line in file.readlines()]
    return result


class Stack:
    def __init__(self):
        self.sp = []

    
    def push(self, el):
        self.sp.append(el)


    def pop(self):
        if len(self.sp) > 0:
            return self.sp.pop()

    def __str__(self) -> str:
        return ' '.join(self.sp)


def func(array):
    flag = True
    stack = Stack()
    for el in array:
        if el == '[' or el == '(':
            stack.push(el)
        elif el == ')':
            last = stack.pop()
            if last != '(':
                flag = False
                break
        elif el == ']':
            last = stack.pop()
            if last != '[':
                flag = False
                break
    if len(stack.sp) != 0:
        flag = False
    return 'YES' if flag else 'NO'



def main():
    arrays = input('input3_true.txt')
    arrays = ['(']
    t_start = perf_counter()
    for array in arrays:
        print(func(array))
        # func(array)
    print('Время работы: ' + str(perf_counter() - t_start) + ' секунд')


if __name__ == '__main__':
    main()