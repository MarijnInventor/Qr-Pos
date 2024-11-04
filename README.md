# Installation
Please keep in mind that the installation is made for Windows.
A successful installation on Linux is not guaranteed, but it is possible with some adjustments.


1. *Install python* - Please click [here](https://www.microsoft.com/store/productId/9NRWMJP3717K?ocid=pdpshare) to install Python 3.11 from the Microsoft store.
2. *Download Qr-Pos* - Scroll to the top of this page and click on the green "Code" button, then click Download zip. When donwnloaded, right-click the folder and press unpack. In windows 11, it may be necessary to first click more, then the unpack option is also there. Now select a folder such as documents to place the files. Place it somewhere it doesn't bother you. Now, click ok, then unpack and when done close the window.
3. *Install some requirements* - Now, navigate into the Qr-Pos folder with the explorer app. Right click somewhere and click "Open in terminal". A new window will open. Please copy the command below, paste it into the window you just opened, and press enter. When you see someithing like "C:\users\YourName", the command is done executing and the system is ready to use, but don't close the window yet.

```bash
pip install -r requirements.txt
```
5. *Make a shortcut* - The last step is to make a shortcut. Type start pythonfiles and press enter. Search for a file called main.py and click it once, so don't double click it. Now, right click on it and then click on "Make shortcut". In windows 11 you first need to click on "More options". Now, you see a new file called "main - shortcut". Place this file on your desktop and rename the file so you know it starts Qr-Pos when you click it.

*Done!* - You can now close the cmd app. Start Qr-Pos by clicking on the shortcut on your desktop. If it asks how to open the file, select Python and click "always". Enjoy!



# Updating
I regularly improve the system with bug fixes and new features. It is therefore important to update occasionally.
The update function is currently not available but i'm working hard to make automatic updates possible.
