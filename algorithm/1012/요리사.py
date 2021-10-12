import sys
sys.stdin = open('input.txt','r')
for t in range(int(input())):
    N = int(input())
    lst = [list(map(int,input().split())) for _ in range(N)]
    def f(n,path):

        f(n+1,path)
        f(n+1,path+'')

    lst[i][j]+lst[j][i]