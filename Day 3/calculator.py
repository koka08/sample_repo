
	
def add(x, y):
   return x + y
def subtract(x, y):
   if(x>y):	
   	return x - y
   else:
	print("num2 is Greater than num1.Thus displayed result is mod of the difference:")
	return(y-x)
def multiply(x, y):
   return x * y
def divide(x, y):
   return x / y
def mod(x, y):
   return x % y
def menu():
	print("Select operation.")
	print("1.Add")
	print("2.Subtract")
	print("3.Multiply")
	print("4.Divide")
	print("5.Modulus")
	

st='y';
while(st=='y'): 
	menu()
	choice = input("Enter choice(1/2/3/4/5):")
	print choice	
	num1 = input("Enter first number: ")
	num2 = input("Enter second number: ")
	

	if choice == 1:
   		print(add(num1,num2))
 
	elif choice == 2:
	        print(subtract(num1,num2))
 
	elif choice == 3:
   		print(multiply(num1,num2))
 
	elif choice == 4:
   		print(divide(num1,num2))
	elif choice == 5:
		print(mod(num1,num2))
	else:
   		print("Invalid input")

	st=str(raw_input("choose to continue (y/n)):"))