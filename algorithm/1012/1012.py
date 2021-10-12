a = '000011000110111011111100001100011111100001010111'
cnt =[0] * len(a)
for i in range(len(a)):
    if a[i] == '1':
        j = i
        while a[j] == '1' and j < len(a)-1:
            cnt[i] += 1
            j += 1
for i in range(len(cnt)):
    if cnt[i] == max(cnt):
        print(i)
        break