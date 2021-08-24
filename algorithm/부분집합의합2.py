def func(level):
    global k
    if level == n and sum(res) == k:
        global cnt
        cnt += 1
        return
    for i in range(1,k-2):
        if c[i-1] == 0:
            res.append(i)
            c[i-1] = 1
            if sum(res) > k:
                break
            func(level+1)
            c[i-1] = 0
            res.pop()
        else:
            continue
    return

for t in range(int(input())):
    lst = [i for i in range(1, 21)]
    c = [0 for _ in range(20)]
    n,k = map(int,input().split())
    res = []
    cnt = 0
    a = n
    cc = 1
    while a != 1:
        cc *= a
        a-= 1
    func(0)
    cnt //= cc
    print('#{} {}'.format(t+1,cnt))
