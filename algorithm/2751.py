import sys
sys.stdin = open('../1028/input.txt', 'r')
import sys
res = [0]*10001
for t in range(int(input())):
    n = int(sys.stdin.readline())
    res[n]+= 1
for i in range(1,10001):
    if res[i]:
        for _ in range(res[i]):
            print(i)