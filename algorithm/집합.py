x = [0]*21
m = int(input())
for _ in range(m):
    com = list(input().split())
    if com[0] == 'add':
        x[int(com[1])] = 1
    elif com[0] == 'remove':
        x[int(com[1])] = 0
    elif com[0] == 'check':
        print(x[int(com[1])])
    elif com[0] == 'toggle':
        if x[int(com[1])] == 0:
            x[int(com[1])] =1
        else:
            x[int(com[1])] = 0
    elif com[0] == 'all':
        x = [1]*21
    elif com[0] == 'empty':
        x = [0] * 21