while True:
	m= int(raw_input("\nPress 1 for mathematical operations, 0 for exit"))
	if(m == 0):
		exit()	
	elif( m==1):
		n= int(raw_input("\n Enter 1 for Addition\n Enter 2 for Subtraction\n Enter 3 for Multiplication\n Enter 4 for Division\n Enter 5 for Modulus"))
		if(n ==1 or n==2 or n==3 or n==4 or n==5):
			a = float(raw_input("\nEnter the first number for given operation: "))
			b = float(raw_input("\nEnter the second number for given operation: "))
			if(n == 1):
				print("\nThe addition of {} and {} is {}".format(a, b, a+b))
			elif(n == 2):
				print("\nThe subtraction of {} and {} is {}".format(a, b, a-b))
			elif(n == 3):
				print("\nThe multiplication of {} and {} is {}".format(a, b, a*b))
			elif(n == 4):
				if (b==0):
					print("\nThe divisor cannot be zero. Try Again")
				else:
					print("\nThe division of {} and {} is {}".format(a, b, a/b))
			elif(n == 5):
				if (b==0):
					print("\nThe divisor cannot be zero. Try Again")
				else:
					print("\nThe remainder when {} is divided by {} is {}".format(a, b, a%b))
		else:
			print("\nInvalid Input. Try Again")
	else:
			print("\nInvalid Input. Try Again")
	
		
	

