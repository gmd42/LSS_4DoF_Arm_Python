########################################################
# Authors: Gabriel Detter, 
# Class: Senior Design
# Group: 8B
########################################################

# Import required liraries
import time
import serial
import pynput

# Import LSS library
import lss
import lss_const as lssc

# Constants
#CST_LSS_Port = "/dev/ttyUSB0"		# For Linux/Unix platforms
CST_LSS_Port = "COM3"				# For windows platforms
CST_LSS_Baud = lssc.LSS_DefaultBaud

# Create and open a serial port
lss.initBus(CST_LSS_Port, CST_LSS_Baud)

# Create LSS objects
all_Servo = []
base = lss.LSS(1)
shoulder = lss.LSS(2)
elbow = lss.LSS(3)
wrist = lss.LSS(4)
claw = lss.LSS(5)

#Add all LSS object to list for universal changes
all_Servo.append(base)
all_Servo.append(shoulder)
all_Servo.append(elbow)
all_Servo.append(wrist)
all_Servo.append(claw)

def home():
	for x in all_Servo:
		x.move(0)

home()