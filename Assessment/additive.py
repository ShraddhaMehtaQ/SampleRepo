str= raw_input("\nEnter the sequence to be checked with numbers seperated by spaces: ")
str = list(map(int, str.split(' ')))
ctr = 0
j = (len(str))-2
for i in range(j):
	if (str[i]+str[i+1] == str[i+2]):
		i= i+1;
if(i == len(str)-2):
	print ("\nThe given sequence is an additive sequence")
else:
	print ("\nThe given sequence is not an additive sequence")