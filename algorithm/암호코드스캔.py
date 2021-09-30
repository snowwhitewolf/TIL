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
MAP = {
    '0' : '0000',
    '1' : '0001',
    '2' : '0010',
    '3' : '0011',
    '4' : '0100',
    '5' : '0101',
    '6' : '0110',
    '7' : '0111',
    '8' : '1000',
    '9' : '1001',
    'A' : '1010',
    'B' : '1011',
    'C' : '1100',
    'D' : '1101',
    'E' : '1110',
    'F' : '1111',
}

for t in range(1,int(input())+1):
    N,M = map(int,input().split())
    code = set()
    res = []
    for _ in range(N):
        a = input().strip('0')
        if a and a not in code:
            code.add(a)
    print(code)
    # print(bin(int(code[0],16)).rstrip('0'))
    # pw = ''
    # pw2 = []
    # for y in range(N):
    #     if len(pw2):
    #         break
    #     for x in range(0,M):
    #         if code[y][x] != '0':
    #             pw2.append(code[y][x])
    #         if code[y][x]=='0' and len(pw2):
    #             break
    # for i in range(len(pw2)):
    #     pw += MAP[pw2[i]]
    # for x in range(len(pw) - 1, -1, -1):
    #     if pw[x] == '1':
    #         if len(pw[0:x + 1]) >=56:
    #             pw = pw[x-55:x+1]
    #         else:
    #             pw= pw[0:x + 1]
    #             pw = '0' * (56 - len(pw)) + pw
    #         break
    # for i in range(0,56,7):
    #     res.append(solve[pw[i:i+7]])
    #
    # a = (res[0] + res[2] + res[4] + res[6])*3 + \
    #         (res[1]+res[3]+res[5]) + res[7]
    # if not a % 10:
    #     print('#{} {}'.format(t,sum(res)))
    # else:
    #     print('#{} 0'.format(t))