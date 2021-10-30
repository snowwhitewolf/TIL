import sys
sys.stdin = open('input.txt','r')

lst = list(map(int,input().split()))
res = sorted(lst)[3]
while True:
    cnt = 0
    for i in range(5):
        if res%lst[i] == 0:
            cnt += 1
    if cnt >= 3:
        break
    res += 1
print(res)
