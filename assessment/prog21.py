l=[12,24,35,24,88,120,155,88,120,155]
#print(type(l))
for i in range(0,len(l)-1):
	for j in range(i+1,len(l)-1):
		if(l[i] == l[j]):
			l.remove(l[i])
			
print(l)