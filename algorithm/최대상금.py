import sys
sys.stdin= open('input.txt', "r")
for t in range(int(input())):
    num, n = input().split()
    n = int(n)
    N = len(num)
    now = set([num])
    next = set()
    for _ in range(n):
        while now:
            s = now.pop()
            s = list(s)
            for i in range(N):
                for j in range(i+1,N):
                    s[i],s[j] = s[j],s[i]
                    next.add(''.join(s))
                    s[i], s[j] = s[j], s[i]
        now,next = next,now

    print('#{} {}'.format(t+1,max(map(int,now))))
