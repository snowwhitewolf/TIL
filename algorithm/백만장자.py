# N일 동안 매매가를 알수 있음
# N이 100만 까지이므로 시간복잡도 따져야함
# 최대값 앞에 있는 날은 모두 사야함
# 맨 마지막값보다 큰값이 나올때까지 다 사고 큰값이 나오면 기준을 바꿈

for t in range(int(input())):
    n = int(input())
    lst = list(map(int, input().split()))
    max = lst[n - 1]
    res = 0
    for i in range(n-2, -1, -1):
        if lst[i] < max:
            res += max-lst[i]
        elif lst[i] > max:
            max = lst[i]
    print('#{} {}'.format(t+1, res))
