lst = [0,1,2,3,4,5,6,7,8]
def dfs(now):
    if now >= len(lst) : return
    if lst[now] == 0: return

    dfs(now*2) # left subtree
    print(lst[now], end=' ')
    dfs(now*2+1) # right subtree

    return

dfs(1)