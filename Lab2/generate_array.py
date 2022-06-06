from random import randint


def generate_array(n, m, neg=True):
    a = []
    for _ in range(n):
        if neg:
            a.append(randint(-m, m))
        else:
            a.append(randint(1, m))
    return a