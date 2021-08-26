n = int(input())
lst = []
for i in range(n):
    lst.append(list(map(int,input().split())))
paper = [[0]*101 for _ in range(101)]

for i in range(n):
    sty = lst[i][1]+10
    stx = lst[i][0]
    for y in range(10):
        for x in range(10):
            paper[sty-y][stx+x] = 1
cnt = 0
for i in range(101):
    for j in range(101):
        if paper[i][j] == 1:
            cnt += 1
print(cnt)