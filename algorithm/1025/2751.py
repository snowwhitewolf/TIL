import sys
sys.stdin = open('input.txt', 'r')

res = []
for t in range(int(input())):
    res.append(int(input()))
res.sort()
for i in range(len(res)):
    print(res[i])