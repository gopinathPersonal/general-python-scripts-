# All classes in python are inherited from class "Object"
# thats why you will see lot of dunder methods when you check the method of any class

class Animal:
    species = 'mammal'
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def make_sound(self):
    	print('Do Nothing')

class Dog(Animal):		# inheriting class Animal 
	def make_sound(self):
		print(f"{self.name} is barking always ")

class Cat(Animal):
	def make_sound(self):
		Animal.make_sound(self)				# to call the make_sound of parent class
		print(f"{self.name} is meowing always ")



# make_sound - is polymorphism (different forms with same name)

roxy = Dog("Roxy", 6)
print(roxy.age)
roxy.make_sound()

julie = Cat("Julie", 3)
print(julie.age)
julie.make_sound()