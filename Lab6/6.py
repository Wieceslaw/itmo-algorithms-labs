def create_fib(n):
    a = 0
    b = 1
    st = set()
    st.add(0)
    st.add(1)
    for _ in range(2, n):
        res = (a + b)
        a = b
        b = res
        st.add(res)
    return st


fibs = set(create_fib(24000))
n = int(input())
result = [int(input()) for _ in range(n)]
for el in result:
   if el in fibs:
       print('Yes')
   else:
       print('No')