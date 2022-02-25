# 9*9 배열이 주이짐
# 가로 세로 네모를 따져서 하나라도 안되면 바로 리턴해서 끝냄
# 가로 세로 네모를 각각의 함수로 만들어서 검증

for t in range(int(input())):
    lst = [list(map(int, input().split())) for _ in range(9)]
    print(lst)
