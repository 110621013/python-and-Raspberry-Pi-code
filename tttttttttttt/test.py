x=input("gogo")
list(x)
b = False
    
for i in range(len(x)):
    for j in range(len(x)):
        if i == j:
            continue
        else:
            if x[i]==x[j]:
                b=True
    if b:
        print(")")
    else:
        print("(")
    b=False