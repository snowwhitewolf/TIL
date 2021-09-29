import sys
T = int(sys.stdin.readline())

S = 1 << 21
de = -1
for _ in range(T):
    temp = sys.stdin.readline().split()
    if len(temp) == 2:
        cmd = temp[0]
        x = int(temp[1])
    else :
        cmd = temp[0]

    if cmd == "add":
        S |= (1<<x)
    elif cmd == "remove":
        S &= ~(1<<x)
    elif cmd == "check":
        if S & (1<<x)==0:
            print(0)
        else:
            print(1)
    elif cmd == "toggle":
        S ^= (1<<x)
    elif cmd == "all":
        S = 1 << 21 -1
    elif cmd == "empty":
        S = 1 << 21