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
		[-845, 59, 391, 75],\
		[-845, None, None, 97],\
		[None, 194, 288, None],\
		[-845, 59, 391, 75]\
		]

	#Go to home position (currently 0)
	def home(self):
		for x in self.all_Servo:
			x.moveCL(0, self.MAXCURRENT)

	#Make all servos limp
	def estop(self):
		for x in self.all_Servo:
			x.limp()

	#Prints the position of each servo
	def printLocation(self):
		for x in self.all_Servo:
			print(x.getPosition(),"\n")

	#Returns true if the arm is moving
	def holdOn(self):
			for x in self.all_Servo:
				if (abs(int(x.getSpeedPulse())) > 2):
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
		for i,servo in enumerate(self.positions):
			if servo != None:
				self.all_Servo[i].moveCL(self.positions[step-1][i], self.MAXCURRENT)

	def getNumPositions(self):
		return len(self.positions)

