T = int(input())

#입력 받을 숫자열
num_list = []

#T만큼 반복해서 입력을 받음
for i in range(T):
    N = int(input())
    #숫자열을 숫자 형태의 리스트로 받음
    num = list(map(int, input().split()))
    #이중 리스트로 숫자열을 저장
    num_list.append(num)



for t in range(T):
    print(f'#{t+1}',end = ' ')
    #숫자열을 오름차순 정렬한 후 리스트를 풀어서 출력
    print(*sorted(num_list[t]), sep = ' ')