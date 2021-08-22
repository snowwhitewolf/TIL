# Alice가 시작
# x가 2x 또는 2x+1
# 두 선택지의 차이가 크지 않음
# x가 10이면 6이상 만들면 승리
#
for t in range(int(input())):
    N, L = map(int, input().split())
    arr = [list(map(int,input().split())) for _ in range(N)]
    result = arr[0][0]

    for i in range(1 << N):
        cal = 0
        point = 0
        for j in range(N):
            if i & (1 << j):
                cal += arr[j][1]
                point += arr[j][0]
        if (cal <= L) & (point > result):
            result = point
    print('#{} {}'.format(t+1,result))