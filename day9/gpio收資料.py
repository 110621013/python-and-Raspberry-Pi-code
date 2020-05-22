import serial

ser=serial.Serial(port='/dev/ttyAMA0',baudrate=19200,bytesize=8,parity='N',stopbits=1,timeout=12) 
#port開端口,baudrate,bytesize不變
a=ser.read(27)
print("a的序列(27個)")
for i in range(27):
    print(a[i])
print("------------------------------------------------------------")
for i in range(6):
    print("a",i,"=",a[i]," a0~a5用以驗證")

b=[]
print("temp=",(a[6]*256+a[7]-255)/10)#溫度為a6*256+a7-255再除10
print("RH=",float((a[8]*256+a[9])/10))#濕度為a8*256+a9再除10

for j in range(4):
    b.append(a[2*j+10]*256+a[2*j+11])#下面四項為a(i)*256+a(i+1)
print("pressure=",b[0])
print("PM2.5=",b[1])
print("CO2=",b[2])
print("light=",b[3])

print("battery voltage=",a[18])
print("year=",a[19])
print("month=",a[20])
print("date=",a[21])
print("hour=",a[22])
print("min=",a[23])
print("sec=",a[24])

sum=0
for z in range(21):
    sum=sum+a[3+z]
sum=sum%255
if sum==a[25]:
    word="No broblem!"
else:
    word="GG"

print("checksum=",a[25],word)   #3~24 a25為驗證資料a3~a23總和%255 若不對則GG
print("End Byte=",a[26])

cc=[a[1],a[5],(a[6]*256+a[7]-255)/10,float((a[8]*256+a[9])/10),b[0],b[1],b[2],b[3],a[19],a[20],a[21],a[22],a[23],a[24],word]
print(cc)

