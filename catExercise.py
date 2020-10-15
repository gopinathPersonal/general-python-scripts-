#Given the below class:
class Cat:
    species = 'mammal'
    def __init__(self, name, age):
        self.name = name
        self.age = age


# 1 Instantiate the Cat object with 3 cats
myCat1 = Cat('Roxy', 1)
myCat2 = Cat('Drixy', 3)
myCat3 = Cat('Tiger', 6)

# 2 Create a function that finds the oldest cat
def find_oldest(cat1_age, cat2_age, cat3_age):
	return max(cat1_age, cat2_age, cat3_age)



# 3 Print out: "The oldest cat is x years old.". x will be the oldest cat age by using the function in #2
print(f"The oldest cat is {find_oldest(myCat1.age, myCat2.age, myCat3.age)} years old")