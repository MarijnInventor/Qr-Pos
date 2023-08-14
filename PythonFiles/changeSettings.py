import tkinter as tk
from tkinter import ttk
from tkinter import *
import customtkinter
import configparser
import os
import cv2
from getSettings import configFile
from tkinter import messagebox
import time


def changeSettings():
    def save_config():
        button.configure(text="   Saving...     ")
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
            button.configure(text="      Saved      ")
            root.after(3000, lambda: button.configure(text="Save settings"))


    config = configparser.ConfigParser()
    if os.path.exists(configFile):
        config.read(configFile)
    else:
        print('Configuration file not found.')
        tk.messagebox.showerror(title="Failed", message="The configuration file is not found")
                                                
    



    customtkinter.set_appearance_mode("dark")
    customtkinter.set_default_color_theme("blue")
    root = customtkinter.CTk()
    root.geometry("385x430")
    root.maxsize(385,430)
    root.title("QR-Pos settings")
    
    currencyOptions = ['€','$','£','¥','USD ']
    
    
    
    #Label(root, text='Currency', bg='#CFCFCF', font=('arial', 12, 'normal')).place(x=18, y=21)
    Label1 = customtkinter.CTkLabel(master=root, justify=customtkinter.LEFT, text='Currency')
    Label1.pack(pady=10, padx=10)
    Label1.place(x=18, y=21)
    
    
    #currencyInput = ttk.Combobox(root, values=currencyOptions, width=7, state='readonly')
    #currencyInput.place(x=168, y=21)
    currencyInput = customtkinter.CTkComboBox(root, values=currencyOptions, state='readonly')
    currencyInput.pack(pady=10, padx=10)
    currencyInput.place(x=168, y=21)

    currentCurrency = config.get('SETTINGS', 'currency')
    if currentCurrency not in currencyOptions:
        currencyInput.set('€')
    else:
        currencyInput.set(currentCurrency)
        


    #Label(root, text='Printer name', bg='#CFCFCF', font=('arial', 12, 'normal')).place(x=18, y=51)
    Label2 = customtkinter.CTkLabel(master=root, justify=customtkinter.LEFT, text='Printer name')
    Label2.pack(pady=10, padx=10)
    Label2.place(x=18, y=51)
    

    #PrinternameInput=Entry(root)
    #PrinternameInput.place(x=168, y=51)
    PrinternameInput = customtkinter.CTkEntry(master=root)
    PrinternameInput.pack(pady=10, padx=10)
    PrinternameInput.place(x=168, y=51)
    currentPrinter = config.get('SETTINGS', 'printer_name').split(', ')
    PrinternameInput.insert(0, currentPrinter)

    #Label(root, text='Camera source', bg='#CFCFCF', font=('arial', 12, 'normal')).place(x=18, y=81)
    Label3 = customtkinter.CTkLabel(master=root, justify=customtkinter.LEFT, text='Camera source')
    Label3.pack(pady=10, padx=10)
    Label3.place(x=18, y=81)

    camera_sources = []
    for i in range(10):
        cap = cv2.VideoCapture(i)
        if cap.isOpened():
            camera_sources.append(i)
        cap.release()
    
    currentcam = int(config.get('SETTINGS', 'cam_source'))
    if currentcam not in camera_sources:
        camera_sources.append('None')

    camera_sources = [str(src) for src in camera_sources]

    camera_sources.sort()
    camsourceInput = customtkinter.CTkComboBox(master=root, values=camera_sources, state='readonly')
    camsourceInput.pack(pady=10, padx=10)
    camsourceInput.place(x=168, y=81)
    camsourceInput.set(str(currentcam))

    

    #Label(root, text='Logo', bg='#CFCFCF', font=('arial', 12, 'normal')).place(x=170, y=120)
    Label4 = customtkinter.CTkLabel(master=root, justify=customtkinter.LEFT, text='Logo')
    Label4.pack(pady=10, padx=10)
    Label4.place(x=170, y=120)
    
    text_box = Text(root,height=13,width=40,undo=True)
    text_box.place(x=30,y=151)

    firstcurrentlogo = config.get('SETTINGS', 'logo')
    currentLogo = firstcurrentlogo.replace("~", " ")
    text_box.insert("1.0", currentLogo)


    #button = tk.Button(root, text='Save settings', command=save_config)
    button = customtkinter.CTkButton(master=root, command=save_config, text='Save settings')
    button.pack(pady=10, padx=10)
    button.place(x=125,y=385)


    root.mainloop()

if __name__ == "__main__":
    changeSettings()



