import math
 
class Demo:

    def append(self,lt,r):
        lt.append(r)
	print(lt)
    def remove(self,lt,r):
	lt.remove(r)
	print(lt)
    def display(self,lt):
	print(lt)
lt=[1,2,3,4,5,6,9]
c=Demo()
c.append(lt,7)
c.remove(lt,9)
c.display(lt)
