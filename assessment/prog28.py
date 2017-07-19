import re

l=["ABd1234@1","a F1#","2w3E*","2We3345"]
x=len(l)
print(x)
for i in range(0,x):

	if((len(l[i])>=9 and len(l[i])<=16) and (re.search("[a-z]",l[i])) and (re.search("[0-9]",l[i])) and (re.search("[A-Z]",l[i])) and (re.search("[$#@]",l[i]))):
						print(l[i])
					
	
	
