n = int(input())
k = int(input())
apple = []
board = list([0]*n for _ in range(n))
for _ in range(k):
    y,x = map(int,input().split())
    board[y][x] = 2

l = int(input())
move = []
for _ in range(l):
    move.append(list(input().split()))

bam = [[0,0]]
time = 1
eat = 0
dy = [0,1,0,-1]# 오른쪽 아래 왼쪽 위
dx = [1,0,-1,0]
d = 0
while eat != k:
    if len(move) != 0:
        if time == int(move[0][0]):
            if move[0][1] == 'D':
                d += 1
            else:
                d += 3
            del move[0]
    now = [bam[-1][0]+dy[d%4],bam[-1][1]+dx[d%4]]
    if 0 <= now[0] < n and 0<= now[1] < n and now not in bam:
        bam.append(now)
        time += 1
        if board[now[0]][now[1]] == 0:
            del bam[0]
        else:
            board[now[0]][now[1]] = 0
            eat += 1
    else:
        time += 1
        break

print(time)




