import sys
sys.stdin = open('input.txt','r')

for t in range(int(input())):
    N,M = map(int,input().split())
    person = [0]*(N+1)
    cnt = 1
    lst = [[]]*N
    for i in range(M):
        a,b = map(int,input().split())
        for j in range(len(lst)):
            if a in lst[j]
    print(person)
