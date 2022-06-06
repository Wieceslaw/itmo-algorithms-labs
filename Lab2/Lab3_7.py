from generate_array import generate_array


def subarray_serach(a):
    sm = 0
    mx = -1
    start = 0
    end = 0
    sp = []
    for i in range(len(a)):
        if sm <= 0:
            start = i
            sm = 0
        sm += a[i]
        if sm > mx:
            mx = sm
            end = i
            sp.append((start, end))
    mx_sm_arr = a[sp[0][0]: sp[0][1] + 1]
    for i1, i2 in sp:
        if sum(a[i1: i2 + 1]) > sum(mx_sm_arr):
            mx_sm_arr = a[i1: i2 + 1]
    return mx_sm_arr


def main():
    a = generate_array(10, 100)
    print('Исходный массив: ', *a)
    print('Максимальный подмассив:', *subarray_serach(a))


if __name__ == "__main__":
    main()