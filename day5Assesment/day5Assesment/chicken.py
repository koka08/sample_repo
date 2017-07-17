hc=int(raw_input("enter the headcount:"))
lc=int(raw_input("enter the legcount:"))
chl=2
rl=4
ch=35
rb=0
tlc=ch*chl+rl*rb
thc=ch+rb
while(True):
	if((tlc!=lc) or (thc!=hc)):
		ch=ch-1
		rb=rb+1
		tlc=ch*chl+rl*rb
		thc=ch+rb
	if((tlc==lc) and (thc==hc)):
		break

print(ch)
print(rb)