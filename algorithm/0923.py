N,K = map(int,input().split())
A = list(map(int,input().split()))
robot = [0 for _ in range(2*N)]
cnt = 0
while True:
    # 1번째 단계
    cnt += 1
    next = A[-1]
    del A[-1]
    A.insert(0,A.pop())
    next = robot[-1]
    del robot[-1]
    robot.insert(0, next)
    if robot[N-1]:
        robot[N-1]-=1

    # 2번째 단계
    for i in range(N-2,-1,-1):
        if robot[i] and A[i+1] and robot[i+1]==0:
            robot[i]-=1
            robot[i+1]+=1
            A[i+1] -= 1
    if robot[N - 1]:
        robot[N - 1] = 0

    # 3번째 단계
    if A[0] and robot[0]==0:
        robot[0] = 1
        A[0] -= 1

    # 4번째 단계
    if A.count(0) >= K:
        break

print(cnt)