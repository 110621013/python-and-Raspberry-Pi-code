import RPi.GPIO as gpio
import time

while True:
    gpio.setmode(gpio.BOARD)
    gpio.setup([13,],gpio.OUT,initial=gpio.HIGH)
    try:
        #req = urllib.request.Request('https://google.com')
        #urllib.request.urlopen(req)
        gpio.output([13,],gpio.HIGH)
        print('high')
        time.sleep(0.01)
        gpio.output([13,],gpio.LOW)
        print('low')
        time.sleep(0.2)

    except KeyboardInterrupt:
        break
#    except:
#        time_now = time.strftime("%Y/%m/%d %H:%M:%S")
#        with open(logfile,"a+") as f:
#            f.write(time_now + " " + "Pi Start now!!!" + "\n")
#            f.close()
    finally:
        gpio.cleanup()


#GPIO.setmode(GPIO.BOARD) or GPIO.setmode(GPIO.BCM)
