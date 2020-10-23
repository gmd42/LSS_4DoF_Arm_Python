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
#all_Servo.append(claw)

# define our clear function 
def clear(): 
  
    # for windows 
    if name == 'nt': 
        _ = system('cls') 
  
    # for mac and linux(here, os.name is 'posix') 
    else: 
        _ = system('clear') 

#Go to home position (currently 0)
def home():
	for x in all_Servo:
		x.move(0)

#Make all servos limp
def estop():
	for x in all_Servo:
		x.limp()

#Prints the position of each servo
def printLocation():
	for x in all_Servo:
		print(x.getPosition(),"\n")

#Waits until the arm has stopped moving
def holdOn():
	done = 0
	while(done == 0):
		for x in all_Servo:
			print(x.getSpeedPulse())
			if (int(x.getSpeed()) == 0):
				done = 1
			else:
				done = 0
				break

#This function should move the arm to the next sequence
#Will need to create a datastructre to hold the sequences easily

#def stepPosition():

#Set the maximum speed and acceleration
for x in all_Servo:
	x.setMaxSpeed(30)
	x.setAngularAcceleration(10)

#####I am ugly delete me ASAP!####

holdOn()
home()

holdOn()
base.move(-845)
shoulder.move(59)
elbow.move(391)
wrist.move(75)

holdOn()
base.move(-845)
wrist.move(97)

holdOn()
elbow.move(288)
shoulder.move(194)


holdOn()
base.move(-845)
shoulder.move(59)
elbow.move(391)
wrist.move(75)

holdOn()
home()

####End of disgusting pile of code####

#Main loop
exit = 0
while(exit == 0):
	clear()
	printLocation()
	time.sleep(.5)
	#holdOn()
	#stepPosition()



# Destroy objects
del base
del shoulder
del elbow
del wrist
del claw

# Destroy the bus
lss.closeBus()