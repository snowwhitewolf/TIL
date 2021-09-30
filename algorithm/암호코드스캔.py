import sys
sys.stdin = open("input.txt", "r")

solve = {
    '211':0,
    '221':1,
    '122':2,
    '411':3,
    '132':4,
    '231':5,
    '114':6,
    '312':7,
    '213':8,
    '112':9
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
def func(f3, f2, f1):
    a = min(f3,f2,f1)
    f1 //= a
    f2 //= a
    f3 //= a
    return str(f3)+str(f2)+str(f1)

for t in range(int(input())):
    N, M = map(int, input().split())
    code = [input() for _ in range(N)]
    lst = [''] * N
    for y in range(N):
        for x in range(M):
            lst[y] += MAP[code[y][x]]
    result = []
    visited = []
    res = 0
    for y in range(N):
        f1 = 0
        f2 = 0
        f3 = 0
        for x in range(M*4-1, -1, -1):
            if f2 == 0 and f3 == 0 and lst[y][x] == '1':
                f1 += 1
            elif f1 > 0 and f3 == 0 and lst[y][x] == '0':
                f2 += 1
            elif f1 > 0 and f2 > 0 and lst[y][x] == '1':
                f3 += 1

            if f1 and f2 and f3 and lst[y][x] == '0':
                result.append(solve[func(f3, f2, f1)])
                f1 = 0
                f2 = 0
                f3 = 0

            if len(result) == 8:
                result = result[::-1]
                value = (result[0] + result[2] + result[4] + result[6]) * 3 + \
                        (result[1] + result[3] + result[5]) + result[7]
                if value % 10 == 0 and result not in visited:
                    res += sum(result)
                visited.append(result)
                result = []

    print('#{} {}'.format(t+1, res))