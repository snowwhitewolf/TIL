def winner(a,b):
    if card[a] == card[b] : return a
    if (card[a] == 1 and card[b] == 3) or \
            (card[a] == 2 and card[b] == 1) or \
            (card[a] == 3 and card[b] == 2) :
        return a
    else :
        return b


def dfs(s,e):
    if s == e :
        return s
    mid = (s+e)//2
    a = dfs(s,mid) # 왼쪽
    b = dfs(mid+1,e) # 오른쪽
    ret = winner(a,b)
    return ret


for t in range(int(input())):
    card = [-1]
    N = int(input())
    card += list(map(int, input().split()))
    ret = dfs(1, N)
    print('#{} {}'.format(t+1,ret))