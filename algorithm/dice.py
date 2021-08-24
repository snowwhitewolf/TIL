def dice(level):
    global n
    if level == n:
        print(res)
        return
    for i in range(4):
        res.append(i+1)
        dice(level+1)
        res.pop()
    return

n = int(input())
res = []
dice(0)