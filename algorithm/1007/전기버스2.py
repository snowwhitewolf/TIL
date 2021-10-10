import sys
sys.stdin = open("input.txt",'r')

for t in range(int(input())):
    lst = list(map(int,input().split()))
    N = lst[0]
    charge = lst[1:]
    res = 124234543
    def func(now,bat,cnt):
        global res
        if now == N-1:
            if res > cnt:
                res = cnt
            return
        if now == 0:
            func(now + 1,charge[now], cnt)
        else:
            if bat > 0:
                func(now+1,charge[now],cnt+1)
                func(now+1, bat-1, cnt)
            else:
                func(now + 1,charge[now], cnt + 1)

    func(0,0,0)
    print('#{} {}'.format(t+1,res))