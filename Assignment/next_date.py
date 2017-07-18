year = int(raw_input("\nInput a year: "))
month = int(raw_input("\nInput a month[1-12]: "))
day = int(raw_input("\nInput a day[1-31]: "))
if(month == 2):
	if((year%400 == 0) or (year%4==0 and year%100 !=0)):
		if(day == 29):
			day=1
			month=3
		else:
			day = day+1
	else:
		if(day==28):
			day=1
			month=3
		else:
			day = day+1
elif(month == 1 or month == 3 or month == 5 or month == 7 or month == 8 or month == 10 or month ==12):
	if(day ==31):
		if(month == 12):
			day=1
			month=1
			year = year+1
		else:
			day=1
			month = month+1
	else:
		day=day+1
else:
	if(day==30):
		day=1
		month= month+1
	else:
		day= day+1
print("\nThe next date is [yyyy-mm-dd]: {}-{}-{}".format(year,month,day))
		