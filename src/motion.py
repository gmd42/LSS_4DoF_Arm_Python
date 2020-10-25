class motion():
	def __init__(self, lss):
		self.lss = lss
		self.base = lss.LSS(1)
		self.shoulder = lss.LSS(2)
		self.elbow = lss.LSS(3)
		self.wrist = lss.LSS(4)
		self.claw = lss.LSS(5)
		self.all_Servo = []
		for i in range(1,6):
			self.all_Servo.append(lss.LSS(i))
			lss.LSS(i).setMaxSpeed(30)
			lss.LSS(i).setAngularAcceleration(10)
		self.positions =[\
		[-845, 59, 391, 75],\
		[-845, None, None, 97],
		[-None, 194, 288, None],
		[-845, 59, 391, 75]\
		]

	#Go to home position (currently 0)
	def home(self):
		for x in self.all_Servo:
			x.move(0)

	#Make all servos limp
	def estop(self):
		for x in self.all_Servo:
			x.limp()

	#Prints the position of each servo
	def printLocation(self):
		for x in self.all_Servo:
			print(x.getPosition(),"\n")

	#Waits until the arm has stopped moving
	def holdOn():
		done = 0
		while(done == 0):
			for x in self.all_Servo:
				print(x.getSpeedPulse())
				if (int(x.getSpeed()) == 0):
					done = 1
				else:
					done = 0
					break

	def start(self):		
		self.holdOn()
		self.home()

	# servo and step numbers indexed from 1, position list indexed from 0
	def stepPosition(self, step):
		self.holdOn()
		for i,servo in enumerate(self.positions):
			if servo != None:
				self.lss(i+1).move(self.positions[step+1][i])

