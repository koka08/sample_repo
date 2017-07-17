import logging
def sum(x):
	sum=0
	while(x!=0):
		digit=x%10
		sum=sum+digit
		x=x//10
	print(sum)

def main():
    logging.basicConfig(filename='myapp1.log', level=logging.INFO)
    logging.info('Started')
    n=int(raw_input("enter a number:"))
    sum(n)
    logging.info('Finished')

main()	

