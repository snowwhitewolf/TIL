def dice(level):
    global n
    if level == n:
        print(res)
        return
    for i in range(1,5):
        if al[i-1] == 0:
            res.append(i)
            al[i-1] = 1
            dice(level+1)
            al[i-1]=0
            res.pop()
        else:
            continue
    return

n = int(input())
res = []
al = [0,0,0,0]
dice(0)