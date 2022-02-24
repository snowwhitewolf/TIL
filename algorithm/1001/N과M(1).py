N, M = map(int, input().split())


def f(level, s):
    if level == M:
        print(s.lstrip())
        return
    for i in range(1, N+1):
        if str(i) not in s:
            f(level+1, s+f' {str(i)}')
        else:
            continue


f(0, '')
