def last(y):
	return y[-1]
a=input("Enter a list of tuples:")
print("Sorted list of tuples:")
print(sorted(a, key=last))