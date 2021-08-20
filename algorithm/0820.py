lst = [5,3,2,7,9,8,6]

for i in range(len(lst)):
    for j in range(i,len(lst)):
        if lst[i] > lst[j]:
            lst[i], lst[j] = lst[j], lst[i]
print(lst)