def multiply_by2(num):	
	for item in range(num):
		yield item * 2

final = multiply_by2(10)
for i in final:
	print(i)

# print(next(final))
# print(next(final))
# print(next(final))
# print(next(final))

'''
def multiply_by2(num):
	result = []
	for item in range(num):
		result.append(item * 2)
	return result

final = multiply_by2(10)
print(final)
'''