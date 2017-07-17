list=[1,2,3,4,6,7,8]
c=1
x=len(list)
list.sort()
for i in range(0,x):
	if(c==list[i]):
		c+=1
	else:
		print(c)
		break
		