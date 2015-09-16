class Calc(object):
	def __init__(self):
		self.value = 0
		self.history = str(self.value)

	def __str__(self):
		return self.history + " = " + str(self.value)

	def add(self, value):
		self.value += value
		self.history += " + %i" %value

	def subtract(self, value):
		self.value -= value
		self.history += " - %i" %value

	def multiply(self, value):
		self.value *= value
		self.history += " * %i" %value

	def divide(self, value):
		self.value /= value
		if self.value % 1 == 0:
			self.value = int(self.value)
		self.history += " / %i" %value

	def clear(self):
		self.value = 0
		self.history = str(self.value)

	def new_calculation(self, value):
		self.value = value
		self.history = str(value)


if __name__ == "__main__":
	a = Calc()
	a.new_calculation(50)
	a.add(50)
	a.add(3)
	a.add(100)
	a.subtract(33)
	a.subtract(100)
	a.multiply(2)
	a.multiply(4)
	a.divide(2.111)
	print a.value
	print a
		