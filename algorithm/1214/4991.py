
while True:
    w, h = map(int,input().split())
    dust_cnt = 0
    if w == 0:
        break
    MAP = [list(input().split()) for _ in range(h)]
    for y in range(h):
        for x in range(w):
            if MAP[y][x] == '*':
                dust_cnt += 1
                continue
            elif MAP[y][x] == 'o':
                sy = y
                sx = x

    def bfs(y,x,dirty, cnt):
        if len(dirty) == dust_cnt:
            return cnt