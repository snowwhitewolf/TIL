for t in range(10):
    #입력받는공간
    T = int(input())
    s_list = []
    result = 0
    s=[]
    for j in range(100):
        s = list(map(int, input().split()))
        s_list.append(s)
    
    #가로줄일때의 최댓값
    for i in range(100):
        result = max(result,sum(s_list[i]))
    
    #세로줄일때의 최댓값
    sum1 = 0
    for j in range(100):
        for i in range(100):
            sum1 += s_list[i][j]
        result = max(result,sum1)
        sum1 = 0
    
    #오른쪽으로 가는 대각선
    sum1 = 0
    for i in range(100):
        sum1 += s_list[i][i]
    result = max(result,sum1)
    
    #왼쪽으로 가는 대각선
    sum1 = 0
    for i in range(100):
        sum1 += s_list[i][99-i]
    result = max(result,sum1)
    
    print(f'#{T} {result}')