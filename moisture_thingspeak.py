import RPi.GPIO as GPIO
import time
from wia import Wia
import json
import urllib2

WRITE_API_KEY='PLKA3BS2S4WOMG30'

baseURL='https://api.thingspeak.com/update?api_key=%s'%WRITE_API_KEY

#This function will be called every time there is a data change on the GPIO channel 17, if channel goes 
def callback(channel):
 if GPIO.input(channel):
	print "Plant Needs Watering"
	conn = urllib2.urlopen(baseURL + '&field1=%s' % (channel))
	conn.close()
 else:
	print "Plant does not need Watering"
        conn = urllib2.urlopen(baseURL + '&field2=%s' % (channel))
	conn.close()

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
