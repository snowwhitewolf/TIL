def dfs(now) :
    if now == 0 :
        return
    preorder.append(now)
    dfs(left[now])
    inorder.append(now)
    dfs(right[now])
    postorder.append(now)
    return

lst = [0 for _ in range(11)]
lst[2*1] = 3
lst[2*1+1] = 5
preorder = []
postorder = []
inorder  = []
dfs(root)
print(*preorder)
print(*postorder)
print(*inorder)