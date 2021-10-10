import sys
sys.stdin = open("input.txt","r")

def q_sort(lst):
    if len(lst) <= 1:
        return lst
    pivot = lst[len(lst) // 2]
    lst1, lst2, lst3 = [], [], []
    for num in lst:
        if num < pivot:
            lst1.append(num)
        elif num > pivot:
            lst3.append(num)
        else:
            lst2.append(num)
    return q_sort(lst1) + lst2 + q_sort(lst3)

for t in range(1,int(input())+1):
    N = int(input())
    lst = list(map(int,input().split()))
    print('#{} {}'.format(t,q_sort(lst)[N//2]))