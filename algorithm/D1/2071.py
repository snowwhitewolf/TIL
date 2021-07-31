T = int(input())

numbers = []
for t in range(T):
    n = list(map(int, input().split()))
    numbers.append(n)

avg =0
for i in range(T):
    for j in range(10):
        avg += numbers[i][j]
    avg = round(avg / 10)
    print(f'#{i+1} {avg}')
    avg = 0