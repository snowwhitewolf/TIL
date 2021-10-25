import sys
sys.stdin = open('input.txt', 'r')

res = [0]*10001
for t in range(int(input())):
    n = int(input())
    res[n]+= 1
for i in range(1,10001):
    if res[i]:
        for _ in range(res[i]):
            print(i)