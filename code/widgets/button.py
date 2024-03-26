from tkinter import Button, Tk

window = Tk()
window.geometry("400x400+300+100")
window.title("My app")

def click():
    btn.configure(text="Clicked" ,state="disabled")
    print("button click")


style_btn = {
    "font": ("Arial", 14),
    "bg": "light blue",
    "fg": "white",
}

btn = Button(window, text="Click me", **style_btn, command=click)
btn.pack()





window.mainloop()