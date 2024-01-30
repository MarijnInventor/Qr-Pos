# Installation
Please keep in mind that the installation is made for Windows.
A successful installation on Linux is not guaranteed, but it is possible with some adjustments.


1. *Install python* - Please click [here](https://www.microsoft.com/store/productId/9NRWMJP3717K?ocid=pdpshare) to install Python 3.11 from the Microsoft store.
2. *Install Git* - Next, you need to install Git. Click [here](https://github.com/git-for-windows/git/releases/download/v2.43.0.windows.1/Git-2.43.0-64-bit.exe) to download Git and then run the downloaded file. Leave everything at the default settings and press OK several times until you see an install button. After installation, proceed to step 3.
3. *Install QR-Pos* - Now, press the Windows key and R at the same time. Type cmd and press enter. Paste the following command in that app and press enter again.
```bash
git clone https://github.com/MarijnInventor/Qr-Pos
```
4. *Install some requirements* - When you see something like "C:\users\YourName>", the installation is done. Execute the following command and press enter.
```bash
cd Qr-Pos
```
Finally, paste this command and press enter again. It may take a while for this to be completed.
```bash
pip install -r requirements.txt
```
5. *Make a shortcut* - The last step is to make a shortcut. Type start pythonfiles and press enter. Search for a file called main.py and  click it once, so don't double click it. Now, right click on it and then click on "Make shortcut". In windows 11 you first need to click on "More options". Now, you see a new file called "main - shortcut". Place this file on your desktop and rename the file so you know it starts Qr-Pos when you click it.

*Done!* - You can now close all apps you just installed. Start Qr-Pos by clicking on the shortcut on your desktop. If it asks how to open the file, select Python and click "always". Enjoy!



# Updating
I regularly improve the system with bug fixes and new features. It is therefore important to update occasionally.
This can be done by pressing Windows key and R at the same time. Type cmd and press enter. Then, paste the command below and press enter again. When you see something like "C:\users\YourName>", the update is done.
```bash
git pull origin main
```
