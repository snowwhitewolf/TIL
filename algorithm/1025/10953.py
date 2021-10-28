import sys
sys.stdin = open('../1028/input.txt', 'r')

for t in range(int(input())):
    A,B = map(int,input().split())
    print('Case #{}: {} + {} = {}'.format(t+1,A,B,A+B))
