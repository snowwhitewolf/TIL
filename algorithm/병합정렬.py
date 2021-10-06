import sys
sys.stdin = open("input.txt","r")


def merge(lst1, lst2):
    global cnt
    s1 = 0
    s2 = 0
    e1 = len(lst1)
    e2 = len(lst2)
    res = [0]*(e1+e2)
    now = 0
    if lst1[-1] > lst2[-1]:
        cnt += 1
    while s1 < e1 or s2 < e2:
        if s1 < e1 and s2 < e2:
            if lst1[s1] < lst2[s2]:
                res[now] = lst1[s1]
                now += 1
                s1 += 1
            else:
                res[now] = lst2[s2]
                now += 1
                s2 += 1
        else:
            if s1 < e1:
                res[now] = lst1[s1]
                now += 1
                s1 += 1
            else:
                res[now] = lst2[s2]
                now += 1
                s2 += 1
    return res


def div(lst):
    if len(lst) == 1:
        return lst
    mid = len(lst) // 2
    lst1 = div(lst[:mid])
    lst2 = div(lst[mid:])
    return merge(lst1, lst2)



for t in range(1,int(input())+1):
    N = int(input())
    lst = list(map(int,input().split()))
    cnt = 0
    print('#{} {} {}'.format(t,div(lst)[N//2],cnt))