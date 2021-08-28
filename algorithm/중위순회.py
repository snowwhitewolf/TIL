def dfs(now):
    if now > n or tree[now] == 0: return
    dfs(now * 2)
    inorder.append(tree[now])
    dfs(now*2 + 1)
    return

for t in range(1,11):
    lst = []
    n = int(input())
    for i in range(n):
        lst.append(list(input().split()))

    tree = [0 for _ in range(n+1)]
    for i in range(len(lst)):
        tree[int(lst[i][0])] = lst[i][1]

    inorder = []
    dfs(1)
    result = ''
    for i in range(len(inorder)):
            result += inorder[i]

    print('#{} {}'.format(t,result))
