print("Enter the temperature:")
print("Select the choice to enter the temperature")
print("1.Degree Celsius")
print("2.Degree Fahrenheit")
print("3.Degree Kelvin")
choice=input("choice(1/2/3):")
x=input("Enter:")
if(choice==1):
	n=input("Enter the choice for conversion:(2/3):")
	if(n==2):
		p=(x*9/5)+32
		print("Degree Fahrenheit")
		print(p)
	if(n==3):
		p=x+273.15
		print("Degree Kelvin")
		print(p)
if(choice==2):
	n=input("Enter the choice for conversion:(1/3):")
	if(n==1):
		p=(x-32)*5/9
		print("Degree Celsius")
		print(p)
	if(n==3):
		p=(x-32)*5/9+273.15
		print("Degree Kelvin")
		print(p)
	
if(choice==3):
	n=input("Enter the choice for conversion:(1/2):")
	if(n==2):
		p=(x-273.15)*9/5+32
		print("Degree Fahrenheit")
		print(p)
	if(n==1):
		p=x-273.15
		print("Degree Celsius")
		print(p)
	
	
	
	


