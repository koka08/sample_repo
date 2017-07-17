import re
def validate(st,x):
	if(x>=9 and x<=12):
		if re.search("[a-z]",st):
			if re.search("[0-9]",st):
				if re.search("[A-Z]",st):
					if re.search("[$#@]",st):
						print("VAlID String")
					
	else:
		print("Invalid String")
	
def main():
	st=str(raw_input("Enter the password:"))
	x=len(st)
	validate(st,x)

main()