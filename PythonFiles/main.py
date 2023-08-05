from getSettings import productsFile,receiptFile,beep,logo,currency,camsource
import tkinter as tk
import customtkinter
from tkinter import *
import cv2
import sys
import os
import subprocess
import numpy as np
import pyzbar.pyzbar as pyzbar
import threading
from playsound import playsound
import time
from SearchForProductNr import searchForProductNr
from tkinter import messagebox as msgb

line = '________________________________________'

customtkinter.set_appearance_mode("dark")  # Modes: system (default), light, dark
customtkinter.set_default_color_theme("blue")  # Themes: blue (default), dark-blue, green


def main():
    window=customtkinter.CTk()
    window.title("QR POS")
    window.geometry("500x500")
    window.maxsize(500,500)
    price = 0.00
    product = 'INVALID'
    message = ""
    text_box = Text(window,height=13,width=40,undo=True)
    text_box.pack(expand=True)
    text_box.config(state=DISABLED)
    
    

    prices = []
    total = 0.00
    
        
        
    def undo():
        if(prices == []):
            print("Undo not possible")
        else:
            ele= prices.pop() #remove latest item from the prices list
            print("Latest product deleted")
            
            with open(receiptFile, "r") as receipt:
                currentText = receipt.read()
                m=currentText.split("\n")
                new="\n".join(m[:-3])
                
            with open(receiptFile, "w") as receipt:
                for i in range(len(new)):
                    receipt.write(new[i])
                    
            writeinfile("") #don't write anything, just execute this to change currentText
            text_box.configure(state=NORMAL)
            text_box.delete(1.0, 'end')
            text_box.insert(INSERT, new)
            text_box.see("end")
            text_box.config(state=DISABLED)
            


    def scan():
        lastProduct = ''
        lastTime = 0.0

        cap = cv2.VideoCapture(int(camsource))
        font = cv2.FONT_HERSHEY_PLAIN

        while True:
            _, frame = cap.read()

            decodedObjects = pyzbar.decode(frame)
            for obj in decodedObjects:
                qrContent = obj.data
                price, product = searchForProductNr(qrContent)
                textToWrite = product + '  -  ' + currency + str(price)
                t = time.time()
                if product != lastProduct or (t - lastTime) >= 1:
                    prices.append(price)
                    priceText = "{:.2f}".format(price)
                    message = '\n' + product + '\n' +  currency + priceText + '\n' + line
                    writeText(message)
                    print("price: " + currency + priceText + "   |   name: " + product)
                        
                lastTime = t
                lastProduct = product

                cv2.putText(frame, "price: " + priceText + "   name: " + product, (50, 50), font, 2, (255, 0, 0), 3)
                
            cv2.imshow("QR-Pos scanning window", frame)
            key = cv2.waitKey(1)


            if cv2.getWindowProperty('QR-Pos scanning window',cv2.WND_PROP_VISIBLE)<1:
                break
        cv2.destroyAllWindows()
    
    def startScan():
        x = threading.Thread(target=scan, args=())
        x.start()


    def payment():
        total = sum(float(t) for t in prices)
        message = '\n\nTotal: ' + currency + "{:.2f}".format(total) + "\n"
        text_box.configure(state=NORMAL)
        text_box.insert(INSERT, message)
        text_box.see("end")
        text_box.config(state=DISABLED)
        writeinfile(message)
        

    def clear():
        prices.clear()
        price = 0.00
        with open(receiptFile, "w") as receipt:
            receipt.seek(0) # rewind
            receipt.write(logo + "\n" + line) # write the new line before
        with open(receiptFile, "r") as receipt:
            currentText = receipt.read()
            
        text_box.configure(state=NORMAL)
        text_box.delete(1.0, 'end')
        text_box.insert(INSERT, currentText)
        text_box.configure(state=DISABLED)

    def writeinfile(text):
        with open(receiptFile, "r") as receipt:
            currentText = receipt.read() # read everything in the file
        with open(receiptFile, "w") as receipt:
            receipt.seek(0) # rewind
            receipt.write(currentText + text) # write the new stuff

    def writeText(text):
        playsound(beep)
        writeinfile(text)
        with open(receiptFile, "r") as receipt:
            currentText = receipt.read()
            
        text_box.configure(state=NORMAL)
        text_box.delete(1.0, 'end')
        text_box.insert(INSERT, currentText)
        text_box.see("end")
        text_box.config(state=DISABLED)
        
    
    
    def printReceipt():
        import printReceipt
        
    def openMenu():
        subprocess.Popen(["python3", "config.py"])
        os._exit(0)
        
        

    clear()
    startScan()
    payButton = customtkinter.CTkButton(master=window,text='Pay',command=payment)
    payButton.place(relx=0.35, rely=0.85,anchor=tk.CENTER)
    undoButton = customtkinter.CTkButton(master=window,text='Undo',command=undo)
    undoButton.place(relx=0.65, rely=0.85,anchor=tk.CENTER)
    clearButton = customtkinter.CTkButton(master=window,text='Clear',command=clear)
    clearButton.place(relx=0.35, rely=0.92,anchor=tk.CENTER)
    moreButton = customtkinter.CTkButton(master=window,text='Settings',command=openMenu)
    moreButton.place(relx=0.65, rely=0.92,anchor=tk.CENTER)

    
    window.bind("<Return>", (lambda event: payment()))
    window.bind("<BackSpace>", (lambda event: undo()))
    window.bind("<Delete>", (lambda event: clear()))
    window.bind("p", (lambda event: printReceipt()))
    window.mainloop()

if __name__ == '__main__':
    main()
