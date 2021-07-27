T = int(input())
#1부터 9까지 숫자 리스트
R = [1,2,3,4,5,6,7,8,9]
#t리스트에 3중 리스트로 값들을 저장
t_list = []
for t in range(T):
    s_list = []
    for j in range(9):
        s = list(map(int, input().split()))
        s_list.append(s)
    t_list.append(s_list)

#스도쿠 검증을 1~9까지의 숫자가 모두 존재하는지로 확인
#첫번째 검증 : 가로줄 확인
def check_1(ch_list):
    for i in range(9):
        if sorted(ch_list[i]) != R:
            return False
    return True
#두번째 검증 : 세로줄 확인
def check_2(ch_list):
    for i in range(9):
        test = []
        for j in range(9):
            #세로줄을 test리스트에 저장
            test.append(ch_list[j][i])
        #정렬된 test가 R과 같은지 비교
        if sorted(test) != R:
            return False
    return True
#세번째 검증 : 사각형 확인
def check_3(ch_list):
    a = 0
    b = 0
    test = []
    #4중 for loop로 각각의 사각형을 만들어 리스트로 확인
    for s in range(3):
        for k in range(3):
            for i in range(a,a+3):
                for j in range(b,b+3):
                    test.append(ch_list[i][j])
            if sorted(test) != R:
                return False
            test = []
            b += 3
        b = 0
        a += 3
    return True

# 세번의 검증을 모두 통과하면 1, 하나라도 실패시 0을 출력
for i in range(T):
    if check_1(t_list[i]) and check_2(t_list[i]) and check_3(t_list[i]):
        print(f'#{i+1} 1')
    else:
        print(f'#{i+1} 0')