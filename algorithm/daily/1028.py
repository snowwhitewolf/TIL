#다음 세대 변환 함수
def gen(lst):
    new_lst = lst[::-1]
    for i in range(len(lst)):
        new_lst[i] = (new_lst[i]+1)%4
    return lst + new_lst
N = int(input())

cnt = 0
dx = [1,0,-1,0]
dy = [0,-1,0,1]
on = []
for _ in range(N):
    x,y,d,g = map(int,input().split())
    #첫번째 방향 추가
    move = [d]
    #세대 만큼 반복
    for _ in range(g):
        move = gen(move)
    on.append([y, x])
    #값 추가
    for d in move:
        x += dx[d]
        y += dy[d]
        on.append([y,x])

# 맵에 커브 추가
MAP = [[0]*101 for _ in range(101)]
for i in range(len(on)):
    MAP[on[i][0]][on[i][1]] = 1

# 커브 개수 확인
for y in range(100):
    for x in range(100):
        if MAP[y][x] == MAP[y+1][x] == MAP[y][x+1] == MAP[y+1][x+1] == 1:
            cnt += 1
print(cnt)