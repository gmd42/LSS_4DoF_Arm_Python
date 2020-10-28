########################################################
# Authors: Gabriel Detter, 
# Class: Senior Design
# Group: 8B
########################################################

# Import required liraries
import time
import serial
import pynput

from os import system, name 

# Import LSS library
import lss
import lss_const as lssc


# for our arm's movement
from motion import motion

# Constants
#CST_LSS_Port = "/dev/ttyUSB0"		# For Linux/Unix platforms
CST_LSS_Port = "COM3"				# For windows platforms
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

