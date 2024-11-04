import tkinter as tk
from tkinter import *
from tkinter import messagebox
import qrcode
from tkinter import filedialog
import customtkinter
from CTkMessagebox import CTkMessagebox
import os

lastNr = 0
currentNr = 0
finished = 0
startNr = 0


def qrGenerator():
    customtkinter.set_appearance_mode("dark")  # Modes: "System" (standard), "Dark", "Light"
    customtkinter.set_default_color_theme("blue")  # Themes: "blue" (standard), "green", "dark-blue"

    window = customtkinter.CTk()
    window.geometry("270x230")
    window.title("QR generator")
    
    
    label = customtkinter.CTkLabel(master=window, justify=customtkinter.CENTER, text='Number of QR codes to generate:')
    label.pack(pady=0, padx=10)
    
    numberOf = customtkinter.CTkEntry(master=window)
    numberOf.pack(pady=10, padx=10)

    label = customtkinter.CTkLabel(master=window, justify=customtkinter.CENTER, text='Starting with:')
    label.pack(pady=0, padx=10)
    
    startNr = customtkinter.CTkEntry(master=window)
    startNr.pack(pady=10, padx=10)
    
    button_1 = customtkinter.CTkButton(master=window, text='Generate',command=lambda: generate())
    button_1.pack(pady=20, padx=10)
    
    window.bind("<Return>", (lambda event: generate()))



    
#     window = tk.Tk()
#     window.geometry("400x100")  # Size of the window 
#     window.title("QR generator for QR-POS")  # Adding a title
#     window.configure(background='grey')
#     
#     
#     label=tk.Label(window,text='        Number of QR codes to generate',bg="grey")
#     label.grid(row=0,column=0,columnspan=2)
#     
#     numberOf=tk.Entry(window,font=22,width=15)
#     numberOf.grid(row=2,column=1,padx=10,pady=10)
#     
#     button=tk.Button(window,font=22,text='Generate',command=lambda: generate())
#     button.grid(row=2,column=2,padx=5,pady=10)
#     
    numberOf.focus()
    def generate():
        lastNr = int(startNr.get()) + int(numberOf.get())
        currentNr = int(startNr.get())
        finished = 0

        if(lastNr < 1001 or lastNr > 5000):
            print("Error - Make sure all numbers are within the range of 1001 and 5000")
            CTkMessagebox(title='Error', message="Error - Make sure all numbers are within the range of 1001 and 5000")
        else:
            button_1.configure(text="Done")
            window.after(1500, lambda: button_1.configure(text="Generate"))

        
            newfoldername = "qr-pos output"
            folder = filedialog.askdirectory()
            new_folder = os.path.join(folder, newfoldername)
            os.makedirs(new_folder, exist_ok=True)

            button_1.configure(text="Done")
            window.after(1500, lambda: button_1.configure(text="Generate"))
        

            while finished == 0:
                if(currentNr <= lastNr):
                    filename = str(currentNr) + ".png"
                    img = qrcode.make(currentNr)
                    img.save(new_folder + "/" + filename)
                    currentNr += 1
                else:
                    CTkMessagebox(title="Finished", message="Your QR codes are succesfully generated: \n" + str(startNr.get()) + " - " + str(lastNr))
                    return


    
    window.mainloop()
    
if __name__ == "__main__":
    qrGenerator()
