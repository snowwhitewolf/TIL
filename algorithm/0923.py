def dfs(now):
    if now == -1 : return
    dfs(left[now]) # left subtree
    dfs(right[now]) # right subtree
    print(now, end=' ')
    return

left = [-1 for _ in range(9)]
right= [-1 for _ in range(9)]

left[0] = 1
right[0] = 2
left[1] = 3
right[1] = 4
left[3] = 7
right[3] = 8
left[2] = 5
right[2] = 6

dfs(0)