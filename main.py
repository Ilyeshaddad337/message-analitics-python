import json

CNV_PATH = 'messages//inbox//nourbenayache_sqkapd3pyw'

option_menu = {
	1: 'search for a message' , 
	2: 'basic analitics',
	3: 'Exit' ,
}

def print_options():
	print('----------Msg Analitics----------')
	for key in option_menu.keys():
		print(key , '---' , option_menu[key])

def load_cnv ():
    cnv = None
    
def search(msg):
    
    
	pass


def analize():
	pass

if __name__ == '__main__':
	load_cnv()
	
	while(True):
		
		print_options()
		option = ""

		try:
			option = int(input('Select an action to perform :'))

		except:

			print('option' , option)

		if option == 1:
			msg = input("Enter a messge to search for: ")
			search(msg)

			

		elif option == 2:
			print("OPTION2 WORING....")
			analize()
		elif option == 3:
			print("Exit code....")
			exit()
		else:
			print('Invalid Action:' , option ,'Try again...')

