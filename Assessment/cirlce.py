class Circle():
	def __init__(self):
		self.radius=25
	
	def area (self):
		self.area = self.radius*self.radius*3.14

c = Circle()
c.area()
print(c)
print ("The radius is {} and area is {}".format(c.radius, c.area))