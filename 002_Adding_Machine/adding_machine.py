from tkinter import *


def add():
    # retrieves the value from the input box and assigns it to a variable
    number1 = float(inpNumber1.get())
    number2 = float(inpNumber2.get())
    result = number1 + number2
    # assigns the result variable to the text variable
    lblResult.config(text=result)


def subtraction():
    # retrieves the value from the input box and assigns it to a variable
    number1 = float(inpNumber1.get())
    number2 = float(inpNumber2.get())
    result = number1 - number2
    # assigns the result variable to the text variable
    lblResult.config(text=result)


def multiplication():
    number1 = float(inpNumber1.get())
    number2 = float(inpNumber2.get())
    result = number1 * number2
    lblResult.config(text=result)


def division():
    number1 = float(inpNumber1.get())
    number2 = float(inpNumber2.get())
    try:
        result = number1/number2
        lblResult.config(text=result)
    except:
        ZeroDivisionError
        lblResult.config(text="ZeroDivisionError")


def clear():
    inpNumber1.delete(0, END)
    inpNumber2.delete(0, END)
    lblResult.config(text='')


# Design the Graphical User Interface (GUI)
# Build the form
Form = Tk()  # This creates a GUI and assigns it a name
Form.title("GUI Adding Machine")
Form.configure(bg="darkgrey")
# Sets the dimensions of the form, Length X Width, the X and Y coordinates
Form.geometry("350x500+1000+300")
# Create our form controls (the widgets/objects on the form, buttons, labels, inoutboxes, images, etc)
# input boxes
# set the name and style
inpNumber1 = Entry(Form, font=("default", 14))
inpNumber2 = Entry(Form, font=("default", 14))
# set its location and dimensions
inpNumber1.place(x=100, y=100, width=150, height=30)
inpNumber2.place(x=100, y=150, width=150, height=30)
# labels
lblResult = Label(Form, font=("default", 14), bg='cyan')
lblResult.place(x=100, y=200, width=150, height=30)
# buttons
# set name, style and assign a function to the command property
btnAdd = Button(Form, text="Add", fg="black", bg="white", command=add)

btnAddition = Button(Form, text="Addition", fg="black",
                     bg="white", command=add)
btnAddition.place(x=35, y=275, width=275, height=30)
# set its location and dimensions

btnSubtract = Button(Form, text="Subtract", fg="black",
                     bg="white", command=subtraction)
btnSubtract.place(x=35, y=300, width=275, height=25)
# set its location and dimensions

btnMultiplication = Button(Form, text="Multiplication",
                           fg="black", bg="white", command=multiplication)
btnMultiplication.place(x=35, y=325, width=275, height=25)
# set its location and dimensions

btnDivision = Button(Form, text="Division", fg="black",
                     bg="white", command=division)
btnDivision.place(x=35, y=350, width=275, height=25)
# set its location and dimensions

btnClear = Button(Form, text="Clear", fg="black", bg="white", command=clear)
btnClear.place(x=35, y=375, width=275, height=25)
# set its location and dimensions


# run the code
Form.mainloop()
