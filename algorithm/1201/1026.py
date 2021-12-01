N = int(input())
A = list(map(int,input().split()))
B = list(map(int,input().split()))
res = 0
A.sort()
B.sort(reverse=True)
for i in range(N):
    res += A[i] * B[i]
print(res)