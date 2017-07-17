from __future__ import print_function 
num = int(raw_input("\nEnter the number to generate the sequence: "))
print(num, end = ', ')
while (num > 1):
	if(num%2 == 0):
		num = num/2
	else:
		num = (3*num)+1
	if (num == 1):
		print (num)
	else:
		print(num, end = ', ')
