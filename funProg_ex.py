from functools import reduce

#1 Capitalize all of the pet names and print the list
my_pets = ['sisi', 'bibi', 'titi', 'carla']

def toupper(my_pets):
	return my_pets.capitalize()

print(list(map(toupper, my_pets)))
print(my_pets) # this is not impacting data outside the fucntion


#2 Zip the 2 lists into a list of tuples, but sort the numbers from lowest to highest.
my_strings = ['a', 'b', 'c', 'd', 'e']
my_numbers = [5,4,3,2,1]

print(tuple(zip(my_strings, sorted(my_numbers))))


#3 Filter the scores that pass over 50%
scores = [73, 20, 65, 19, 76, 100, 88]

def passingscore(item):
	return item > 50 

print(list(filter(passingscore, scores)))
print(scores) 

#4 Combine all of the numbers that are in a list on this file using reduce (my_numbers and scores). What is the total?
def accumulator(acc, item):
    return acc + item

print(reduce(accumulator, (my_numbers + scores)))