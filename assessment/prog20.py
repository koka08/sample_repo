class Person:
	def getGender(s,g):
		print("Gender = "+str(s.g))

class Male(Person):
	def getGender(s,g):
		print("Gender = "+str(s.g))

class Female(Person):
	def getGender(s,g):
		print("Gender = "+str(s.g))

x=Male()
y=Female()
print(x.getGender("Male"))
print(y.getGender("Female"))