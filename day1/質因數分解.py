num = int(input("輸入數字啦! :"))

alist = []
j=0
for i in range(num): #i是0~num-1
    if num%(i+2) == 0:
        alist.append((i+2))
    while num%(i+2) == 0:
        num=num/(i+2)
        j+=1
    if j!=0:
        alist.append(j)
    j=0
#print(alist)
#print(len(alist))
total = ""
for k in range(len(alist)):
    if k%2 == 0 :
        total += "*"
        total += str(alist[k])
        #print (alist[k])
    if k%2 == 1 and alist[k]!=1 :
        total += "^"
        total += str(alist[k])
        #print ("^",alist[k])

total=total.lstrip("*")
print (total)
#for k in range(len(answer)):
#    total += str(answer[len(answer)-k-1])
#print(total)
