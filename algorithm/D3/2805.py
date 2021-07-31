T = int(input())

for t in range(1,T+1):
    N = int(input())
    a_list = []
    for i in range(N):
        a = str(input())
        a_list.append(a)
    result = 0
    cnt = 1
    k = 1
    result += int(a_list[0][N//2])
    for i in range(1,N):
            if len(a_list[i][N//2-cnt:N//2+cnt+1]) ==N:
                k = -1
            rlist = a_list[i][N//2-cnt:N//2+cnt+1]
            for i in range(len(rlist)):
                result += int(rlist[i])
            cnt += k
    print(f'#{t} {result}')