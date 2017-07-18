tup=(1,2,3,4,5,6,7,8,9,10)
lis=list()
for i in range(len(tup)):
	if tup[i]%2==0:
		lis.append(tup[i])

tup2=tuple(lis)
print("\nThe tuple whose values are even numbers in the given tuple (1,2,3,4,5,6,7,8,9,10) is: {}".format(tup2))
