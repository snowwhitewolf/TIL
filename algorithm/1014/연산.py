from collections import deque

import sys
sys.stdin = open("text.txt","r")

def bfs(n,m) :
    # 큐 / visited 큐에 재등록 방지
    qu = deque()
    visited = [0] * 1000001

    # 시작 노드 큐에 등록하기(방문 예약)
    visited[n] = 1 # 재등록 방지
    qu.append((n, 0)) # (숫자, level) level : 연산 횟수

    # BFS
    while qu :
        num , level = qu.popleft()
        if num == m : # BFS 중에 m 나옴
            return level # m 이 처음 탐색되었을때 연산횟수를 리턴 ----> 최소 연산횟수를 구할수 있다.

        # next 노드 큐에 등록 (방문예약) -> for 문으로 묶기
        if 1 <= num+1 <= 1000000 and visited[num+1] == 0:
            visited[num+1] = 1
            qu.append((num+1, level + 1))
        if 1 <= num - 1 <= 1000000 and visited[num-1] == 0:
            visited[num-1] = 1
            qu.append((num-1, level + 1))
        if 1 <= num * 2 <= 1000000 and visited[num * 2] == 0:
            visited[num*2] =1
            qu.append((num*2, level + 1))
        if 1 <= num - 10 <= 1000000 and visited[num - 10] == 0 :
            visited[num-10] = 1
            qu.append((num-10, level + 1))

    return - 1

T = int(input())
for tc in range(1,T+1) :
    N,M = map(int, input().split())
    ret = bfs(N,M)
    print("#{} {}".format(tc, ret))