def rotate(lst):
    backup = lst[-1]
    for i in range(4, 0 - 1, -1):
        lst[i + 1] = lst[i]
    lst[0] = backup

lst = [3,4,7,9,8,5]
for i in range(3):
    rotate(lst)
    print(lst)