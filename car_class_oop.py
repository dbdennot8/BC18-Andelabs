class Car(object):
	def __init__(self, type="trailer", name="General", model="GM"):
		self.type = type
		if self.type != "trailer": 
			self.type = "saloon"
		self.name = name
		self.model = model

	
	def num_of_doors(self):
		number_of_doors = 0
		if self.name != "Porsche" and self.name != "Koenigsegg":
			number_of_doors = 4
		else:
			number_of_doors = 2
		return number_of_doors

	def num_of_wheels(self):
		num_of_wheels = 0
		if self.type != "Trailer":
			num_of_wheels = 4
		else:
			num_of_wheels = "More than 4"
		return num_of_wheels

	def speed(self, status):
		self.status = status
		speed = 0
		if self.status == "parked":
			speed = 0
		else:
			speed = "moving at speed"
		return speed

	def drive_car(self, speed):
		self.speed = speed
		return speed


	 

