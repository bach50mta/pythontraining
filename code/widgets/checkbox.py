from tkinter import Tk, Checkbutton, IntVar, StringVar, BooleanVar

window = Tk()
window.geometry("400x400+300+100")
window.title("My app")

check_box_value = BooleanVar()
check_box = Checkbutton(window, text="Python", variable=check_box_value, 
                        onvalue=True, offvalue=False, command=lambda:print(check_box_value.get()))
check_box.pack()





window.mainloop()