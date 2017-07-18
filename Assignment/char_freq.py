str = raw_input("\nEnter the string whose character frequency has to be found: ")
str = list(str)
str2 = list(set(str))
print("\nThe character frequencies are: ")
for i in range(len(str2)):
	print("{},{}".format(str2[i],str.count(str2[i])))