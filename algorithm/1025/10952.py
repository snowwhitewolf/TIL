import sys
sys.stdin = open('../1026/input.txt', 'r')

while True:
    A,B = map(int,input().split())
    if A == 0 and B == 0:
        break
    print(A+B)