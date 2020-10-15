class SuperList(list):
	def __len__(self):
		return 1000


super_list1 = SuperList();

print(len(super_list1))
super_list1.append(5) 
super_list1.append(2)
print(super_list1)
''' in order to have the superlist class 
having list class' fucntios like "append"
inherit list class in SuperList(list)

'''