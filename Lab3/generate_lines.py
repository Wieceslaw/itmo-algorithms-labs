from random import randint


def generate_lines(n, m):
    with open('lines.txt', 'w') as file:
        for _ in range(n):
            file.write(''.join(chr(randint(97, 122))  for _ in range(m)) + '\n')



def main():
    n = 10 ** 6
    m = 50
    generate_lines(n, m)


if __name__ == '__main__':
    main()