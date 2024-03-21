import tkinter as tk
from tkinter import ttk, messagebox
import tkinter.font as font
from PIL import Image, ImageTk

root = tk.Tk()
root.title("đang học")
root.resizable(False, False)
im = Image.open('D:\pythontraining\day_1\logo.png')
photo = ImageTk.PhotoImage(im)
root.wm_iconphoto(True, photo)

customfont = ttk.Style()
style_name = "custom.TButton" 
customfont.configure(style_name,font=('Helvetica', 12), background='green')


def display(number):
    messagebox.showinfo("Notify",f"Kết quả là {number}")

m=3
k = 1
for i in range(m):
    for j in range(m):
        btn1 = ttk.Button(root, text=f"btn{k}", style=style_name, command=lambda a=k:display(a))
        btn1.grid(row=i, column=j,padx=2, pady=3)
        k+=1

root.mainloop()
