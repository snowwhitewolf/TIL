import heapq

for t in range(int(input())):
    N, E = map(int, input().split())
    dist = [0] + [float('inf') for _ in range(N)]
    node = [[] for _ in range(N + 1)]
    visited = [0 for _ in range(N + 1)]
    for _ in range(E):
        a, b, c = list(map(int, input().split()))
        node[a].append((b, c))
    queue = []
    heapq.heappush(queue, (0, 0))
    while queue:
        d, idx = heapq.heappop(queue)
        if visited[a]:
            continue
        visited[idx] = 1
        for a, b in node[idx]:
            if dist[a] > d + b:
                dist[a] = d + b
                heapq.heappush(queue, (dist[a], a))
    print('#{} {}'.format(t + 1, dist[N]))