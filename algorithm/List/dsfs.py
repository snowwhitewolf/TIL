# Alice가 시작
# x가 2x 또는 2x+1
# 두 선택지의 차이가 크지 않음
# x가 10이면 6이상 만들면 승리
#
for i in range(1 << 5):
        for j in range(5):
            if i & (1<<j):
                print(j,end = ' ')
        print()
