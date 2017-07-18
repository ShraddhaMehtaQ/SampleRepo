str = raw_input("Enter the string whose digits are to be printed: ")
list = str.split(" ")
list = [x for x in list if x.isdigit()]
print list
