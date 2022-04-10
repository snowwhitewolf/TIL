import sys
import itertools
from math import gcd
'''
연산을 줄이는 방법
1. 순열 리스트를 계산할 때
2. K로 나눌 때
3. 경우의 수 최대 15! = 약 13억...
'''
sys.stdin = open('input.txt', 'r')

N = int(input())
lst = [input() for _ in range(N)]
K = int(input())
res = 0
P = []
def func(cnt, num_lst):
    if cnt == N:
        P.append(num_lst)
        return  
    for i in lst:
        if i in num_lst:
            continue
        num_lst.append(i)
        func(cnt+1, num_lst)
        num_lst.pop()

func(0,[])
print(P)


# P = list(itertools.permutations(lst, N))
# total = ''
# for i in range(len(P)):
#     for j in range(N):
#         total += P[i][j]
#     if int(total) % K == 0:
#         res += 1
#     total = ''

# a = gcd(res,len(P))
# if res:
#     print("{}/{}".format(res//a,len(P)//a))
# else:
#     print('0/1')
