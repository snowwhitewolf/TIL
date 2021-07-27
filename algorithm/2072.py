T = int(input())

numbers = []
for t in range(T):
    n = list(map(int, input().split()))
    numbers.append(n)

total = 0
for i in range(T):
    for j in range(10): 
        if numbers[i][j]%2 == 1:
            total += numbers[i][j]
    print(f'#{i+1} {total}')
    total = 0