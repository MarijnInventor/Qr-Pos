import platform
from getSettings import receiptFile,printername
import tkinter as tk
from tkinter import messagebox as msgb



def showMessage(message):
    root = tk.Tk()
    root.withdraw()
    if message == 1:
        root.after(3000, root.destroy)
        msgb.showinfo('Print job started!', 'The print job has been sent successfully', master=root)
    if message == 2:
        msgb.showwarning('Printing failed!', 'This feature only works on Winsows and Linux. If you are using one of these, please share this issue on Github so that this bug can be fixed in the next version of QR-Pos. You can do it here: https://github.com/MarijnInventor/Qr-Pos/issues', master=root)
    


os_name = platform.system()

if os_name == "Linux":
    import os
    os.system("lpr -P " + printername + " " + receiptFile)
    showMessage(message=1)
    
elif os_name == "Windows":
    import subprocess
    subprocess.Popen(['AcroRd32.exe', '/t', receiptFile, printername], shell=True)
    showMessage(message=1)

else:
    showMessage(message=2)
    


#alternative code for printing from linux:

# from sh import lp               #this is for printing with linux
# lp_cp = lp.bake('-d')           #this is for printing with linux
# lp_cp (printername, receiptFile)#this is for printing with linux