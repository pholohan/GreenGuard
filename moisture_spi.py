#!/usr/bin/python
 
import spidev
import os
import time
import json
import urllib2

#Write API Key for Thingspeak
WRITE_API_KEY='PLKA3BS2S4WOMG30'

#URL for the Thingspeak Web API
baseURL='https://api.thingspeak.com/update?api_key=%s'%WRITE_API_KEY
 
delay = 0.2
 
#Python Binding for Serial Peripheral Interface
spi = spidev.SpiDev()

#Open SPI (bus, dev)
spi.open(0,0)

#Define the MAX SPI speed
spi.max_speed_hz=1000000
 
#Read Channel Function
def readChannel(channel):
  val = spi.xfer2([1,(8+channel)<<4,0])
  data = ((val[1]&3) << 8) + val[2]
  return data

#Try/Catch for read channel and filter out zeros 
if __name__ == "__main__":
  try:
    while True:
      val = readChannel(0)
      if (val != 0):
        print(val)
        conn = urllib2.urlopen(baseURL + '&field1=%s' % (val))
	conn.close()
      time.sleep(delay)
      
  except KeyboardInterrupt:
    print "Cancel."

