queue = [3,7,2,1,5,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
front = 0
rear = 5

while front != rear:
    ret = queue(front)
    front += 1
    print(ret)