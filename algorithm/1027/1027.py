N = int(input())
lst = []
for _ in range(N):
    lst.append(input())
res = ''

for i in range(len(lst[0])):
    k = 0
    for j in range(1,N):
        if lst[j][i] != lst[0][i]:
            res += '?'
            k = 1
            break
    if k == 0:
        res += lst[0][i]

print(res)