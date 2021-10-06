lst = [4,7,2,1,8,5]

def merge_sort(s, e ):
    if s == e :
        return
    mid = (s + e ) // 2
    merge_sort(s,mid) # 왼쪽 부분 정렬
    merge_sort(mid+1, e) # 오른쪽 부분 정렬

    # merge 해주기
    # left [s~mid]     [s : mid + 1]    / right [mid+1 ~ e]     [mid + 1 : e + 1]
    a = s
    b = mid+1
    res = []
    while a <= mid and b <= e :
        if lst[a] <= lst[b] :
            res.append(lst[a])
            a += 1
        elif lst[b] < lst[a] :
            res.append(lst[b])
            b += 1
    while a <= mid :
        res.append(lst[a])
        a += 1
    while b <= e :
        res.append(lst[b])
        b += 1

    # res -> lst 에 복사
    t = 0
    for i in range(s, e + 1) : # [s ~ e]
        lst[i] = res[t]
        t += 1

    print(lst[s:e + 1])

merge_sort(0,5) # [s ~ e]