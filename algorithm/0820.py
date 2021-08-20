import time

def map_print(ny,nx): # @
    for i in range(100): print(end = ' ')
    print()
    for y in range(7):
        for x in range(10) :
            if (y,x) == (ny,nx):
                print("@",end='')
            else :
                print(MAP[y][x],end ='')
        print()

    time.sleep(0.7)

def dfs(y,x):
    if MAP[y][x] == '#': return
    if visited[y][x] == 1 : return
    visited[y][x] = 1
    map_print(y,x)
    dfs(y-1,x)
    map_print(y, x)
    dfs(y+1,x)
    map_print(y, x)
    dfs(y,x-1)
    map_print(y, x)
    dfs(y,x+1)
    map_print(y, x)
    return

MAP = [
    "##########",
    "#_#___#__#",
    "#_#_#_#_##",
    "#_#_#_#__#",
    "#_#_#_#_##",
    "#___#____#",
    "##########",
]
visited = [
    [0 for _ in range(10)] for _ in range(7)
]

dfs(1,1)