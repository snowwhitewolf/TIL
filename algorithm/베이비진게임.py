import sys
sys.stdin = open('input.txt',"r")

for t in range(1,int(input())+1):
    num = '0123456789'
    lst = list(input().split())
    res = 0
    a = []
    b = []
    for i in range(0,12,2):
        a.append(lst[i])
        b.append(lst[i+1])
    def func(lst):
        n = sorted(lst)
        aa = ''
        for i in range(len(n)):
            aa += n[i]
        for i in range(0,len(n)-2):
            if aa[i:i+3] in num:
                return True
            if aa.count(aa[i]) >= 3:
                return True
        return False
    for j in range(3,12):
        if func(a[:i]):
            res = 1
            break
        if func(b[:i]):
            res = 2
            break
    print('#{} {}'.format(t,res))