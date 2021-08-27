def dfs(now) :
    if now == 0 :
        return
    preorder.append(now)
    dfs(left[now])
    dfs(right[now])
    postorder.append(now)
    return

left = [0 for _ in range(11)]
right = [0 for _ in range(11)]

root = 1
left[1] = 3
right[1] = 5
left[3] = 2
right[3] = 6
left[5] = 7
right[5] = 8
left[7] = 9
left[9] = 10
right[8] = 4

preorder = []
postorder = []
inorder  = []
dfs(root)
print(preorder)
print(postorder)
print(inorder)