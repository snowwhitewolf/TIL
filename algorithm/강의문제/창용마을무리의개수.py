import sys
sys.stdin = open("text.txt","r")

def Find(a) :
    if parent[a] == a :return a
    ret = Find(parent[a])
    parent[a] = ret
    return ret

def Union(a,b):
    global group_cnt
    pa = Find(a)
    pb = Find(b)
    if pa != pb :
        group_cnt -= 1
        parent[pb] = pa
    return

T = int(input())

for tc in range(1,T+1):
    N,M = map(int ,input().split())
    parent = [i for i in range(N+1)]
    group_cnt = N

    for _ in range(M) :
        a,b = map(int ,input().split())
        Union(a,b)
    print("#{} {}".format(tc, group_cnt))