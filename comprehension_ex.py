my_dict = {num:num**2 for num in [1,2,3] if num%2 !=0}

print(my_dict)

some_list = ['a', 'b', 'c', 'b', 'd', 'm', 'n', 'n']
# find duplicates and print in a list
duplic = [x for x in some_list if some_list.count(x) > 1]
print(duplic)

# 