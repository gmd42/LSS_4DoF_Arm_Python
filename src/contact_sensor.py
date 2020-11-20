class contact_sensor():
	def __init__(self, GPIO, sensor_pin):
		self.GPIO = GPIO
		self.sensor_pin = sensor_pin
		self.validateList = [0, 1, 1, 0, 0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0] # fill in with expected readings of sensor for every step

	def validateStep(self, stepNumber):
			assert self.GPIO.input(self.sensor_pin) == self.validateList[stepNumber]
		
				




	def currentReading(self):
		if self.GPIO.input(self.sensor_pin):
			print("Stent is gripped")
		else:
			print("Stent is not gripped")
