########################################################
# Authors: Gabriel Detter, 
# Class: Senior Design
# Group: 8B
########################################################

# Import required liraries
import time
import sys
import serial
import pynput

from os import system, name 

# Import LSS library
import lss
import lss_const as lssc

# for contact sensor's digital input
import RPi.GPIO as GPIO
import time


####### example code for GPIO input ######
GPIO.setmode(GPIO.BOARD)
GPIO.setup(13,GPIO.OUT) # board pin 10
try:
	while True:
		'''
		time.sleep(0.5)
		print("Reading...")
		GPIO.output(16,1)
		print("on")
		time.sleep(0.5)
		GPIO.output(16,0)
		print("off")
		'''	
		time.sleep(0.5)
		if GPIO.input(13):
			print("off")
		else:
			print("on")
except KeyboardInterrupt:
	print("STOP")
finally:
	print("cleanup")
	GPIO.cleanup() # you MUST do GPIO cleanup whenever main.py ends
	sys.exit(0)
##### end of GPIO input exmaple ##############

# for our arm's movement
from motion import motion


# Constants
CST_LSS_Port = "/dev/ttyUSB0"		# For Linux/Unix platforms
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

#Main loop
mt.start()
exit = 0
counter = 0
max_steps = mt.getNumPositions()

#mt.estop()
while(exit == 0):
	clear()
	mt.printLocation()
	time.sleep(.5)
	
	if(mt.holdOn() == False):
		mt.stepPosition(1 + (counter % max_steps))
		counter += 1
	if (counter >= max_steps):
		exit = 1
	
#mt.end()
# Destroy the bus
#mt.lss.closeBus()

# Destroy objects
#del mt

