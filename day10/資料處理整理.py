filename="day10/NCU_ATM_201807051204.txt"
savefile="day10/solarge.txt"
#f=open(filename,"r")
#print(f.read())

with open(filename,"r") as in_file:
    with open(savefile,"a+") as out_file:
        a1,a2,change=0,0,0
        a=[]

        data=in_file.read()
        for i in range(len(data)):#len(data)
            if ord(data[i])>=97 and ord(data[i])<=102:
                w=int(ord(data[i])-87)
            elif data[i]==",":
                w=0
            else :
                w=int(data[i])
        
            if i%3==0:
                a1=w
            elif i%3==1:
                a2=w
            elif i%3==2:
                a.append(a1*16+a2)

        s=""
        for k in range(int(len(a)/32)):
            s+="["
            for l in range(32):
                s+=str(a[k*32+l])
                if l != 31:
                    s+=", "
            s+="]\n"
            print(s)
            out_file.write(s)
            s=""
    out_file.close()
in_file.close()