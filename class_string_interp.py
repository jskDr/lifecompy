class Car():
	def __init__(self, name = "BMW"):
		self.name = name

	def show( self):
		print( "Car name is %(name)s" % {"name":self.name})
		print( "Show all member functions as dict format:")
		print( self.__dict__)
		print( "Car name is %(name)s" % self.__dict__)

def testing():
	print( "Hello, this is Car class.")

	car = Car("BMW")
	car.show()

if __name__ == "__main__":
	testing()
