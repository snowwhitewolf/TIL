a=int(input("a를 입력해주세요."))
b=int(input("b를 입력해주세요."))
c=int(input("c를 입력해주세요."))

D = (b**2) - (4*a*c)

if D>0:
    r1= (-b + D**0.5)/(2*a)
    r2 = (-b - D**0.5)/(2*a)
    print(f'실근이고, {r1} 와 {r2} 입니다.')
elif D==0:
    x = -b / 2*a
    print(f'"중근이고, 해는 {x}입니다."')
else:
    r1= (-b + D**0.5)/(2*a)
    r2 = (-b - D**0.5)/(2*a)
    print(f'허근이고, 해는 {r1} 와 {r2} 입니다.')