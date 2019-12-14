import RPi.GPIO as GPIO
import time
from wia import Wia

wia = Wia()
wia.access_token = "d_sk_4T10bCtctB6mRCSK2QqdmGo2"

#This function will be called every time there is a data change on the GPIO channel 17
def callback(channel):
 if GPIO.input(channel):
	print "Plant Needs Watering"
 else:
	print "Plant does not need Watering"

#Set our GPIO Numbering to BCM
GPIO.setmode(GPIO.BCM)

#Define Channel as No 17
channel = 17

#Set the GPIO Pin to be an Input 
GPIO.setup(channel, GPIO.IN)

#Poll the GPIO pin and and detect when the Pin goes High Or Low
GPIO.add_event_detect(channel, GPIO.BOTH, bouncetime=300)

#Assign a function to the GPIO Pin so that when the is a change on the Pin it calls the callback function
GPIO.add_event_callback(channel, callback)

while True:
   time.sleep(0.5)
