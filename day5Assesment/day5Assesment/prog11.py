import logging
def additive():
	list=[6,6,12,18,30]
	c=len(list)
	for i in range(2,c):
		if(list[i]==(list[i-2]+list[i-1])):
			i=i+1
		else:
			print("Invalid Additive Sequance number")
def main():
    logging.basicConfig(filename='Additve.log', level=logging.INFO)
    logging.info('Started')
    additive()
    print("Valid Additve Sequance number")
    logging.info('Finished')

