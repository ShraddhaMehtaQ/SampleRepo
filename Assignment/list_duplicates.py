list1 =  [12,24,35,24,88,120,155,88,120,155]
list1 = list(set(list1))
list1 = list1[::-1]
print("\nThe given list [12,24,35,24,88,120,155,88,120,155] without any duplicates and reversed is: ")
for i in range(len(list1)):
	print list1[i],