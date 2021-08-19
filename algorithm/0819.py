for t in range(int(input())):
    st = input()
    lst = []
    for i in st:
        if i == '{' or i == '}' or i == '[' or i == ']' or i == '(' or i == ')':
            lst.append(i)
    print(lst)

    def f(n):
        if lst[n] == '{' :

