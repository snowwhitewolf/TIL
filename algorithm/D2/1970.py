'''
금액이 주어짐
큰돈부터 거슬러 주고 그 돈만큼 빼면서 반복
'''


T = int(input())

for t in range(1,T+1):
    cost = int(input())
    change = [50000, 10000, 5000, 1000, 500, 100, 50, 10]
    change_num = [0,0,0,0,0,0,0,0]
    while cost >= 10:
        if cost >= change[0]:
            cost -= change[0]
            change_num[0] += 1
        elif cost >= change[1]:
            cost -= change[1]
            change_num[1] += 1
        elif cost >= change[2]:
            cost -= change[2]
            change_num[2] += 1
        elif cost >= change[3]:
            cost -= change[3]
            change_num[3] += 1
        elif cost >= change[4]:
            cost -= change[4]
            change_num[4] += 1
        elif cost >= change[5]:
            cost -= change[5]
            change_num[5] += 1
        elif cost >= change[6]:
            cost -= change[6]
            change_num[6] += 1
        elif cost >= change[7]:
            cost -= change[7]
            change_num[7] += 1
        elif cost >= change[8]:
            cost -= change[8]
            change_num[8] += 1
    print(f'#{t}')
    print(*(change_num))