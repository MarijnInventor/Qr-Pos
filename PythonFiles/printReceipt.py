import platform
from getSettings import receiptFile,printername
import tkinter as tk
from CTkMessagebox import CTkMessagebox



def showMessage(message):
    root = tk.Tk()
    root.withdraw()
    if message == 1:
        root.after(1500, root.destroy)
        CTkMessagebox(title="Print job started!", message="The print job has been sent successfully")
    if message == 2:
        CTkMessagebox(title="Printing failed!", message="Error\nThis feature only works on Winsows and Linux.",icon="cancel")


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