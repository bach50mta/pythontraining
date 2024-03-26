from tkinter import Button, Tk
from tkinter.filedialog import askopenfile


window = Tk() # mở ra cửa sổ
window.geometry("400x400+300+100")
window.title("My app")

def on_browe():
    file = askopenfile(mode='r', filetype=[('text file', '*.txt')])
    print(file.read())

def print_number(n):
    print(n)



askfile_btn = Button(window, text="chọn file", command=lambda:on_browe())
askfile_btn.pack()

for i in range(10):
    btn = Button(window, text=f"btn{i}", command=lambda i=i: print_number(i))
    btn.pack()




window.mainloop()