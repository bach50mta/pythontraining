from tkinter import Tk, Label, Button

window = Tk()
window.geometry("400x400+300+100")
window.title("My app")

style_label = {
    'font': ('Arial', 14),
    'bg': 'light blue',
    'fg': 'black',
}

def change():
    # label.configure(text='Ngon ngay')
    label.destroy()
    btn.configure(state='disabled')


label = Label(window, text="My app", **style_label)
label.pack()

btn = Button(window, text='Thay đổi lable', command=lambda:change())
btn.pack()




window.mainloop()