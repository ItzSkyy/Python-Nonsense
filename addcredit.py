import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BOARD)
GPIO.setup(12, GPIO.OUT)
GPIO.output(12,1)
time.sleep(1)
GPIO.output(12,0)

#run following pins
#Pin2 Pin 12 Pin 6
# PWR  SIG    GND
