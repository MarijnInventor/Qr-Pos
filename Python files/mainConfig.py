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
from tkinter import messagebox as msgb

line = '________________________________________'

def main():
    menuwindow=tk.Tk()
    menuwindow.title("QR-Pos toolbox")
    menuwindow.geometry("400x100")
    menuwindow.config(background='grey')
    menuwindow.resizable(0, 0)
    undoButton = Button(menuwindow,text='Add products',width=10,height=2,command=addProducts).pack(pady=20,side = LEFT,expand=True)
    clearButton = Button(menuwindow,text='QR generator',width=10,height=2,command=qrGenerator).pack(pady=20,side = LEFT,expand=True)
    moreButton = Button(menuwindow,text='Settings',width=10,height=2,command=changeSettings).pack(pady=20,side = LEFT,expand=True)
    menuwindow.mainloop()

if __name__ == '__main__':
    main()
