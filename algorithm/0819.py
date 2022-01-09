for t in range(1,11):
    N , a = map(int,input().split())
    lst = []
    for i in str(a):
        lst.append(i)
    result = []
    while lst:
        s = lst.pop(0)
        if result == [] or result[-1] != s:
            result.append(s)
        else:
            result.pop()
    print('#{} {}'.format(t, int(''.join(result))))