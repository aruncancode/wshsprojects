from tkinter import *

master = Tk()


def test(decimal):
    red = hex(r.get()).split('x')[-1]
    green = hex(g.get()).split('x')[-1]
    blue = hex(b.get()).split('x')[-1]

    if len(red) == 1:
        red = '0' + red
    if len(green) == 1:
        green = '0' + green
    if len(blue) == 1:
        blue = '0' + blue

    mix = '#' + str(red) + str(green) + str(blue)
    mixed_label['bg'] = mix
    hex_label['text'] = mix
    hex_label['fg'] = mix


hex_label = Label(text='#ffffff', fg='black', font=('Consolas', 25))
hex_label.grid(column=1)

mixed_label = Label(bg='#ffffff')
mixed_label.grid(column=1, ipadx=100, ipady=100)

r = Scale(master, from_=0, to=255, orient=HORIZONTAL, command=test, fg='red')
r.grid(column=1)
g = Scale(master, from_=0, to=255, orient=HORIZONTAL, command=test, fg='green')
g.grid(column=1)
b = Scale(master, from_=0, to=255, orient=HORIZONTAL, command=test, fg='blue')
b.grid(column=1)


master.title('Colour Mixer')
master.mainloop()
