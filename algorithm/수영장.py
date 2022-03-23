for t in range(int(input())):
    c1,c30,c90,c365 = map(int,input().split())
    lst = list(map(int,input().split()))
    res = c365
    def func(now,cost):
        global res
        if now>=12:
            res = min(res,cost)
            return
        else:
            func(now + 1, cost + c1 * lst[now])
            func(now + 1, cost + c30)
            func(now + 3, cost + c90)
    func(0,0)
    print('#{} {}'.format(t+1,res))