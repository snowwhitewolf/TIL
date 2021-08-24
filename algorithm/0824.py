
def func(l,n):
    if l == n-1:
        print(res)
    res.append(dice[0])
    func(l +1,n)
    res.append(dice[1])
    func(l +1,n)
    res.append(dice[2])
    func(l +1,n)
    res.append(dice[3])
    func(l +1,n)
    return
n = int(input())
dice = [1,2,3,4]
res = []
func(0,n)
