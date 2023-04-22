# Qr-Pos
A simple point of sale system with a qr code for each product.

The purpose of this project is to make a well-functioning POS system that everyone can use for free.

-------------
# Installation

1. Click on the green "Code" button and click on Download zip
2. Unpack the zip folder and place it wherever you want
3. Copy the path to requirements.txt
4. Open a terminal (command prompt for windows) and type cd, followed by a space and your path. Then press enter.
5. Type "pip install requirements.txt" and press enter again.
6. When it is finished, you can use the system by clicking main.py for the POS system and mainConfig.py for the rest.

-------------
# Preparation
**Preparation step 1:**

When you have downloaded all the files, launch qrGenerator.py to generate some QR codes.  Enter the number of required qr codes and then click on generate to generate them. Select the folder where the qr codes should be placed. After a very short time you will see "Done!" under the generate button. Then everything is done and you can close the program. Print your qr codes on paper so you can scan them.

**Preparation step 2:**

Now it's time to add your products. When you have applied a qr code to each product, you can open mainConfig.py and click add products. Scan a qr code, type in the name and price and click add. Repeat this for each product. For removing products, there is no function yet, so if you want to remove or change a product, you can open products.xlsx and remove or change it manually.

**Preparation step 3:**

Finally, edit your currency, printer, camera source and logo. You can do this by opening mainConfig.py and open the settings menu. Change it to what you want and then click the save settings button at the bottom of the window.

-------------
# Usage

When you run main.py the UI will open. You'll see 2 windows. The first window shows what the webcam sees. Ajust the position so that the camera can see the place where the qr codes are going to be scanned.
You can minimalize the window so you can see the actual UI. The UI contains a box where the scanned products appear, with your logo at the top, and some buttons. 

**These are the functions of the buttons:**

Pay = All prizes will be added up and placed at the bottom of the receipt.

Undo = Delete the last scanned product.

Clear = Delete all products and create a new session.

There is also a function to print the receipt on a physical printer. Just press "1" to print a receipt on the printer you have selcted in the settings file. Note: this has only been tested on linux, but windows is also supported.

-------------

**Keyboard shortcuts:**

[Delete] = Delete all products and create a new empty receipt.

[Backspace] = Delete the last scanned product.

[Enter] = All prizes will be added up and placed at the bottom of the receipt.

[p] = Print the receipt on the printer you selected in the settings.

-------------
**I hope this program is useful for you. I like to receive feedback for improvements or bugs.**

