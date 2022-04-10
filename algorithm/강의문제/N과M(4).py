lst = [1, 2, 3, 4, 5]
res = set()


def f(level, path):
    if level == len(lst):
        return
    res.add(path)
    f(level + 1, path + f'{lst[level]}')
    res.add(path)
    f(level + 1, path)


f(0, '')
print(sorted(res))
