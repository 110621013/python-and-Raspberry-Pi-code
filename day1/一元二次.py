#x=input("輸入x")
try:
    a, b, c = (int(x) for x in input().split(' '))
#print(a,b,c)
#print(a+b)

    if b**2-4*a*c > 0:
        x1=(-b+(b**2-4*a*c)**(1/2))/(2*a)
        x2=(-b-(b**2-4*a*c)**(1/2))/(2*a)
        print("Two different roots x1=",x1,", x2=",x2)
    elif b**2-4*a*c == 0:
        x=(-b)/(2*a)
        print("Two same roots x=",x)
    else :
        print("No real root")
except ValueError:
    print("666")
except GeneratorExit:
    print("666")