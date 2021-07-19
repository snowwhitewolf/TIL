a = int(input())
i = 0
total = 0

if a > 1000:
    print('10000을 넘는 숫자입니다.')
else:
    while i <= a:
        total += i
        i += 1
    print(total)