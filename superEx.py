class User():
	def __init__(self, email):
		self.email = email

	def sign_in(self):
		print('logged in')


class Wizard(User):
	def __init__(self, name, power, email):
		#User.__init__(self, email)           # to Access init function of super class
		super().__init__(email)		# Another way to Access init function of super class
		self.name = name
		self.power = power

	def attack(self):
		print(f'attacking with power of {self.power}')

wizard1 = Wizard('Sen', 45, 'sen@gmail.com')
print(wizard1.email)

#introspection
print(dir(wizard1))    # will list out all methods, attributes this object has acess
