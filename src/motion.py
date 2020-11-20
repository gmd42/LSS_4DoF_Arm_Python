import time
class motion():
	def __init__(self, lss):
		self.MAXCURRENT = 700
		self.lss = lss
		self.base = lss.LSS(1)
		self.shoulder = lss.LSS(2)
		self.elbow = lss.LSS(3)
		self.wrist = lss.LSS(4)
		#self.claw = lss.LSS(5)
		self.all_Servo = []
		for i in range(1,5):
			self.all_Servo.append(lss.LSS(i))
			lss.LSS(i).setMaxSpeed(30)
			lss.LSS(i).setAngularAcceleration(10)
		self.positions =[\
		#Far above infeed
		[-845, 40, 420, 10, 0],\
		#Close to infeed
		[None, 132, 357, None, 0],\
		#grab stent
		[None, 205, 314, None, 0],\
		#back up
		[None, 40, 420, None, 0],\
		#Mandrel far
		[63, 40, 350, 20, 0],\
		#Mandrel slam
		[121, 40, 350, 60, 5],\
		#Close pull off
		[None, -60, 425, 60, 0],\
		#Perform laser
		[None, -500, 0, None, 5],\
		#Close approach
		[None, -60, 425, 60, 0],\
		#Grab
		[121, 40, 353, 60, 5],\
		#Close off mandrel
		[63, 40, 360, 20, 0],\
		#Clear mandrel
		[63, -210, 613, 20, 0],\
		#
		[870, -210, 613, 20, 0],\
		[870, 41, 320, 32, 0],\
		[975, 41, 320, 32, 0],\
		#Let go
		[975, -130, 450, 32, 0]]\
		

	#Go to home position (currently 0)
	def home(self):
		for x in self.all_Servo:
			x.move(0)

	def blink(self):
			self.lss.LSS(4).setColorLED(0)
			time.sleep(.5)
			self.lss.LSS(4).setColorLED(1)
			time.sleep(.5)
	#Make all servos limp
	def estop(self):
		for x in self.all_Servo:
			x.limp()

	#Make all servos freeze
	def freeze(self):
		for x in self.all_Servo:
			x.hold()

	#Prints the position of each servo
	def printLocation(self):
		for x in self.all_Servo:
			print(x.getPosition(),"\n")

	#Returns true if the arm is moving
	def holdOn(self):
			for x in self.all_Servo:
				try:
					z = int(x.getSpeedPulse())
				except Exception:
					return True
				if (abs(z) > 1):
					return True
			return False

	def start(self):		
		while(self.holdOn() == True):
			pass
		self.home()


	def end(self):		
		while(self.holdOn() == True):
			pass
		self.home()

	# servo and step numbers indexed from 1, position list indexed from 0
	def stepPosition(self, step):
		i = 0
		while(i < len(self.all_Servo)):
			if self.positions[step-1][i] != None:
				self.all_Servo[i].move(self.positions[step-1][i])
			i += 1
		time.sleep(self.positions[step-1][i])

	def getNumPositions(self):
		return len(self.positions)

