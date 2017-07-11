m = int(raw_input("Enter no. of rows: "))
n = int(raw_input("Enter no. of columns: "))
if (m==0 or n==0):
	print("Invalid")
for i in range (m):
	if (i==0 or i==m-1):
		print ('*' *n)
	elif (i == m/2):
		print ('*' *(n-1))
	else:
		print('*')