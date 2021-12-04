import sys
sys.stdin = open('input.txt', 'r')

N,M,K = map(int,input().split())
A = [list(map(int,input().split())) for _ in range(N)]
MAP = [[0]*N for _ in range(N)]
for _ in range(M):
    x,y,age = map(int,input().split())
    MAP[y-1][x-1] = age
print(MAP)