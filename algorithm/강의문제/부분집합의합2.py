def dfs(num, sum,cnt, path):
    global ans
    if cnt > n:
        return
    if sum > k:
        return
    if num == 21:
        if cnt == n and sum == k:
            ans += 1
        return
    dfs(num+1, sum+num, cnt + 1,path+str(num))
    dfs(num+1, sum,cnt,path)
    return

for t in range(int(input())):
    n, k = map(int, input().split())
    ans = 0
    dfs(1,0,0,"")
    print('#{} {}'.format(t+1,ans))