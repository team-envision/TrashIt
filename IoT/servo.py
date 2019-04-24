import pyrebase
import os
import RPi.GPIO as GPIO
import time
import sys

#config = {
#  "apiKey": "",
#  "authDomain": "",
#  "databaseURL": "https://smart-dustbin-e369d.firebaseio.com/",
#  "storageBucket":""
#}

#firebase = pyrebase.initialize_app(config)
#db = firebase.database()

#db.child("All Bins").child("Bin 1").update({"Bio_percent": 25})

GPIO.setmode(GPIO.BOARD)
GPIO.setup(7,GPIO.OUT)

p = GPIO.PWM(7,50)
p.start(7.5) #NEUTRAL START - DONT CHANGE
#db.child("All Bins").child("Bin 1").update({"Bio_percent": 25})
a = 1
try:
	if a==0:
		while True:
			p.ChangeDutyCycle(7.5)
			time.sleep(3) #Bin open time
			p.ChangeDutyCycle(12.5)
			time.sleep(1)
			p.stop()
			sys.exit()
	elif a==1:
		while True:
			p.ChangeDutyCycle(7.5)
			time.sleep(3) #Bin open time
			p.ChangeDutyCycle(2.5)
			time.sleep(1)
			p.stop()
			sys.exit()

except KeyboardInterrupt:
	p.stop()
	GPIO.cleanup()
