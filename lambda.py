from functools import reduce

my_list = [1,2,3,4,5]

# multiply each item by 10 
''' usage of Lambda

lambda param: action(param)
'''

print(list(map(lambda item: item * 10, my_list)))

# to find odd number in the list using Reduce

print(list(filter(lambda item: item % 2 !=0, my_list)))

#lambda expression utilizing reduce function

print(reduce(lambda acc, item: acc+item, my_list))


# lamda to square the list
my_list1 = [5,4,3]

print(list(map(lambda item: item **2, my_list1)))

# list sorting based on 2nd item in each tuple

a = [(0,2), (4,3), (10,-1), (9,9)]
a.sort(key=lambda x: x[1])
print(a)