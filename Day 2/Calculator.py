n= int(raw_input("Enter 1 for Addition\n Enter 2 for Subtraction\n Enter 3 for Multiplication\n Enter 4 for Division\n Enter 5 for Power\n Enter 6 for Remainder\n Enter 0 for Exit"))
if n==1:
	a, b = int(raw_input("Enter the two numbers for Addition: ")
	print ("The addition of two numbers is: {}" .format(a+b))
elif( n==2):
	a, b = int(raw_input("Enter the two numbers for Subtraction: ")
	print ("The subtraction of two numbers is: {}" .format(a-b))
elif( n==3):
	a, b = int(raw_input("Enter the two numbers for Multiplication: ")
	print ("The multiplication of two numbers is: {}" .format(a*b))
elif( n==4):
	a, b = int(raw_input("Enter the two numbers for Division: ")
	print ("The division of two numbers is: {}" .format(a/b))
elif( n==5):
	a, b = int(raw_input("Enter the two numbers for Power: ")
	print ("{} raised to {} is: {}" .format(a, b, a ** b))
elif( n==6):
	a, b = int(raw_input("Enter the two numbers for Remainder: ")
	print ("The remainder when {} is divided by {} is: {}" .format(a, b, a%b))
elif( n==0):
	break
else:
	print("Invalid Input. Try again")
	continue


