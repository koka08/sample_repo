st=str(raw_input("Enter a string:"))
x=len(st)
c=0
p=0
for i in st:
	if i.isdigit():
		c=c+1
	elif i.isalpha():
		p=p+1
	else:
		break

print("Letter:",p)
print("Digits:",c)
