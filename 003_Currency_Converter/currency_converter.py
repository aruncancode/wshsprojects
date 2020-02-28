import time

from tkinter import *

def usd():
    number1 =float(inpNumber1.get()) # retrieves the value from the input box and assigns it to a variable
    result = number1 * 0.66
    lblResult.config(text="$" + result) # assigns the result variable to the text variable

def euro():
        number1 = float(inpNumber1.get())  # retrieves the value from the input box and assigns it to a variable
        result = number1 * 0.61
        lblResult.config(text=result)  # assigns the result variable to the text variable
def aud():
    number1 = float(inpNumber1.get())
    result = number1 * 1
    lblResult.config(text="$" + result)


def jpy():
    number1 = float(inpNumber1.get())
    result = number1 * 73.92
    lblResult.config(text=result)

def clear():
    number1 = float(inpNumber1.get())
    number2 = float(inpNumber2.get())
    result = number1 * number2 * 0
    inpNumber1.delete(0,END)
    inpNumber2.delete(0,END)
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

def paypal():
    number1 = float(inpNumber1.get())
    result = number1 * 1
    lblResult.config(text=("Enter your PayPal email!"))

Form = Tk()
Form.title("Currency Converter")
Form.configure(bg="black")
Form.geometry("350x500+1000+300")

inpNumber1 = Entry(Form, font =("default", 14))
inpNumber2 = Entry(Form, font =("default", 14))
# set its location and dimensions
inpNumber1.place (x=100, y=100, width=150, height=30)
# labels
lblResult = Label(Form, text="Result", font=("default", 14), bg='yellow')
lblResult.place(x=100, y=200, width=150, height=30)
# button
# set name, style and assign a function to the command property
btnAdd = Button(Form, text="USD", fg="black", bg="red", command=usd)

btnAddition = Button(Form, text="USD", fg="Blue", bg="black", command=usd)
btnAddition.place(x=35, y=255, width=275, height=30)

btnAddition = Button(Form, text="EURO", fg="Blue", bg="black", command=euro)
btnAddition.place(x=35, y=285, width=275, height=30)
# set its location and dimensions

btnSubtract = Button(Form, text="JPY", fg="Blue", bg="black", command=jpy)
btnSubtract.place(x=35, y=310, width=275, height=25)
# set its location and dimensions

btnMultiplication = Button(Form, text="VENZ", fg="Blue", bg="black", command=venz)
btnMultiplication.place(x=35, y=335, width=275, height=25)
# set its location and dimensions

btnDivision = Button(Form, text="SRU", fg="Blue", bg="black", command=sru)
btnDivision.place(x=35, y=360, width=275, height=25)
# set its location and dimensions

btnClear = Button(Form, text="NGD", fg="Blue", bg="black", command=ngd)
btnClear.place(x=35, y=385, width=275, height=25)

btnAddition = Button(Form, text="AUD (Base Amount)", fg="Blue", bg="black", command=aud)
btnAddition.place(x=35, y=50, width=275, height=30)

btnClear = Button(Form, text="HACK PAYPAL.exe", fg="Blue", bg="black", command=ngd)
btnClear.place(x=35, y=155, width=275, height=30)




# run the code
Form.mainloop() # OR mainloop()
