for t in range(int(input())):
    V, E = map(int, input().split())
    lst = list([0 for _ in range(V)] for _ in range(V))
    for e in range(E):
        a, b = map(int, input().split())
        lst[a-1][b-1] = 1

    S, G = map(int, input().split())
    print(lst)