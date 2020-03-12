from tkinter import *


window = Tk()
window.title("Milky Milk")
window.configure(bg="#5c455a")
window.geometry("400x400+100+100")


def total():
    total_cost = 0
    cheesetotal = cheese_label_input.get()
    yoghurttotal = yoghurt_label_input.get()
    beeftotal = beef_label_input.get()
    buttertotal = butter_label_input.get()
    milktotal = milk_label_input.get()

    if milktotal != '':
        milk_label_total.configure(text="$" + str(int(milktotal) * 3))
        total_cost += int(milktotal) * 3
    if cheesetotal != '':
        cheese_label_total.configure(text="$" + str(int(cheesetotal) * 4))
        total_cost += int(cheesetotal) * 4
    if buttertotal != '':
        butter_label_total.configure(text="$" + str(int(buttertotal) * 3))
        total_cost += int(buttertotal) * 3.5
    if beeftotal != '':
        beef_label_total.configure(text="$" + str(int(beeftotal) * 20))
        total_cost += int(beeftotal) * 20
    if yoghurttotal != '':
        yoghurt_label_total.configure(
            text="$" + str(int(yoghurttotal) * 2))
        total_cost += int(yoghurttotal) * 2
    total_label.configure(text="Total: $" + str(total_cost))


# prices and names of products
title_label = Label(window, text='Milky Milk Vendor',
                    bg='violet').grid(row=0, column=2)
milk_label = Label(window, text='Milk - $3/L',
                   bg='white').grid(row=1, column=1)
cheese_label = Label(window, text='Cheese - $4/KG',
                     bg='yellow').grid(row=2, column=1)
yoghurt_label = Label(window, text='Yoghurt - $2/L',
                      bg='white').grid(row=3, column=1)
butter_label = Label(window, text='Butter - $3/KG',
                     bg='yellow').grid(row=4, column=1)
beef_label = Label(window, text='Beef - $20/KG',
                   bg='#2e1c14').grid(row=5, column=1)
exe_button = Button(window, text='Total', bg='black',
                    command=total).grid(row=6, column=1)

# total labels for each product
total_label = Label(window, text='Total', bg='red')
total_label.grid(row=6, column=3)
milk_label_total = Label(window, text='Cost', bg='grey')
milk_label_total.grid(row=1, column=3)
cheese_label_total = Label(window, text='Cost', bg='grey')
cheese_label_total.grid(row=2, column=3)
yoghurt_label_total = Label(window, text='Cost', bg='grey')
yoghurt_label_total.grid(row=3, column=3)
butter_label_total = Label(window, text='Cost', bg='grey')
butter_label_total.grid(row=4, column=3)
beef_label_total = Label(window, text='Cost', bg='grey')
beef_label_total.grid(row=5, column=3)

# input boxes for products
milk_label_input = Entry(window, bg='white')
milk_label_input.grid(row=1, column=2)
cheese_label_input = Entry(window, bg='white')
cheese_label_input.grid(row=2, column=2)
yoghurt_label_input = Entry(window, bg='white')
yoghurt_label_input.grid(row=3, column=2)
butter_label_input = Entry(window, bg='white')
butter_label_input.grid(row=4, column=2)
beef_label_input = Entry(window, bg='white')
beef_label_input.grid(row=5, column=2)


# tended and change

tended_label = Label(window, text='Tendered', bg='blue')
tended_label.grid(row=7, column=1)

tended_input = Entry(window, bg='white')
tended_input.grid(row=7, column=2)

window.mainloop()
