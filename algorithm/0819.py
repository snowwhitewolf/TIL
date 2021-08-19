def func(level, s):
    if level == 3:
        print(s)
        return
    func(level+1, s+'L')
    func(level + 1, s + 'M')
    func(level + 1, s + 'R')
    return

func(0,'')