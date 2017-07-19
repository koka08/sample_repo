class MyException:
	def __init__(self,s):
		self.s=s
		print("The error string is : "+str(self.s))
		
st=str(raw_input("enter a message : "))
MyException(st)