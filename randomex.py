import random

print(random.random())  # print a random number between 0 1n 1

print(random.randint(1, 10)) # print a random int  between 1 and 10

print(random.choice([1,2,3,4,5]))# print a random choice

list1 = [1,2,3,4,5]
random.shuffle(list1)  # shuffiles the list randomly
print(list1)