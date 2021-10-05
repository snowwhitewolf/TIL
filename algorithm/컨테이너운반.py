import sys
sys.stdin= open('input.txt', "r")

def f(N,M):
        global res
        for i in range(N):
            for j in range(M):
                if t[i] >= c[j]:
                    res += c[j]
                    del c[j]
                    del t[i]
                    return
                else:
                    del c[j]
                    return

for tc in range(int(input())):
    N,M = map(int,input().split())
    c = list(map(int,input().split()))
    t = list(map(int,input().split()))

    c.sort(reverse=True)
    t.sort(reverse=True)
    res = 0
    while t and c:
        f(len(t),len(c))

    print('#{} {}'.format(tc+1,res))