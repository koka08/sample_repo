

def F(n):
    if n == 0: return 0
    elif n == 1: return 1
    else: return F(n-1)+F(n-2)
s=0
for i in range(0,50):
	s=F(i)
	print(s)
	if(s<50):
		print(s)
	else:
		break

