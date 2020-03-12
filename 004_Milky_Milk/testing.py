from tkinter import *

window = Tk()
window.title('test')
window.configure(bg="#5c455a")
window.geometry("400x400+100+100")


listbox = Listbox(window)
listbox.grid(row=1, column=1)

for e in range(10):
    listbox.insert(END, str(e))

window.mainloop()
