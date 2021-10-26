n = int(input())
lst = [0] * 1001
for i in range(1,100):
    lst[i] = 1
for i in range(100,1000):
    if int(str(i)[0]) - int(str(i)[1]) == int(str(i)[1]) - int(str(i)[2]):
        lst[i] = 1
print(lst[1:n+1].count(1))