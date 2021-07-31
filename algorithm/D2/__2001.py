
T = int(input())

for t in range(1, T+1):
    nm = list(map(int, input().split()))
    N = nm[0]
    M = nm[1]
    n = []
    for i in range(N):
        n.append(list(map(int, input().split())))
    print(n)