N,M,sy,sx,K = map(int,input().split())
MAP = []
for _ in range(N):
    MAP.append(list(map(int,input().split())))
move = list(map(int,input().split()))
dy = [0,0,0,-1,1]
dx = [0,1,-1,0,0]
y = sy
x = sx
dice = [0]*7
for i in range(K):
    if 0 > y+dy[move[i]] or y+dy[move[i]] >= N or 0 > x+dx[move[i]] or x+dx[move[i]] >= M:
        continue
    else:
        y += dy[move[i]]
        x += dx[move[i]]
        if move[i] == 1:
            dice[1],dice[3],dice[4],dice[6] = dice[3],dice[6],dice[1],dice[4]
        elif move[i] == 2:
            dice[1], dice[3], dice[4],dice[6] = dice[4], dice[1], dice[6],dice[3]
        elif move[i] == 3:
            dice[1], dice[2], dice[5], dice[6] = dice[2], dice[6], dice[1],dice[5]
        else:
            dice[1], dice[2], dice[5], dice[6] = dice[5], dice[1], dice[6], dice[2]
        if MAP[y][x]:
            dice[1] = MAP[y][x]
            MAP[y][x] = 0
        else:
            MAP[y][x] = dice[1]
        print(dice[6])
