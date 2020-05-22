numm = list(input("輸入數字轉進位啦!(接受大寫英文字母代碼表示法) :"))
inn = int(input("輸入數字進位制:"))
out = int(input("輸出數字進位制:"))

num=0
max=0
for i in range(len(numm)):
    if ord(numm[i])>=65 and ord(numm[i])<=90:
        numm[i]=ord(numm[i])-55
    numm[i]=int(numm[i])
    if max<numm[i]:
        max=numm[i]
    num=num+numm[i]*inn**(len(numm)-i-1)

while max>inn:
    print("進位制數<=數字,不合理,重新輸入!!")
    numm = list(input("輸入數字轉進位啦!(接受大寫英文字母代碼表示法) :"))
    inn = int(input("輸入數字進位制:"))
    out = int(input("輸出數字進位制:"))
    for i in range(len(numm)):
        if ord(numm[i])>=65 and ord(numm[i])<=90:
            numm[i]=ord(numm[i])-55
        numm[i]=int(numm[i])
        if max<numm[i]:
            max=numm[i]
        num=num+numm[i]*inn**(len(numm)-i-1)


usoo = []
while num>=out:
        #num =int(num/out)
        print(num)
        usoo.append(num%out) 
        num =int(num/out)
usoo.append(num%out)
print(usoo)

jinweinum = ""
for k in range(len(usoo)):
    if usoo[len(usoo)-k-1]>=10:
        usoo[len(usoo)-k-1]=chr(usoo[len(usoo)-k-1]+55)
    jinweinum += str(usoo[len(usoo)-k-1])
print(jinweinum)
