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

#Go to home position (currently 0)
def home():
	for x in all_Servo:
		x.move(0)

#Make all servos limp
def estop():
	for x in all_Servo:
		x.limp()


for x in all_Servo:
	x.setMaxSpeed(30)
	x.setAngularAcceleration(10)

home()
time.sleep(10)
base.move(100)
time.sleep(5)
estop()


# Destroy objects
del base
del shoulder
del elbow
del wrist
del claw

# Destroy the bus
lss.closeBus()