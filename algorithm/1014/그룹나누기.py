import sys
sys.stdin = open('input.txt','r')

for t in range(int(input())):
    N,M = map(int,input().split())
    num = list(map(int,input().split()))
    p = [0] * (N+1)
    p[0] = 1
    cnt = 0
    for i in range(0,len(num)-1,2):
        if p[num[i]]==0 and p[num[i+1]]==0:
            cnt += 1
        p[num[i]] = 1
        p[num[i+1]] = 1
    cnt += p.count(0)
    print('#{} {}'.format(t+1,cnt))