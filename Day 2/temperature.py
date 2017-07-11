conv = raw_input("Enter c to convert Fahrenheit to Celcius and f to convert Celcius to Fahrenheit")
conv = str(conv)
temp = raw_input("Enter temperature")
temp = float(temp)
if (conv == 'f'):
	print("Temperature in Fahrenheit is: {0}" .format((temp* 1.8) +32))
elif (conv == 'c'):
	print("Temperature in Celcius is: {0}" .format((temp - 32)/1.8))