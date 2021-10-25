import sys
sys.stdin = open('input.txt', 'r')

a,b,c, = map(int,input().split())

res = []
res.append((a+b)%c)
res.append(((a%c) + (b%c))%c)
res.append((a*b)%c)
res.append(((a%c) * (b%c))%c)
for i in range(len(res)):
    print(res[i])