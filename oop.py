# OOP

class MyCar:
	is_automatic = True	 # this is class obj attribute and its not dynamic
	def __init__(self, name, age):  # constructor method of class called when creating an object
		if (self.is_automatic):    # we can also write Mycar.is_automatic
			self.x = name # when obj is created, obj will create the attribute 'x' assigned with name we used to create obj
			self.age = age
	
	def drive(self):
		print(f'{self.x} is driving')
		return 'Done'

myobj = MyCar('Gopi', 40)
print(myobj.x)
print(myobj.is_automatic)
myobj.drive()
print(myobj.age)
myobj.age = 44
print(myobj.age)