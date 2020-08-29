from tkinter import *
from PIL import Image, ImageTk
window = Tk()

window.title("Welcome to LikeGeeks app")

a = Label(window, bg="black", fg="white", text="hello").grid(row=1, column=1)
b = Button(window, text="button", fg="black").grid(row=1, column=2)

window.mainloop()
