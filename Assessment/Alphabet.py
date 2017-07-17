from __future__ import print_function
import string
num = int(raw_input("Enter the number of rows you want in your alphabet patter: "))
for i in range(num+1):
	for j in range(i):
		print (string.uppercase[i:i+j] , end = '')
	print ("\n")