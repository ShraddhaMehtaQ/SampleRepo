class Person(object):
	def getGender(self):
		return "Gender Unknown"
		

class Male(Person):
	def getGender(self):
		return "Gender: Male"

class Female(Person):
	def getGender(self):
		return "Gender: Female"

male = Male()
female = Female()
person = Person()
print male.getGender()
print female.getGender()
print person.getGender()