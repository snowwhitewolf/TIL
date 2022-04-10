for t in range(int(input())):

    N, M, L = map(int, input().split())
    lst = [0 for _ in range(N + 1)]
    for _ in range(M):
        a, b = map(int, input().split())
        lst[a] = b

    for i in range(N//2, 0, -1):
        if i*2 <= N:
            lst[i] += lst[i*2]
        if i*2+1 <= N:
            lst[i] += lst[i*2+1]
        if lst[L]:
            break
    print('#{} {}'.format(t+1, lst[L]))
