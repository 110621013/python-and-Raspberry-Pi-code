import serial
import time
import RPi.GPIO as GPIO
import numpy as np
import atexit

ser=serial.Serial(port='/dev/ttyAMA0',baudrate=57600,bytesize=8,parity='N',stopbits=1,timeout=5)
#port開端口,baudrate,bytesize不變,timeout停滯時間


def act(blis,bees):
    try:
        ifbee=beep(bees)#執行同時傳ifbee回來
        bling_pm()
        bling_t()
        ser.write(dpb_show(a[4],a[3],a[5]))
                
        if ifbee:
            time.sleep(blis-bees)
        else:
            time.sleep(blis)
        ser.flush()

    except KeyboardInterrupt:
        GPIO.cleanup()
        exit()


def beep(bees):  #若極端天氣(pm>150  t>30  t<15)則逼bees秒
    ifbee=False
    if a[5]>10 or a[4]>25:
        GPIO.output(pin_vo,True)
        time.sleep(bees)
        GPIO.output(pin_vo,False)
        ifbee=True
    return ifbee  #反應是否有休bees秒


def bling_pm():     #選pm燈亮
    if a[5]<=7 and a[5]>=0:
        GPIO.output(pin_pm_g,True)
    elif a[5]<=10 and a[5]>7:
        GPIO.output(pin_pm_y,True)
    elif a[5]>10:
        GPIO.output(pin_pm_r,True)
    else:
        print("pm怪怪")
        pass

def bling_t():     #選t燈亮
    if a[4]<=22 and a[4]>=18:
        GPIO.output(pin_t_g,True)
    elif a[4]<=25 and a[4]>=15:
        GPIO.output(pin_t_y,True)
    elif a[4]>25 or a[4]<15:
        GPIO.output(pin_t_r,True)
    else:
        print("t怪怪")
        pass


def int_show(data):
    return [int(data/255),int(data%255)]
def float_show(data):
    return [int(data*10/255),int((data*10)%255)]
def get_color(data):
    if float(data) <= 32:
        return 1
    elif float(data) <= 50 and float(data) > 32:
        return 2
    elif float(data) <= 72 and float(data) > 50:
        return 3
    elif float(data) > 72:
        return 4

def dpb_show(display1,display2,display3):              #display 123 濕溫pm
    trans=[85,218,0,14,194,
    get_color(display1),
    float_show(display1)[0],float_show(display1)[1],
    float_show(display2)[0],float_show(display2)[1],
    int_show(display3)[0],int_show(display3)[1]
    ,0,237]
    trans[12]=sum(trans[3:12])%255
    b = np.arange(len(trans),dtype=np.uint8)
    for index in range(len(trans)):
        b[index] = trans[index]
    #print(b)
    return b



n=0
ser.flush()#清掉所有暫存,或是ser.read(7000)也可

pin_vo=12
pin_pm_r=13
pin_pm_y=15
pin_pm_g=16
pin_t_r=18
pin_t_y=19
pin_t_g=21

@atexit.register
def gpio_cleanup():
    GPIO.cleanup()

while 1:
    a=ser.read(7)
    if a[1]!=0 or a[2]!=2:
        continue

    n=n+1
    print("\n\n\n第",n,"次量測")#第幾次量測

    print("a的序列3+3+1個,(開頭,你是誰,傳給誰,pm,temp,rh,gg)")
    #for i in range(7):
    #    print(a[i])
    print("------------------------------------------------------------")
    for i in range(3):
        print("a",i,"=",a[i]," a0用以驗證,a1你是誰,a2傳給誰")

    print("濕度=",(a[3]))
    print("溫度=",(a[4]))
    print("pm=",(a[5]))

    print("End Byte=",a[6])

    cc=[a[0],a[1],a[2],a[3],a[4],a[5],a[6]]
    #print(cc)
##############################################################################上面持續收

    #if a[1]==0 and a[2]==2:

    GPIO.setmode(GPIO.BOARD)

    GPIO.setup(pin_vo, GPIO.OUT)
    GPIO.setup(pin_pm_r, GPIO.OUT)
    GPIO.setup(pin_pm_y, GPIO.OUT)
    GPIO.setup(pin_pm_g, GPIO.OUT)
    GPIO.setup(pin_t_r, GPIO.OUT)
    GPIO.setup(pin_t_y, GPIO.OUT)
    GPIO.setup(pin_t_g, GPIO.OUT)
    
    act(3,0.5)
    GPIO.output(pin_pm_g,False)
    GPIO.output(pin_pm_y,False)
    GPIO.output(pin_pm_r,False)
    GPIO.output(pin_t_g,False)
    GPIO.output(pin_t_y,False)
    GPIO.output(pin_t_r,False)
