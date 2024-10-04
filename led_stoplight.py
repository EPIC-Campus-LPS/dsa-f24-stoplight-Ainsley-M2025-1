#Green LED is 4
import RPi.GPIO as GPIO
import time
#The two lines above import GPIO and time
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(4,GPIO.OUT)
#This is setting the pin that will recieve power when the code is run
print "LED on"
#This will print out "LED on" when the LED recieves power
GPIO.output(4,GPIO.HIGH)
#This will turn on the power
time.sleep(5)
#This sets the amt of time the LED is on 
print "LED off"
#This will print when the power to the LED is stoppped 
GPIO.output(4,GPIO.LOW)
#This will turn off the power 
#Yellow LED is 22
import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(22,GPIO.OUT)
#This line sets the new pin that power will be directed too 
print "LED on"
#This will pring LED on when the light is on
GPIO.output(22,GPIO.HIGH)
#This line will direct power to go to the pin
time.sleep(1)
#This is the amt of time the pin will get power/how long the LED is on
print "LED off"
GPIO.output(22,GPIO.LOW)
#These two lines will turn off the power to the LED and print LED off when the power is cut off
#Red LED is 18
import RPi.GPIO as GPIO
import time
#These import GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(18,GPIO.OUT)
#This cahnges the pin that power is going too 
print "LED on"
GPIO.output(18,GPIO.HIGH)
#These will print LED on when the LED will recieve power and the second line turns on power to the pin
time.sleep(4)
#This is how long the LED will be on
print "LED off"
GPIO.output(18,GPIO.LOW)
#This will turn the LED off and print out LED off when it turns off power to the LED

