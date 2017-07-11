from __future__ import print_function
j =[0, 1]

for i in range (2, 50):
	j.append(j[i-2]+ j[i-1])
k=0
while(j[k] <50):
	print (j[k], end=' ')
	k = k+1
