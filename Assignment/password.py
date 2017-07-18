string = raw_input("\nEnter the passwords to be checked seperated by commas: ")
lis = string.split(',')
for i in range(len(lis)):
	ctr1=0
	ctr2=0
	ctr3=0
	ctr4=0
	if(len(lis[i]) >=6 and len(lis[i])<=16):
		for c in lis[i]:
			if c.isupper():
				ctr1 = ctr1+1
			elif c.islower():
				ctr2 = ctr2+1
			elif c.isdigit():
				ctr3 = ctr3+1
			elif c in ('$', '#', '@'):
				ctr4 = ctr4+1
	
	if(ctr1>0 and ctr2>0 and ctr3>0 and ctr4>0):
		print lis[i],
	



	
	
	