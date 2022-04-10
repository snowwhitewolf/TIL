import sys
sys.stdin = open('input.txt',"r")

def func(p):
    for j in range(10):
        if p[j] == 3:
            return True
    for k in range(8):
        if p[k] and p[k + 1] and p[k + 2]:
            return True
    return False
for t in range(1, int(input()) + 1):
    card = list(map(int, input().split()))
    p1 = [0] * 10
    p2 = [0] * 10
    res = 0
    for i in range(12):
        if not i % 2:
            p1[card[i]] += 1
            if func(p1):
                res = 1
                break
        else:
            p2[card[i]] += 1
            if func(p2):
                res = 2
                break
    print('#{} {}'.format(t,res))