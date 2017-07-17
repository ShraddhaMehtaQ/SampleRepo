file = open('testfile.txt', 'r') 
ctr = 0
for line in file: 
	ctr = ctr+1
print ("There are {} lines in the given file".format(ctr))