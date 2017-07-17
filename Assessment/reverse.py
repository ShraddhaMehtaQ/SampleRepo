num = int(raw_input("Enter the number to be reversed: "))
rev = 0
while (num>0):
	temp = num%10
	rev = (rev*10)+temp
	num = num/10
print ("The reversed number is: {}".format(rev))