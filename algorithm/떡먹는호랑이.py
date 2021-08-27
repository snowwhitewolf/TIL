d,k = map(int,input().split())

resa = 0
resb = 0
def f(d,k):
    for a in range(1,k):
        for b in range(1,k):
            if a+b > k:
                break
            lst = [a, b]
            for i in range(2, d):
                lst.append(lst[i - 1] + lst[i - 2])
            if lst[d-1] == k:
                return [a,b]
res = f(d,k)
print(res[0])
print(res[1])