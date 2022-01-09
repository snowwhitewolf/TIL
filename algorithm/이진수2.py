for t in range(int(input())):
    n = float(input())
    res = []
    def f(num,res):
        if num == 1.0:
            return res
    while len(res)<=13:
        n *= 2
        if n > 1:
            n -= 1
            res += '1'
        elif n == 1.0:
            res += '1'
            break
        else:
            res += '0'
    if len(res)<= 12:
        print('#{} {}'.format(t+1,res))
    else:
        print('#{} overflow'.format(t+1))