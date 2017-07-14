#Input from  the user the string to be checked for palindrome
string = str(raw_input("Enter the string to be checked for palindrome:"))

# Initializing conuter with value = 0
ctr = 0

# For loop to break the string and check for palindrome
for i in range (len(string)):
	if(string[i] == string[len(string)-1-i]):
		ctr = ctr + 1
	else:
		break

#Checking if the value of counter is equal to length of the string, which will indicate that the string is palindrome
if(ctr == len(string)):
	print("The given string is a palindrome")
else:
	print("The given string is not a palindrome")
