def func(level,s):
    global cnt
    if level ==5:
        if 'AAA' not in s and 'BBB' not in s and 'CCC' not in s:
            print(s)
            cnt += 1
        return
    for i in arr:
        func(level +1,s+i)


arr = ['A','B','C']
cnt = 0
func(0,'')
print(cnt)