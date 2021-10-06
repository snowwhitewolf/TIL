lst = [1,2,5,7,15,20,300] # 정렬된 데이터

ans = 0
def binary_search(s, e, target) :
    global ans
    if s > e :
        ans = - 1
        return
    mid = (s + e) // 2
    if lst[mid] == target :
        ans = mid
        return
    elif target < lst[mid] : # s target mid e
        binary_search(s,mid - 1)
    elif lst[mid] < target : # s mid target e
        binary_search(mid + 1, e)

    return 