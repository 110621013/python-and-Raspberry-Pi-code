import time
import RPi.GPIO as GPIO

def doReMi():
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(12, GPIO.OUT)
    p = GPIO.PWM(12, 50)
    p.start(1)

    print("Do")
    p.ChangeFrequency(523)
    time.sleep(1)

    print("Re")
    p.ChangeFrequency(587)
    time.sleep(1)
   
    print("Mi")
    p.ChangeFrequency(659)
    time.sleep(1)

    p.stop()
    GPIO.cleanup()

doReMi()




#import time
#import RPi.GPIO as GPIO

#GPIO.setmode(GPIO.BOARD)
#GPIO.setup(12, GPIO.OUT)
#GPIO.output(12,True)
#time.sleep(3)
#GPIO.output(12,False)
######################################
import time
import RPi.GPIO as GPIO

pin_vo=12
pin_li=13

GPIO.setmode(GPIO.BOARD)
GPIO.setup(pin_vo, GPIO.OUT)
GPIO.setup(pin_li, GPIO.OUT)

def beep(bees):
    GPIO.output(pin_vo,GPIO.HIGH)
    time.sleep(bees)
    GPIO.output(pin_vo,GPIO.LOW)

def bling(blis):
    GPIO.output(pin_li,True)
    time.sleep(blis)
    GPIO.output(pin_li,False)

def act(bees,blis,sleeps,totals):
    for i in range(totals):
        beep(bees)
        bling(blis)
        time.sleep(sleeps)
    
act(0.5,0.5,0.5,2)

GPIO.cleanup()

###############################
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BOARD)
GPIO.setup(12, GPIO.OUT)
 
p = GPIO.PWM(12, 0.5)
p.start(1)
input('点击回车停止：')   # 在 Python 2 中需要使用 raw_input
p.stop()
GPIO.cleanup()