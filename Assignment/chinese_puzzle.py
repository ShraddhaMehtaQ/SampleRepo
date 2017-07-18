import numpy as np
print("\nSolving a classic ancient chinese puzzle")
heads = int(raw_input("Enter the number of heads: "))
legs = int(raw_input("Enter the number of legs: "))
a = np.array([[1,1], [2,4]])
b = np.array([heads, legs])
x = np.linalg.solve(a, b)
print("\nThe number of chickens is {} and the number of rabbits is {}".format(x[0], x[1]))