n = int(input())
res = 0
def f(n, cnt):
    global res
    if n == 0:
        res += cnt
        return
    if n >= 20:
        f(n-20,cnt*939)
    if n >= 1:
        f(n-1, cnt+1)
    if n >=2:
        f(n-2, cnt+1)
f(n, 0)
print(res%10007)