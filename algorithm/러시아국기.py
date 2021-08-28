#w,b,r 순서대로 정렬되어야함
#각 색깔의 갯수를 정해서 가야할 자리를 구함
#있어야할 자리라면 중복이 안됨
#모든 경우의 수를 따져야함
def color(lst,b_start,r_start):
    color_cnt = 0
    for y in range(1,r_limit):
        for x in range(m):
            if y < b_start:
                if lst[y][x] != 'W':
                    color_cnt += 1
            elif r_start < y:
                if lst[y][x] != 'R':
                    color_cnt += 1
            else:
                if lst[y][x] != 'B':
                    color_cnt += 1
    return color_cnt

for t in range(int(input())):
    n,m = map(int,input().split())
    lst = [list(input().rstrip()) for _ in range(n)]
    cnt = 0
    b_start = 0
    r_start = 0
    res = m*n
    for i in range(m):
        if lst[0][i] != 'W':
            cnt += 1
    for i in range(n-1,0,-1):
        if lst[i].count('B') < lst[i].count('R'):
            for j in range(m):
                if lst[0][i] != 'R':
                    cnt += 1
        else:
            r_limit = i+1
            break
    for i in range(1,r_limit-1):
        for j in range(i,r_limit+1):
            res = min(res,color(lst,i,j))
    res += cnt
    print(res)

