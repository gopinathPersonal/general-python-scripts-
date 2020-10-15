
# map will take arguments Function, iterables 

my_list = [2,5,6,7,10]
def multiply_by10(item):
	return item * 10


print(list(map(multiply_by10, my_list)))
print(my_list) # this is not impacting data outside the fucntion


# filter function 
# we input n number of data and we receive back less than n

def only_odd(item):
	return item %2 != 0 


print(list(filter(only_odd, my_list)))
print(my_list)


# zip function 
# 2 or more lists /iterables and zip them together, even it works for list , tuples as well
list1 = [1,2,3,4]
list2 = [10,20,30]

print(list(zip(list1, list2))) 

# Reduce function 
# given the list of values as data input , reduce function  will make the output reduced

def accumulator(acc, item):
	print(acc, item)
	return acc + item  # returns one single value 

print(reduce(accumulator, my_list, 0))  # acc initilized with value 0
print(mulist)


