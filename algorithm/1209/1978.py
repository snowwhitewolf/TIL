N = int(input())
lst = list(map(int,input().split()))
res = [1] * 1001
res[1] = 0
total = 0
sosu = [2,3,5,7,11,13,17,19,23,29]
for i in sosu:
    j = 2
    while True:
        if i*j >= 1001:
            break
        if res[i * j]:
            res[i*j] = 0
        j += 1


for i in lst:
    if res[i]:
        total += 1
print(total)
