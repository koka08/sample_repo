x=int(raw_input("enter a number"))
for i in range(0,x):
	if(2**i<=x):
		if(x==2**i):
			print("the number is power of 2")
			break
		else:
			continue
if(x!=2**i):
	print("Not a power of 2")
		