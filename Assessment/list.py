a = raw_input("Enter the list to be checked seperated only by comma: ")
a = [int (x) for x in a.split(',')]
b = [x for x in range(a[0], a[-1] + 1)]
print (list(set(a) ^ set(b)))