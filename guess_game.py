from random import randint

# generate random int number between 1~10

sysGenerated = randint(1,10)
print(sysGenerated)
# input from user between 1~10
while True:
	try:
		guess = input('Enter number between 1 and 10: ')
		print(guess)
		if int(guess) > 0 and int(guess) < 11 :
			print('All good.. ')
			break
		else:
			print('Hello ener 1 ~ 10')	
	except ValueError:
		print('Please enter a number')
		continue
	except ZeroDivisionError:
		print('Please enter number greater than 0')
		continue

