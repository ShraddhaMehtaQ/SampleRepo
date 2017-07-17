def validate(string):
	ctr1=0
	ctr2=0
	ctr3=0
	ctr4=0
	if(len(string) >=6 and len(string)<=16):
		for c in string:
			if c.isupper():
				ctr1 = ctr1+1
			elif c.islower():
				ctr2 = ctr2+1
			elif c.isdigit():
				ctr3 = ctr3+1
			elif c in ('$', '#', '@'):
				ctr4 = ctr4+1
	
	if(ctr1>0 and ctr2>0 and ctr3>0 and ctr4>0):
		return 0
	else:
		return 1


def main():
	str = raw_input("\nEnter the password to be checked: ")
	a = validate(str)
	if (a ==0):
		print ("\nIt's a valid password")
	else:
		print("\nIt's not a valid password")

if __name__== "__main__":
  main()		