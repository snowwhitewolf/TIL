'''
단조 증가하는 수
각 자리수가 증가하면 됨
주어진 양의 정수 N개 중에서 두개의 곱이 단조 증가하는 수인것들을 구하고 그중 최댓값을 출력
N개들의 숫자의 쌍을 먼저 구한뒤 그 값이 단조증가면 결과에 저장
결과값보다 큰 값이 나오면 덮는다.
'''

T = int(input())

for t in range(1,T+1):
    N = int(input())
    a = list(map(int, input().split()))

    def danzo(b):
        b_str = str(b)
        b_max = 0
        for i in range(len(b_str)-1):
            if int(b_str[i]) > int(b_str[i+1]):
                return False
        return True

    result = -1
    for i in range(N):
        cnt = 0
    
        while i+cnt != N:
            if i != i+cnt:
                ax = a[i] * a[i+cnt]
                if ax > result:
                    if danzo(ax) == True:
                        result = ax
            cnt += 1
    print(f'#{t} {result}')
