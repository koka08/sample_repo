import logging 
n=int(raw_input("enter number of rows to print the alphabets:"))

def alpha(x):
	for i in range(0,n+1):
		for j in range(65,65+i):
			a=chr(j)
			print(a),
		print("\r")
def main():
    logging.basicConfig(filename='myapp.log', level=logging.INFO)
    logging.info('Started')
    apha(n)
    logging.info('Finished')