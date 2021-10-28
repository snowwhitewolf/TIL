import sys
sys.stdin = open('input.txt','r')

N = int(input())
X = []
Y = []
D = []
G = []
cnt = 0
for _ in range(N):
    x,y,d,g = map(int,input().split())
    X.append(x)
    Y.append(y)
    D.append(d)
    G.append(g)

on_x = []
on_y = []



MAP = [[0]*(max(on_x)+1) for _ in range((max(on_x)+1))]
for i in range(len(on_x)):
    MAP[on_x[i]][on_y[i]] = 1
for y in range(len(MAP)):
    for x in range(len(MAP[0])):
        if MAP[y][x] == MAP[y+1][x] == MAP[y][x+1] == MAP[y+1][x+1] == 1:
            cnt += 1
print(cnt)