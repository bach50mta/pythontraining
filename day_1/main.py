import tkinter as tk
from tkinter import ttk
from tkinter import messagebox


def on_click():
    try:
        input_string=txt.get("1.0","end-1c")
        print(input_string)
        tk.Label(root, text=str(eval(input_string))).pack()
        txt.delete(1.0,tk.END)
    except Exception as e:
        messagebox.showerror("error", str(e))


root = tk.Tk()
root.title("App demo")
root.geometry("300x300+200+200")

label = tk.Label(root, text="Input")
label.pack()

txt = tk.Text(root, width=30, height=2)
txt.pack()

btn= ttk.Button(root, text="click", command=on_click)
btn.pack(pady=10 )
               
root.mainloop()