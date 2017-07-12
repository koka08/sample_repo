a=int(raw_input("Enter the number of rows:"))
b=int(raw_input("Enter the number of coloumns:"))
c=a/2
x=2
print(c)
if(a>2):
	for j in range(0,a):
		if((j==0) or (j==c)):
			for i in range(0,b):
				print("*"),			
		else:
			for i in range(0,b):
				if((i==0) or(i==b-1)):
					print("*"),
				else:
					print(" "),
		print("\r")
	j=j+1
else:
	print("Number of rows should be greater then 2")
	
	