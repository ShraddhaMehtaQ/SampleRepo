password = str(raw_input("Enter Password:"))
if(len(password)>= 6 and len(password)<= 16 and any(x.isupper() for x in password) and any(x.islower() for x in password) and any(x.isdigit() for x in password) and any(x in ('$', '#', '@')for x in password)):
	print ("Valid Password")
else:
	print("Invalid Password")
	
