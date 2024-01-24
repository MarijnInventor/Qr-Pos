import tkinter as tk
from tkinter import *
from tkinter import messagebox
import qrcode
from tkinter import filedialog
import customtkinter
from CTkMessagebox import CTkMessagebox

def qrGenerator():
    startNr = 1001
    lastNr = 0
    currentNr = 0
    finished = 0
    

    customtkinter.set_appearance_mode("dark")  # Modes: "System" (standard), "Dark", "Light"
    customtkinter.set_default_color_theme("blue")  # Themes: "blue" (standard), "green", "dark-blue"

    window = customtkinter.CTk()
    window.geometry("300x140")
    window.maxsize(300,140)
    window.title("QR-Pos - Qr generator")
    
    
    label = customtkinter.CTkLabel(master=window, justify=customtkinter.CENTER, text='Number of QR codes to generate:')
    label.pack(pady=5, padx=10)
    
    usr_input = customtkinter.CTkEntry(master=window)
    usr_input.pack(pady=0, padx=10)
    
    button_1 = customtkinter.CTkButton(master=window, text='Generate',command=lambda: generate())
    button_1.pack(pady=10, padx=10)
    
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
#     usr_input=tk.Entry(window,font=22,width=15)
#     usr_input.grid(row=2,column=1,padx=10,pady=10)
#     
#     button=tk.Button(window,font=22,text='Generate',command=lambda: generate())
#     button.grid(row=2,column=2,padx=5,pady=10)
#     
    usr_input.focus()
    def generate():
        folder = filedialog.askdirectory() + '/'
        lastNr = int(usr_input.get()) + 1000
        currentNr = startNr
        finished = 0
        if(lastNr < 1001):
            print("Error - LastNr must be between 1001 and 5000")
            CTkMessagebox(title='Error', message='Error - LastNr must be between 1001 and 5000')
        elif(lastNr > 5000):
            print("Error - LastNr must be between 1001 and 5000")
            CTkMessagebox(title='Error', message='Error - LastNr must be between 1001 and 5000')
        else:
            button_1.configure(text="Done")
            window.after(1500, lambda: button_1.configure(text="Generate"))
    
    
            while currentNr <= lastNr:
                filename = str(currentNr) + ".png"
                img = qrcode.make(currentNr)
                img.save(folder + filename)
                currentNr += 1

            CTkMessagebox(title="Finished", message="Your QR codes are succesfully generated: 1001 - " + str(lastNr))
    
    window.mainloop()
    
if __name__ == "__main__":
    qrGenerator()
