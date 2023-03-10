from settings import receiptFile,beep,logo,currency
from printReceipt import printReceipt
import tkinter as tk
from tkinter import *
from tkinter import messagebox
import cv2
import numpy as np
import pyzbar.pyzbar as pyzbar
import threading
import simpleaudio as sa
import time
from SearchForProductNr import searchForProductNr

beepSound = sa.WaveObject.from_wave_file(beep)


def main():
    window=tk.Tk()
    window.title("QR POS")
    window.geometry("500x500")
    window.config(background='grey')
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

        cap = cv2.VideoCapture(0)
        font = cv2.FONT_HERSHEY_PLAIN

        while True:
            _, frame = cap.read()

            decodedObjects = pyzbar.decode(frame)
            for obj in decodedObjects:
                qrContent = obj.data
                price, product = searchForProductNr(qrContent)
                textToWrite = product + '  -  ' + currency + str(price)
                if(product == 'INVALID'):
                    print('No product found - QrValue = ' + str(qrContent))
                else:
                    t = time.time()
                    
                    if(product != lastProduct or (t - lastTime) >= 1):
                        prices.append(price)
                        priceText = "{:.2f}".format(price)
                        message = '\n' + product + '\n' +  currency + priceText + '\n________________________________________'
                        writeText(message)
                        print("price: " + currency + priceText + "   |   name: " + product)
                    cv2.putText(frame, "price: " + priceText + "   name: " + product, (50, 50), font, 2, (255, 0, 0), 3)

                    lastTime = t
                    lastProduct = product

            cv2.imshow("Frame", frame)
            
            key = cv2.waitKey(1)


            if cv2.getWindowProperty('Frame',cv2.WND_PROP_VISIBLE)<1:
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
            receipt.write(logo) # write the new line before
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
        beepSound.play()
        writeinfile(text)
        with open(receiptFile, "r") as receipt:
            currentText = receipt.read()
            
        text_box.configure(state=NORMAL)
        text_box.delete(1.0, 'end')
        text_box.insert(INSERT, currentText)
        text_box.see("end")
        text_box.config(state=DISABLED)

    clear()
    startScan()
    #The textbox is defined at the beginning of the code
    payButton = Button(window,text='Pay',width=15,height=2,command=payment).pack(expand=True)
    undoButton = Button(window,text='Undo',width=15,height=2,command=undo).pack(expand=True)
    clearButton = Button(window,text='Clear',width=15,height=2,command=clear).pack(expand=True)
    window.bind("<Return>", (lambda event: payment()))
    window.bind("<BackSpace>", (lambda event: undo()))
    window.bind("<Delete>", (lambda event: clear()))
    window.bind("<KP_1>", (lambda event: printReceipt()))
    window.mainloop()

if __name__ == '__main__':
    main()
