#Given the below class:
class Cat:
    species = 'mammal'
    def __init__(self, name, age):
        self.name = name
        self.age = age
# cls keyword will create instance of class using __init__  and also to modify the attribute of the class 
    @classmethod
    def myAreaCircle(cls, radius):
    	return (3.14 * radius **2)

    @classmethod
    def adding_things(cls, num1, num2):
    	return cls('Johnny', num1 + num2) 

# Static method is similar to classmethod, but we dont use 'cls', meaning we cannot access any of attribute of class (eg name, age)
    @staticmethod 
    def multiply(num1, num2):
    	return num1*num2

# To access Classmethod, no need to create an instance of class >> classname.method 
mycat = Cat.adding_things(10, 15)
print (mycat.age)

# To access Classmethod, no need to create an instance of class >> classname.method 
print (Cat.myAreaCircle(5))		

# To access Static method, no need to create an instance of class >> classname.method 	
print (Cat.multiply(5, 6))

