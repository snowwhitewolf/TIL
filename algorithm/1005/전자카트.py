import sys
sys.stdin= open('input.txt', "r")

for t in range(1,int(input())+1):
    N = int(input())
    MAP = []
    for _ in range(N):
        MAP.append(list(map(int,input().split())))
    res = []
    def dfs(now,level,sum,path):
        if level == N-1:
            res.append(sum + MAP[now][0])
            return
        for i in range(1,N):
            if str(i) not in path:
                dfs(i,level+1,sum+MAP[now][i],path+str(i))
    dfs(0,0,0,'')
    print('#{} {}'.format(t,min(res)))