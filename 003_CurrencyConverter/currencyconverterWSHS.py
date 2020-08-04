from tkinter import *
from currency_converter import CurrencyConverter

c = CurrencyConverter()


def usd():
    number1 = float(inpNumber1.get())
    result = c.convert(number1, 'AUD', 'USD')
    lblResult.config(text="$" + str(round(result, 2)))


def euro():
    number1 = float(inpNumber1.get())
    result = c.convert(number1, 'AUD', 'EUR')
    lblResult.config(text="$" + str(round(result, 2)))


def jpy():
    number1 = float(inpNumber1.get())
    result = c.convert(number1, 'AUD', 'JPY')
    lblResult.config(text="$" + str(round(result, 2)))


def sek():
    number1 = float(inpNumber1.get())
    result = c.convert(number1, 'AUD', 'SEK')
    lblResult.config(text="$" + str(round(result, 2)))


def gbp():
    number1 = float(inpNumber1.get())
    result = c.convert(number1, 'AUD', 'GBP')
    lblResult.config(text="$" + str(round(result, 2)))


def idr():
    number1 = float(inpNumber1.get())
    result = c.convert(number1, 'AUD', 'IDR')
    lblResult.config(text="$" + str(round(result, 2)))


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
    Form, text="SEK", fg="Blue", bg="black", command=sek)
venvBtn.place(x=35, y=335, width=275, height=25)

sriBtn = Button(Form, text="GBP", fg="Blue", bg="black", command=gbp)
sriBtn.place(x=35, y=360, width=275, height=25)

ngdBtn = Button(Form, text="IDR", fg="Blue", bg="black", command=idr)
ngdBtn.place(x=35, y=385, width=275, height=25)

Form.mainloop()
