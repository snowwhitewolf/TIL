'''
월일로 이루어진 날짜를 2개 입력받아 두 날짜의 차이
월은 1 ~ 12
두 달의 사이의 있는 월의 날짜수 + 첫번째 달의 최대수 - 주어진수 + 두번째 달의 주어진수
'''
T = int(input())

for t in range(1, T+1):
    date = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    a = list(map(int, input().split()))
    result = 0
    a1 = a[0]
    a2 = a[2]
    if a1 == a2:
        result = a[3] - a[1] + 1
    else:
        result += sum(date[a1:(a2-1)]) + a[3] + date[a1-1] - a[1] + 1
    print(f'#{t} {result}')