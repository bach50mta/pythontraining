from tkinter import Tk, Button

window = Tk() # mở ra cửa sổ
window.geometry("400x400+300+100")
window.title("My app")

def click():
    if button1["state"] == "normal":
        button1["state"] = "disabled"
    else:
        button1["state"] = "normal"

# Đưa các widget vào cửa sổ
style_button = {
    "activebackground": "white",
    "activeforeground": "blue",
    "bd": 5,
    "font": ("arial", 14, "bold"),
    "foreground": "red",
    "background": "yellow",
    "highlightbackground": "white",
    "highlightcolor": "black",
    "underline": 0,
}

button1 = Button(window, text="Click me", **style_button)
button1.pack()

button2 = Button(window, text="Click me too", **style_button)
button2.pack()

button2 = Button(window, text="Click me too", **style_button, command=click)
button2.pack()

window.mainloop()