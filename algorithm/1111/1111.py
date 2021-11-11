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

def f2(lst):
    global MAP
    MAP2 = []
    MAP2.append(lst[0])
    MAP = MAP[1:]
    MAP2.append(MAP)
    MAP = MAP2

def f4(lst):
    for i in range(0,N//2):

while True:
    cnt += 1
    f1(MAP)
    f2(MAP)
    print(MAP)
    if max(MAP)-min(MAP) <= K:
        break

print(cnt)