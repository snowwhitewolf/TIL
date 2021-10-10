for t in range(10):
    N = int(input())
    lst = []
    for _ in range(N):
        lst.append(list(input().split()))
    tree = [0 for _ in range(N+1)]
    for i in range(N):
        if len(lst[i]) == 2:
            tree[int(lst[i][0])] = int(lst[i][1])
    for i in range(N,0,-1):
        if tree[i] == 0:
            if lst[i-1][1] == '+':
                tree[i] = tree[int(lst[i-1][2])] + tree[int(lst[i-1][3])]
            elif lst[i-1][1] == '-':
                tree[i] = tree[int(lst[i-1][2])] - tree[int(lst[i-1][3])]
            elif lst[i - 1][1] == '*':
                tree[i] = tree[int(lst[i-1][2])] * tree[int(lst[i-1][3])]
            elif lst[i - 1][1] == '/':
                tree[i] = tree[int(lst[i-1][2])] / tree[int(lst[i-1][3])]
    print('#{} {}'.format(t + 1, int(tree[1])))