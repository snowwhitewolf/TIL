'''
숫자 N이 주어짐
각각 2 3 5 7 11 로 나누어질때 나누고 나눈값을 반복
'''


T = int(input())

for t in range(1,T+1):
    N = int(input())
    n = [0,0,0,0,0]
    while N !=1:
        if N%2 == 0:
            n[0] += 1
            N = N/2
        elif N%3 == 0:
            n[1] += 1
            N = N/3
        elif N%5 == 0:
            n[2] += 1
            N = N/5
        elif N%7 == 0:
            n[3] += 1
            N = N/7
        elif N%11 == 0:
            n[4] += 1
            N = N/11
       
    print(f'#{t}', end = ' ')
    print(*(n))
 