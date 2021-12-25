cnt = 0
for t in range(int(input())):
    a = 1
    n = input()
    lst = []
    for i in range(len(n)):
        if n[i] not in lst:
            lst.append(n[i])
        elif n[i] != n[i-1]:
            a = 0
            break
    if a:
        cnt += 1
print(cnt)
