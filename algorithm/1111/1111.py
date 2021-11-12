import sys
sys.stdin = open('input.txt','r')

N, K = map(int,input().split())
MAP=list(map(int,input().split()))
cnt = 0

def f1(lst):
    m = min(MAP)
    for i in range(N):
        if lst[i] == m:
            lst[i] += 1

print(cnt)