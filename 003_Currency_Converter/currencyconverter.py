from tkinter import *
from money import Money


def usd():
    # retrieves the value from the input box and assigns it to a variable
    number1 = float(inpNumber1.get())
    result = number1 * 0.66
    # assigns the result variable to the text variable
    lblResult.config(text="$" + result)


def euro():
    # retrieves the value from the input box and assigns it to a variable
    number1 = float(inpNumber1.get())
    result = number1 * 0.61
    # assigns the result variable to the text variable
    lblResult.config(text=result)


def aud():
    number1 = float(inpNumber1.get())
    result = number1 * 1
    lblResult.config(text="$" + result)


def jpy():
    number1 = float(inpNumber1.get())
    result = number1 * 73.92
    lblResult.config(text=result)


def venz():
    number1 = float(inpNumber1.get())
    result = 0
    lblResult.config(text=result)


def sru():
    number1 = float(inpNumber1.get())
    result = number1 * 119.94
    lblResult.config(text=result)


def ngd():
    number1 = float(inpNumber1.get())
    result = number1 * 239.96
    lblResult.config(text=result)


Form = Tk()
Form.title("Currency Converter")
Form.configure(bg="teal")
Form.geometry("350x500+1000+300")

inpNumber1 = Entry(Form, font=("default", 14))
inpNumber1.place(x=100, y=100, width=150, height=30)

lblResult = Label(Form, text="Result", font=("default", 14), bg='yellow')
lblResult.place(x=100, y=200, width=150, height=30)

usdBtn = Button(Form, text="USD", fg="Blue", bg="black", command=usd)
usdBtn.place(x=35, y=255, width=275, height=30)

euroBtn = Button(Form, text="EURO", fg="Blue", bg="black", command=euro)
euroBtn.place(x=35, y=285, width=275, height=30)

jpyBtn = Button(Form, text="JPY", fg="Blue", bg="black", command=jpy)
jpyBtn.place(x=35, y=310, width=275, height=25)

venvBtn = Button(
    Form, text="VENZ", fg="Blue", bg="black", command=venz)
venvBtn.place(x=35, y=335, width=275, height=25)

sriBtn = Button(Form, text="SRU", fg="Blue", bg="black", command=sru)
sriBtn.place(x=35, y=360, width=275, height=25)

ngdBtn = Button(Form, text="NGD", fg="Blue", bg="black", command=ngd)
ngdBtn.place(x=35, y=385, width=275, height=25)

Form.mainloop()
