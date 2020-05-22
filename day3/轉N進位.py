num = int(input("輸入數字轉進位啦! :"))
#in = int(input("輸入數字進位制"))
out = int(input("輸出數字進位制:"))

usoo = []
while num>out:
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