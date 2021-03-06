########################################################
# Authors: Gabriel Detter, 
# Class: Senior Design
# Group: 8B
########################################################

# Import required liraries
import time
import sys
import serial

from os import system, name 

# Import LSS library
import lss
import lss_const as lssc

# for contact sensor's digital input
import RPi.GPIO as GPIO
import time
from contact_sensor import contact_sensor

# for our arm's movement
from motion import motion

 # for windows 
if name == 'nt':
    CST_LSS_Port = "COM3"
    		
 
    # for mac and linux(here, os.name is 'posix') 
else: 
    CST_LSS_Port = "/dev/ttyUSB0"
# Constants
#CST_LSS_Port = "/dev/ttyUSB0"		# For Linux/Unix platforms
# CST_LSS_Port = "COM1"				# For windows platforms
CST_LSS_Baud = lssc.LSS_DefaultBaud

# Create and open a serial port
lss.initBus(CST_LSS_Port, CST_LSS_Baud)

# Create LSS objects
mt  = motion(lss)

# define our clear function 
def clear(): 
  
    # for windows 
    if name == 'nt': 
        _ = system('cls') 
  
    # for mac and linux(here, os.name is 'posix') 
    else: 
        _ = system('clear') 

# Setup GPIO input reading
GPIO.cleanup()
sensor_pin = 18
GPIO.setmode(GPIO.BOARD)
GPIO.setup(sensor_pin,GPIO.OUT) # board pin 13
cs = contact_sensor(GPIO, sensor_pin)

#Main loop
mt.start()
exit = 0
counter = 0
max_steps = mt.getNumPositions()

#mt.estop()
while(exit == 0):
	clear()
	mt.printLocation()
	print(cs.currentReading())
	time.sleep(.5)
	
	current_step = 1 + (counter % max_steps)
	
	

	if(mt.holdOn() == False):
		# check if the contact sensor reading is as expected
		try:
			cs.validateStep(current_step) # will raise AssertionError and terminate program if GPIO is not as expected
		except AssertionError as e:
			while True:
				mt.blink()
				print(cs.currentReading())
		mt.stepPosition(current_step)
		counter += 1
	if (counter >= max_steps):
		exit = 1
#mt.end()
# Destroy the bus
#mt.lss.closeBus()

# Destroy objects
#del mt

