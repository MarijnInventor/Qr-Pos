import configparser
import os

#search for the parent dir
config = configparser.ConfigParser()
current_dir = os.path.dirname(__file__)
parDir = os.path.abspath(os.path.join(current_dir, os.pardir))

#Look for the config file and print when the file does not exist
configFile = os.path.join(parDir, 'config.ini')

if os.path.exists(configFile):
    config.read(configFile)
else:
    print('Config file not found!')




#Look for the products file and print when the file does not exist
productsFile = os.path.join(parDir, 'Products.xlsx')
if not os.path.exists(productsFile):
    print('Products file not found!')
    
#Look for the beep file and print when the file does not exist
beep = os.path.join(parDir, 'beep.wav')
if not os.path.exists(beep):
    print('Beep file not found!')
    
#Look for the receipt file and print when the file does not exist
receiptFile = os.path.join(parDir, 'receipt')
if not os.path.exists(receiptFile):
    print('Receipt file not found!')


#Get the current values of the variables in the config file
currency = config.get('SETTINGS', 'currency')
printername = config.get('SETTINGS', 'printer_name')
camsource = config.get('SETTINGS', 'cam_source')
firstlogo = config.get('SETTINGS', 'logo')
logo = firstlogo.replace("~", " ")

#If you want to see the values, you can uncomment the following code:

# print("\nlogo is: " + logo)
# print("\ncurrency is: " + currency)
# print("\nprintername is: " + printername)
# print("\nreceipt location is: " + receiptFile)
# print("\nbeep.wav location is: " + beep)
# print("\nproducts.xlsx is in: " + productsFile)

