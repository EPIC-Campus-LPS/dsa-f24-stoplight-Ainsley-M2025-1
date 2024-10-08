import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
GPIO.setup(12, GPIO.IN)
while True:
    if GPIO.input(12) == 0:
        GPIO.setmode(GPIO.BCM)
        GPIO.setwarnings(False)
        GPIO.setup(23, GPIO.OUT)
        print("LED on")
        GPIO.output(23, GPIO.HIGH)
        time.sleep(5)
        GPIO.setup(16, GPIO.OUT)
        print("LED on")
        GPIO.output(16, GPIO.HIGH)
        time.sleep(1)
        print("LED off")
        GPIO.output(23, GPIO.LOW)
        time.sleep(4)
        GPIO.output(16, GPIO.LOW)
        print("LED off")
        break
