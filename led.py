#Code written for IBM Call for code 2K22 (SwachBin)
import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(27,GPIO.OUT)
GPIO.setup(5,GPIO.OUT)
GPIO.setup(12,GPIO.OUT)
GPIO.setup(13,GPIO.OUT)
GPIO.setup(24,GPIO.OUT)
GPIO.setup(23,GPIO.OUT)
res=1

if res==1:
        print ('Inside')
        GPIO.output(12,GPIO.HIGH)
        print ('B1 Glows 12')
        time.sleep(4)
        GPIO.output(12,GPIO.LOW)
        #time.sleep(2)
       
        GPIO.output(24,GPIO.HIGH)
        print ('B2 Glows 24')
        time.sleep(4)
        GPIO.output(24,GPIO.LOW)
       
        GPIO.output(23,GPIO.HIGH)
        print ('Red Glows 23')
        time.sleep(4)
        GPIO.output(23,GPIO.LOW)
       
        GPIO.output(27,GPIO.HIGH)
        print ('w1 Glows 27')
        time.sleep(4)
        GPIO.output(27,GPIO.LOW)
        
        GPIO.output(5,GPIO.HIGH)
        print ('w2 Glows 05')
        time.sleep(4)
        GPIO.output(5,GPIO.LOW)
        
        GPIO.output(13,GPIO.HIGH)
        print ('w3 Glows 26')
        time.sleep(4)
        GPIO.output(13,GPIO.LOW)