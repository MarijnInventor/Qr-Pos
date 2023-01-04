# Qr-Pos
A simple POS (point of sale) system with a qr code for each product.

The purpose of this project is to make a well-functioning POS system that everyone can use for free.

-------------
# Preparation
**Preparation step 1:**

When you have downloaded all the files, launch qrGenerator.py to generate some QR codes.  Enter the number of required qr codes and then click on generate to generate them. Select the folder where the qr codes should be placed. After a very short time you will see "Done!" under the generate button. Then everything is done and you can close the program. Print your qr codes on paper so you can scan them.

**Preparation step 2:**

Now it's time to add your products. When you have applied a qr code to each product, you can scan the first qr code with your phone to see the product number. Open Products.xlsx and search for the product number you just scanned. You can also change the first product number to your just scanned product number. It doesn't matter if they are in order. Enter a name and price and do this for each product. Then close the file before continuing.

**Preparation step 3:**

Finally, edit settings.py to your correct settings. For each setting there is some explanation commented, followed by a variable name and the value of it. Enter your text between the quotation marks. Now you are ready to use the system!

-------------
# Usage

When you run main.py the UI will open. You'll see 2 windows. The first window shows what the webcam sees. Ajust the position so that the camera can see the place where the qr codes are going to be scanned. Currently the program only supports the built in webcam but if you change the default camera and restart the program it probably work too. (I have not tested this!) Another useful option can be to connect a second screen so that the camera can remain focused on the table.
Now you can minimalize the window so you can see the actual UI. The UI contains a box where the scanned products appear, with your logo at the top, and three buttons. 

**These are the functions of the buttons:**

Pay = All prizes will be added up and placed at the bottom of the receipt.

Undo = Delete the last scanned product.

Clear = Delete all products and create a new empty receipt.

There is also a function to print the receipt on a physical printer. Just press "1" to print a receipt on the printer you have entered in settings.py. Note: this has only been tested on linux.

-------------

**Keyboard shortcuts:**

[Delete] = Delete all products and create a new empty receipt.

[Backspace] = Delete the last scanned product.

[Enter] = All prizes will be added up and placed at the bottom of the receipt.

[1] = Print the receipt on the printer you set in settings.py

-------------
**I hope this program is useful for you. I like to receive feedback for improvements or bugs.**


![alt text](https://github.com/MarijnInventor/Qr-Pos/blob/Version-1.0/qrpos%20screenshot.png?raw=true)
