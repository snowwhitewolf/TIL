N = input()
if len(N)== 1:
    N = '0' + N
N2 = N
cnt = 0
while True:
    num = int(N2[0]) + int(N2[1])
    N2 = N[1] + str(num)
    cnt += 1
    if  N == N2:
        print(cnt)
        break