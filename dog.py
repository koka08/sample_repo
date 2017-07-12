n=int(raw_input("Enter the dog year in human years:"))
s=0
for i in range(0,n):
	if((i==0) or (i==1)):
		s=s+10.5
	else:
		s=s+4
print(s)