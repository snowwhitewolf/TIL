n = int(input())
lst = []
lsty = []
lstx = []
for i in range(n):
    lst.append(list(map(int,input().split())))
    lsty.append(lst[i][1])
    lstx.append(lst[i][0])
lmty = max(lsty)+12
lmtx = max(lstx)+12
paper = [[0]*lmtx for _ in range(lmty)]
dy = [-1,-1,-1,0,0,1,1,1]
dx = [-1,0,1,-1,1,-1,0,1]
no = 0
for i in range(n):
    sty = lst[i][1]+10
    stx = lst[i][0]
    for y in range(10):
        for x in range(10):
            if paper[sty-y][stx+x] == 1:
                no = 1
            else:
                paper[sty-y][stx+x] =1
cnt = 0
def f(y,x):
    for k in range(8):
        if paper[y + dy[k]][x + dx[k]] == 0:
            return 1
    return 0

for i in range(lmty):
    for j in range(lmtx):
        if paper[i][j] == 1:
            for k in range(8):
                if f(i,j) == 1:
                    cnt += 1
                    break

if no == 0:
    print(40*n)
else:
    print(cnt)
for i in range(len(paper)):
    print(paper[i])