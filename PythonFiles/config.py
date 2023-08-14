from getSettings import productsFile,receiptFile,beep,logo,currency,camsource
import tkinter as tk
from tkinter import *
import cv2
import numpy as np
import pyzbar.pyzbar as pyzbar
import threading
from playsound import playsound
import time
from SearchForProductNr import searchForProductNr
from qrGenerator import qrGenerator
from changeSettings import changeSettings
from addproduct import addProducts
import subprocess
import os
import signal
import customtkinter

stopall = False

runningap = False
runningqg = False
runningcs = False


line = '________________________________________'

def exitSettings():
    if runningap:
        ap.terminate()
    if runningqg:
        qg.terminate()
    if runningcs:
        cs.terminate()
    
    stopall = True
    subprocess.Popen(["python3", "main.py"])
    os._exit(0)
    
def ap():
    global ap
    runningap = True
    ap = subprocess.Popen(["python", "addproduct.py"])
    
def qg():
    global qg
    runningqg = True
    qg = subprocess.Popen(["python", "qrGenerator.py"])
    
def cs():
    global cs
    runningcs = True
    cs = subprocess.Popen(["python", "changeSettings.py"])





customtkinter.set_appearance_mode("dark")  # Modes: "System" (standard), "Dark", "Light"
customtkinter.set_default_color_theme("blue")  # Themes: "blue" (standard), "green", "dark-blue"
menuwindow = customtkinter.CTk()
menuwindow.geometry("500x100")
menuwindow.title("QR-Pos toolbox")
menuwindow.resizable(0, 0)

undoButton = customtkinter.CTkButton(master=menuwindow, command=addProducts, width=100, height=100, text='Add products')
undoButton.pack(pady=20,side = LEFT,expand=True)
qrGenerator = customtkinter.CTkButton(master=menuwindow, command=qrGenerator, width=100, height=100, text='QR generator')
qrGenerator.pack(pady=20,side = LEFT,expand=True)
settingsButton = customtkinter.CTkButton(master=menuwindow, command=changeSettings, width=100, height=100, text='Settings')
settingsButton.pack(pady=20,side = LEFT,expand=True)
exitButton = customtkinter.CTkButton(master=menuwindow, command=exitSettings, width=100, height=100, text='Exit')
exitButton.pack(pady=20,side = LEFT,expand=True)

menuwindow.mainloop()

# menuwindow=tk.Tk()
# menuwindow.title("QR-Pos toolbox")
# menuwindow.geometry("500x100")
# menuwindow.config(background='grey')
# menuwindow.resizable(0, 0)
# undoButton = Button(menuwindow,text='Add products',width=10,height=2,command=addProducts).pack(pady=20,side = LEFT,expand=True)
# clearButton = Button(menuwindow,text='QR generator',width=10,height=2,command=qrGenerator).pack(pady=20,side = LEFT,expand=True)
# moreButton = Button(menuwindow,text='Settings',width=10,height=2,command=changeSettings).pack(pady=20,side = LEFT,expand=True)
# exitButton = Button(menuwindow,text='Exit',width=10,height=2,command=exitSettings).pack(pady=20,side = LEFT,expand=True)
# menuwindow.mainloop()

