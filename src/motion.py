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
		[-855, 40, 420, 10, 0],\
		[None, 132, 357, None, 0],\
		[None, 205, 314, None, 0],\
		[None, 40, 420, None, 0],\
		[63, 40, 350, 20, 0],\
		[121, 40, 350, 60, 5],\
		[None, -60, 425, 60, 0],\
		[None, -500, 0, None, 5],\
		[None, -60, 425, 60, 0],\
		[121, 40, 353, 60, 5],\
		[63, 40, 360, 20, 0],\
		[63, -210, 613, 20, 0],\
		[870, -210, 613, 20, 0],\
		[870, 41, 320, 32, 0],\
		[975, 41, 320, 32, 0],\
		[975, -130, 450, 32, 0]]\
		

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

	#Returns true if the arm is moving
	def holdOn(self):
			for x in self.all_Servo:
				if (abs(int(x.getSpeedPulse())) > 1):
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

