n = int(input())

def dice(num,s):
    if num == n:
        print(s)
        return
    for i in range(1,7):
        if str(i) in s:
            continue
        else:
            dice(num+1,s+str(i))

dice(0,'')