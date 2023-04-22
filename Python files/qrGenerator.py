import tkinter as tk
from tkinter import *
from tkinter import messagebox
import qrcode
from tkinter import filedialog

def qrGenerator():
    startNr = 1001
    lastNr = 0
    currentNr = 0
    finished = 0
    
    window = tk.Tk()
    window.geometry("400x100")  # Size of the window 
    window.title("QR generator for QR-POS")  # Adding a title
    window.configure(background='grey')
    
    
    label=tk.Label(window,text='        Number of QR codes to generate',bg="grey")
    label.grid(row=0,column=0,columnspan=2)
    
    usr_input=tk.Entry(window,font=22,width=15)
    usr_input.grid(row=2,column=1,padx=10,pady=10)
    
    button=tk.Button(window,font=22,text='Generate',command=lambda: generate())
    button.grid(row=2,column=2,padx=5,pady=10)
    
    usr_input.focus()
    def generate():
        folder = filedialog.askdirectory() + '/'
        lastNr = int(usr_input.get()) + 1000
        currentNr = startNr
        finished = 0
        if(lastNr < 1001):
            print("Error - LastNr must be between 1001 and 5000")
            tk.messagebox.showerror(title='Error', message='Error - LastNr must be between 1001 and 5000')
        elif(lastNr > 5000):
            print("Error - LastNr must be between 1001 and 5000")
            tk.messagebox.showerror(title='Error', message='Error - LastNr must be between 1001 and 5000')
        else:
            label=tk.Label(window,text='Generating...')
            label.grid(row=4,column=2,columnspan=2)
    
    
            while finished == 0:
                if(currentNr < lastNr):
                    finished = 0
                else:
                    finished = 1
                    label=tk.Label(window,text='        Done        ')
                    label.grid(row=4,column=2,columnspan=2)
                    tk.messagebox.showinfo("Finished", "Your QR codes are succesfully generated: 1001 - " + str(lastNr))
    
                filename = str(currentNr) + ".png"
                img = qrcode.make(currentNr)
                img.save(folder + filename)
                currentNr += 1
    
    window.mainloop()
    
if __name__ == "__main__":
    qrGenerator()
