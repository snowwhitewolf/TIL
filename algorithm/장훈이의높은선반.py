import sys
sys.stdin = open("input.txt",'r')


def func(level, num):
    global res
    if level == N:
        if num >= B:
            if num - B < res:
                res = num - B
        return
    func(level+1, num + H[level])
    func(level+1, num)


for t in range(int(input())):
    N,B = map(int,input().split())
    H = list(map(int,input().split()))
    res = 756787854564
    H.sort(reverse=True)
    func(0,0)
    print('#{} {}'.format(t+1,res))