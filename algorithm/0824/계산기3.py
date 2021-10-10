for t in range(10):
    num = int(input())
    n = input().rstrip()
    result = ''
    stack = []
    for i in n:
        if i.isdecimal():
            result += i
        else:
            if i == '(':
                stack.append(i)
            elif i == '*':
                while stack and stack[-1] == '*':
                    result += stack.pop()
                stack.append(i)
            elif i == '+':
                while stack and stack[-1] != '(':
                    result += stack.pop()
                stack.append(i)
            elif i == ')':
                while stack and stack[-1] != '(':
                    result += stack.pop()
                stack.pop()
    while stack:
        result += stack.pop()
    for i in result:
        if i.isdecimal():
            stack.append(int(i))
        elif i == '+':
            n1 = stack.pop()
            n2 = stack.pop()
            stack.append(n2 + n1)
        elif i == '*':
            n1 = stack.pop()
            n2 = stack.pop()
            stack.append(n2 * n1)
    print('#{} {}'.format(t+1,stack.pop()))