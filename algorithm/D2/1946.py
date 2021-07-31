'''
너비가 10인 여러줄의 문자열
알파벳으로 채워져있고 마지막 줄은 왼쪽부터
알파벳과 숫자로 이루어진 입력
'''
T = int(input())

for t in range(1,T+1):
    result = ''
    ch_list = []
    N = int(input())
    
    for n in range(N):
        ch_num = list(map(str, input().split()))
        ch_list.append(ch_num)

    for i in range(N):
        result += ch_list[i][0] * int(ch_list[i][1])

    total = len(result) //10 + 1
    
    print(f'#{t}')
    for i in range(total):
        print(result[:10])
        result = result[10:]