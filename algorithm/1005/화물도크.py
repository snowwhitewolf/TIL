import sys
sys.stdin = open("input.txt",'r')

for t in range(int(input())):
    N = int(input())
    lst = []
    for i in range(N):
        a,b = map(int,input().split())
        lst.append((a,b))
    print(lst)
    lst.sort(key=lst[1])
    print(lst)