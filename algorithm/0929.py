import sys
sys.stdin = open("input.txt", "r")

solve = {
    '0001101' : 0,
    '0011001' : 1,
    '0010011' : 2,
    '0111101' : 3,
    '0100011' : 4,
    '0110001' : 5,
    '0101111' : 6,
    '0111011' : 7,
    '0110111' : 8,
    '0001011' : 9
}

for t in range(1,int(input())+1):
    N,M = map(int,input().split())
    code = []
    res = []
    for _ in range(N):
        code.append(input().rstrip())
    pw = []
    for y in range(N):
        if len(pw):
            break
        for x in range(M-1,-1,-1):
            if code[y][x] == '1':
                pw.append(code[y][x-55:x+1])
                break
    for i in range(0,56,7):
        res.append(solve[pw[0][i:i+7]])

    a = (res[0] + res[2] + res[4] + res[6])*3 + \
            (res[1]+res[3]+res[5]) + res[7]
    if not a % 10:
        print('#{} {}'.format(t,sum(res)))
    else:
        print('#{} 0'.format(t))