import tkinter as tk
from tkinter import ttk
from tkinter import * 
import configparser
import os
import cv2
from getSettings import configFile
from tkinter import messagebox as msgb


def changeSettings():
    def save_config():
        currency = currencyInput.get()
        printer_name = PrinternameInput.get()
        cam_source = camsourceInput.get()
        firstlogo = text_box.get("1.0", END)
        logo = firstlogo.replace(" ", "~")

        config['SETTINGS'] = {
            'currency': currency,
            'printer_name': printer_name,
            'cam_source' : cam_source,
            'logo': logo
        }

        with open(configFile, 'w') as configfile:
            config.write(configfile)


        root = tk.Tk()
        root.withdraw()
        w = tk.Toplevel(root)
        w.overrideredirect(True)
        w.geometry("300x100+{}+{}".format(
            root.winfo_screenwidth() // 2 - 150, 
            root.winfo_screenheight() // 2 - 50))
        label = tk.Label(w, text="Your settings are saved. \n Please restart the system \n to use the new changes.")
        label.pack(padx=50, pady=20)
        w.after(3000, w.destroy)
        w.mainloop()




    config = configparser.ConfigParser()
    if os.path.exists(configFile):
        config.read(configFile)
    else:
        print('Configuration file not found.')
        tk.messagebox.showerror(title="Failed", message="The configuration file is not found",)


    root = Tk()

    root.geometry('385x430')
    root.maxsize(385,430)
    root.configure(background='grey')
    root.title('QR-Pos settings')
    currencyOptions = ['€','$','£','¥','USD ']

    Label(root, text='Currency', bg='#CFCFCF', font=('arial', 12, 'normal')).place(x=18, y=21)

    currencyInput = ttk.Combobox(root, values=currencyOptions, width=7, state='readonly')
    currencyInput.place(x=168, y=21)
    currentCurrency = config.get('SETTINGS', 'currency')
    currencyInput.current(currencyOptions.index(currentCurrency))

    Label(root, text='Printer name', bg='#CFCFCF', font=('arial', 12, 'normal')).place(x=18, y=51)

    PrinternameInput=Entry(root)
    PrinternameInput.place(x=168, y=51)
    currentPrinter = config.get('SETTINGS', 'printer_name').split(', ')
    PrinternameInput.insert(0, currentPrinter)

    Label(root, text='Camera source', bg='#CFCFCF', font=('arial', 12, 'normal')).place(x=18, y=81)

    camera_sources = []
    for i in range(10):
        cap = cv2.VideoCapture(i)
        if cap.isOpened():
            camera_sources.append(i)
        cap.release()
    
    currentcam = int(config.get('SETTINGS', 'cam_source'))
    if currentcam not in camera_sources:
        camera_sources.append(currentcam)
    
    camera_sources.sort()
    camsourceInput = ttk.Combobox(root, values=camera_sources, width=7, state='readonly')
    camsourceInput.place(x=168, y=81)
    camsourceInput.current(camera_sources.index(currentcam))


    Label(root, text='Logo', bg='#CFCFCF', font=('arial', 12, 'normal')).place(x=170, y=120)

    text_box = Text(root,height=13,width=40,undo=True)
    text_box.place(x=30,y=151)

    firstcurrentlogo = config.get('SETTINGS', 'logo')
    currentLogo = firstcurrentlogo.replace("~", " ")
    text_box.insert("1.0", currentLogo)


    button = tk.Button(root, text='Save settings', command=save_config)
    button.place(x=135,y=380)


    root.mainloop()

if __name__ == "__main__":
    changeSettings()

