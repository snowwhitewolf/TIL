def cal(a):
    stack = []
    for i in a:
        if i.isdecimal():
            stack.append(int(i))
        elif i == '+':
            if len(stack) >= 2:
                n1 = stack.pop()
                n2 = stack.pop()
                if type(n1) != int or type(n2) != int:
                    return 'error'
                stack.append(n2 + n1)
            else:
                return 'error'
        elif i == '-':
            if len(stack) >= 2:
                n1 = stack.pop()
                n2 = stack.pop()
                if type(n1) != int or type(n2) != int:
                    return 'error'
                stack.append(n2 - n1)
            else:
                return 'error'
        elif i == '*':
            if len(stack) >= 2:
                n1 = stack.pop()
                n2 = stack.pop()
                if type(n1) != int or type(n2) != int:
                    return 'error'
                stack.append(n2 * n1)
            else:
                return 'error'
        elif i == '/':
            if len(stack) >= 2:
                n1 = stack.pop()
                n2 = stack.pop()
                if type(n1) != int or type(n2) != int:
                    return 'error'
                stack.append(n2 // n1)
            else:
                return 'error'
        elif i == '.':
            if len(stack) == 1:
                return stack.pop()
            else:
                return 'error'

for t in range(int(input())):
    n = input().split()
    if str(cal(n)).isdecimal():
        print('#{} {}'.format(t+1,cal(n)))
    else:
        print('#{} error'.format(t + 1))