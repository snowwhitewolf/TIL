'''
100점부터 0점까지 하나씩 대입하면서 같은 값이 존재하면 끝
'''
T = int(input())

for t in range(T):
    nk = list(map(int, input().split()))
    test = list(map(int, input().split()))
    N = nk[0]
    K = nk[1]

    result = 0
    test.sort(reverse=True)
    for i in range(K):
        result += test[i]
    print(f'#{t+1} {result}')
    #cnt = 0
    # for i in range(100,-1,-1):
    #     while cnt != K:
    #         if i in test:
    #             result += i
    #             cnt += 1
    
