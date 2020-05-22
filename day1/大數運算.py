while True: 
    
    num = input("大數字運算(請輸入a +-*/ b的形式):").split(' ')
    a=int(num[0])
    b=str(num[1])
    c=int(num[2])
    if b == "+":
        break
    elif b == "-": 
        break
    elif b == "*":
        break
    elif b == "/":
        break
    print("母湯亂用運算符號!!")
################ a, b, c = (int(x) for x in input().split(' '))可作相同事情
d=0
print (b)

if b == "-":
    if a<c:
        d=c
        c=a
        a=d
        d="-"

    alist=[]
    while a!=0:
       alist.append(int(a)-int(a/10)*10)
       a=int(a/10)
    print(alist)

    clist=[]
    while c!=0:
       clist.append(int(c)-int(c/10)*10)
       c=int(c/10)
    print(clist)

    answer=[]
    b=0

    for j in range(len(alist)-len(clist)):
       clist.append(0)
    print(clist)

    for i in range(len(alist)):
        if alist[i]>=clist[i]:
            answer.append(alist[i]-clist[i])
        else :
            answer.append(10+alist[i]-clist[i])
            alist[i+1]-=1
    print(answer[:])

    total = ""
    if d == "-":
        total += "-"
    for k in range(len(answer)):
        total += str(answer[len(answer)-k-1])

    print(total)

elif b == "+":
    alist=[]
    while a!=0:
       alist.append(int(a)-int(a/10)*10)
       a=int(a/10)
    print(alist)

    clist=[]
    while c!=0:
       clist.append(int(c)-int(c/10)*10)
       c=int(c/10)
    print(clist)

    answer=[]
    b=0

    for j in range(len(alist)-len(clist)):
        clist.append(0)
    print(clist)
    for j in range(len(clist)-len(alist)):
        alist.append(0)
    print(alist)

    for i in range(len(alist)):

        if alist[i]+clist[i]>=10:
            answer.append(alist[i]+clist[i]-10)
            alist[i+1]+=1
        else :
            answer.append(alist[i]+clist[i])
    print(answer[:])

    total = ""
    for k in range(len(answer)):
        total += str(answer[len(answer)-k-1])

    print(total)

elif b == "*":
    alist=[]
    while a!=0:
       alist.append(int(a)-int(a/10)*10)
       a=int(a/10)
    print(alist)

    clist=[]
    while c!=0:
       clist.append(int(c)-int(c/10)*10)
       c=int(c/10)
    print(clist)

    chan = 0
    singlege = 0
    ge = 0
    for i in range(len(alist)):
        for j in range(len(clist)):
            chan = alist[i]*clist[j]*10**j
            singlege=singlege+chan
        ge=ge+singlege*10**i
        singlege=0

    print(ge)

elif b == "/":
    print("結果為去掉小數點之整數")
    alist=[]
    while a!=0:
       alist.append(int(a)-int(a/10)*10)
       a=int(a/10)
    print(alist)
    clist=[]
    while c!=0:
       clist.append(int(c)-int(c/10)*10)
       c=int(c/10)
    print(clist)

    answer=[]
    b=0

    for j in range(len(alist)-len(clist)):
       clist.append(0)
    print(clist)

    for i in range(len(alist)):
        if alist[i]>=clist[i]:
            answer.append(alist[i]-clist[i])
        else :
            answer.append(10+alist[i]-clist[i])
            alist[i+1]-=1
    print(answer[:])

    total = ""
    if d == "-":
        total += "-"
    for k in range(len(answer)):
        total += str(answer[len(answer)-k-1])

    print(total)



