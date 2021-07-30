'''
총 N명 중에서 A 와 B 모두 구독하는 최소 최대
최대 : 2개중 작은 수
최소 : A B 의 합에서 N을 뺀값(단 마이너스 일떄는 0)
'''


T = int(input())
for t in range(1, T+1):
    a = list(map(int, input().split()))
    N = a[0]
    A = a[1]
    B = a[2]

    max_sub = min(A, B)
    if A+B >= N:
        min_sub = A+B-N
    else:
        min_sub = 0
    print(f'#{t} {max_sub} {min_sub}')