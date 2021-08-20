for t in range(int(input())):
    h , w = map(int,input().split())
    d = []
    for i in range(h):
        d.append(list(map(int,input().split())))
    ans = 0
    total = []
    for y in range(h):
        for x in range(w):
            total = []
            for yy in range(h-y):
                for xx in range(w-x):
                    total.append(d[y+yy][x+xx])
            print(total)
            if sum(total) > ans:
                ans = sum(total)

    print(ans)