for t in range(int(input())):
    N = int(input())
    lst = []
    num = ''
    if N <= 20:
        lst = list(input().split())
        num += ''.join(lst)
    elif N%20 == 0:
        for x in range(N//20):
            lst = list(input().split())
            num += ''.join(lst)
    else:
        for x in range(N//20+1):
            lst = list(input().split())
            num += ''.join(lst)
    i = 0
    while True:
        if str(i) in num:
            i += 1
        else:
            break
    print('#{} {}'.format(t + 1, i))