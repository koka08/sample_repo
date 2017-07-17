x=int(raw_input("enter a number:"))
print(x),
while(x!=1):
	if(x%2==0):
		x=x//2
		print(x),
	else:
		x=3*x+1
		print(x),
	