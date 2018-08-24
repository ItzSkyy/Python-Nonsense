import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BOARD)
GPIO.setup(16, GPIO.OUT)
GPIO.output(16,1)
time.sleep(1)
GPIO.output(16,0)

#run following pins
#Pin4 Pin 16 Pin 9
# PWR  SIG    GND
