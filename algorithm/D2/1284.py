'''
수도요금
A : PW
B : Q +S(W-R) or if W< R Q
총 사용량 W
'''

T = int(input())

for t in range(1,T+1):
    num = list(map(int, input().split()))

    P = num[0]
    Q = num[1]
    R = num[2]
    S = num[3]
    W = num[4]

    A_cost = P * W
    B_cost = 0
    if W <= R:
        B_cost = Q
    else:
        B_cost = Q + S*(W-R)

    result = min((A_cost, B_cost))

    print(f'#{t} {result}')