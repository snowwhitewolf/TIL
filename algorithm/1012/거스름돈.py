coin = [50000, 10000,5000,1000,500,100,50,10]

N = 32850
cnt = 0 # 거스름돈 개수 세기

ans = []
for i in range(len(coin)):
    ans.append(N // coin[i])
    N %= coin[i]