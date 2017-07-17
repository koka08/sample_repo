import logging 


def alpha(x):
	for i in range(0,x+1):
		for j in range(65,65+i):
			a=chr(j)
			print(a),
		print("\r")
def main():
    logging.basicConfig(filename='myapp.log', level=logging.INFO)
    logging.info('Started')
    n=int(raw_input("enter number of rows to print the alphabets:"))
    alpha(n)
    logging.info('Finished')

main()