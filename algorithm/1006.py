arr1 = [1,3,3,7]
arr2 = [2,3,4,6]
res = []
a = 0
b = 0
while a < len(arr1) and b < len(arr2):
    if arr1[a] >= arr2[b]:
        res.append(arr2[b])
        b+=1
    else:
        res.append(arr1[a])
        a+=1
print(res)