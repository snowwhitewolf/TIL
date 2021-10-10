import sys
sys.stdin= open('input.txt', "r")

N,S = map(int,input().split())
lst = list(map(int,input().split()))
res = 0
def f(level, s):
    global res
    if level ==N:
        if s == S:
            res += 1
        return
    f(level + 1, s)
    f(level + 1, s + lst[level])

f(0,0)
if S == 0:
    res -= 1
print(res)

