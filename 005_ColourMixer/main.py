from tkinter import *

master = Tk()


def test(decimal):
    red = r.get()
    green = g.get()
    blue = b.get()

    red = hex(red).split('x')[-1]
    green = hex(green).split('x')[-1]
    blue = hex(blue).split('x')[-1]

    if len(red) == 1:
        red = '0' + red
    if len(green) == 1:
        green = '0' + green
    if len(blue) == 1:
        blue = '0' + blue

    mix = '#' + str(red) + str(green) + str(blue)
    mixed_label['bg'] = mix
    hex_label['text'] = mix


hex_label = Label(text='#ffffff')
hex_label.grid(row=2, column=3)

mixed_label = Label(bg='#ffffff')
mixed_label.grid(row=1, column=3, ipadx=100, ipady=100)

r = Scale(master, from_=0, to=255, orient=HORIZONTAL, command=test, fg='red')
r.grid(row=0, column=1)
g = Scale(master, from_=0, to=255, orient=HORIZONTAL, command=test, fg='green')
g.grid(row=1, column=1)
b = Scale(master, from_=0, to=255, orient=HORIZONTAL, command=test, fg='blue')
b.grid(row=2, column=1)


master.mainloop()
