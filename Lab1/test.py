from random import randint


def generate_array(n, m, neg=True):
    a = []
    for _ in range(n):
        if neg:
            a.append(randint(-m, m))
        else:
            a.append(randint(1, m))
    return a


def selection_sort(a):
    count = 0
    for j in range(len(a) - 1):
        min_i = len(a) - 1
        for i in range(j + 1, len(a)):
            count += 1
            if a[i] < a[min_i]:
                min_i = i
        if a[j] > a[min_i]:
            a[j], a[min_i] = a[min_i], a[j]
    print(count)
    return a


a = generate_array(10, 10)
print(a)
result = selection_sort(a)
print(result)