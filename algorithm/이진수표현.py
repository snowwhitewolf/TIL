for t in range(1,int(input())+1):
    N,M = map(int,input().split())
    m = bin(M)
    cnt = 0
    num = '000000' + m[2:]
    if num[-1:-(N+1):-1] == '1'*N:
        print("#{} ON".format(t))
    else:
        print("#{} OFF".format(t))