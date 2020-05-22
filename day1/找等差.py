
num = (input("四個等差數字:").split(' '))
#print(num[3])

delta = []
mark="ok"
d=int(num[1])-int(num[0])
for z in range(3):
    delta.append(int(num[z+1])-int(num[z]))
#print(delta,z)
for a in range(len(delta)):
    for b in range(a+1,len(delta)):
        c=delta[b]-delta[a]
        if c != 0:
            mark="gg"

if mark=="gg":
    print("這不是等差數列")
elif mark=="ok":
    print("這是等差數列,公差為",d)
else:
    print("程式有問題")


#if a[0]==a[1] and a[1]==a[2] and a[0]==a[2]:
#    c=num[3]+a[0]
#    num.append(c)
#    print(num)
#if b[0]==b[1] and b[1]==b[2] and b[0]==b[2]:
#    c=num[3]*b[0]
 #   num.append(c)
 #   print(num)
#################################################