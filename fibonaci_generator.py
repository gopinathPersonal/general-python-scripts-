def fib(number):
	a = 0
	b = 1
	for item in range(number):
		yield a
		temp = a 
		a = b
		b = temp + b 



final = fib(20)
for i in final:
	print(i)