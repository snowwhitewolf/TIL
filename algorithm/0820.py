def dfs(now):
    global check
    if now == -1: return
    if now == 99:
        check = 1
        return

    dfs(left[now])
    dfs(right[now])
    return
sdf

left = [-1 for _ in range(100)]
right = [-1 for _ in range(100)]
visited = [0 for _ in range(100)]

N = 16
lst = list(map(int, input().split()))
i = 0
while i < 2 * N:
    from_, to_ = lst[i], lst[i + 1]
    if left[from_] == -1:
        left[from_] = to_
    else:
        right[from_] = to_
    i += 2

check = 0
dfs(0)  # 99번 노드에 도착할수 있는가?
if check == 1:
    print("갈수 있다")
else:
    print("갈수 없다")