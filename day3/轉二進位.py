num = int(input("輸入數字轉二進位啦! :"))

usoo = []
while num>=2:
        print(num)
        usoo.append(num%2) 
        num =int(num/2)
usoo.append(num%2)


jinweinum = ""
for k in range(len(usoo)):
    jinweinum += str(usoo[len(usoo)-k-1])
print(int(jinweinum))