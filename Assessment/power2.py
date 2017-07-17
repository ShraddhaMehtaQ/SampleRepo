def is_power(n):
	if n == 2:
		return 0
	elif n > 2:
		if(n%2 == 0):
			return is_power(n/2)
		else:
			return 1
	else:
        	return 1

num = int(raw_input("\nEnter the number to check whether it is a power of two: "))
ans = is_power(num)
if (ans == 0):
	print("The number is a power of 2")
else:
	print("The number is not a power of 2")