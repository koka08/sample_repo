import re
st=str(raw_input("Enter the password:"))
x=len(st)
print(x)
if(x>=9 and x<=16):
	if re.search("[a-z]",st):
		if re.search("[0-9]",st):
			if re.search("[A-Z]",st):
				if re.search("[$#@]",st):
					print("VAlID String")
					
else:
	print("Invalid String")
	
