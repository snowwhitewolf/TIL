'''
시 끼리 더하고 분끼리 더함
시가 12이상이면 -12 분이 60 이상이면 1시간을 더하고 -60
'''



T = int(input())
for t in range(1, T+1):
    time = list(map(int, input().split()))
    h1 = time[0]
    s1 = time[1]
    h2 = time[2]
    s2 = time[3]

    extra = divmod(s1+s2,60)
    second = extra[1]
    time = (h1+h2)%12 + extra[0]
    print(f'#{t} {time} {second}')