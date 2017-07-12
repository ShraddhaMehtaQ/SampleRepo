string = raw_input("Enter the string to be checked for palindrome:")
ctr = 0
for i in range (len(string)):
	if(string[i] == string[len(string)-1-i]):
		ctr = ctr + 1
	else:
		break
if(ctr == len(string)):
	print("The give string is a palindrome")
else:
	print("The given string is not a palindrome")
