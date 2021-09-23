lst = ['X','A','B','C','D','E','X','F','G','H']
def dfs(now):
    if now >= len(lst) : return
    if lst[now] == 'X': return

    dfs(now*2) # left subtree
    print(lst[now], end=' ')
    dfs(now*2+1) # right subtree
    return

dfs(1)