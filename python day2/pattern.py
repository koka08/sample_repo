n=input('Enter a Number')
for i in range(0,n+1):
	for j in range(0,i):
		print("*"),
	print("\r")
for m in range(0,n):
	for p in range(0,n-m-1):
		print("*"),
	print("\r")