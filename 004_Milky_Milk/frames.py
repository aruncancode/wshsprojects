from tkinter import *


class Page(Frame):
    def __init__(self, *args, **kwargs):
        Frame.__init__(self, *args, **kwargs)

    def show(self):
        self.lift()


class Page1(Page):

    def __init__(self, *args, **kwargs):
        Page.__init__(self, *args, **kwargs)

        self.total_cost = 0

        title_label = Label(self, text='Milky Milk Vendor',
                            bg='violet').grid(row=0, column=2, padx=5)
        milk_label = Label(self, text='Milk - $3/L',
                           bg='white').grid(row=1, column=1, padx=5, pady=5, sticky=N+S+E+W)
        cheese_label = Label(self, text='Cheese - $4/KG',
                             bg='yellow').grid(row=2, column=1, padx=5, pady=5)
        yoghurt_label = Label(self, text='Yoghurt - $2/L',
                              bg='white').grid(row=3, column=1, padx=5, pady=5)
        butter_label = Label(self, text='Butter - $3/KG',
                             bg='yellow').grid(row=4, column=1, padx=5, pady=5)
        beef_label = Label(self, text='Beef - $20/KG',
                           bg='brown').grid(row=5, column=1, padx=5, pady=5)
        exe_button = Button(self, text='Total', bg='white',
                            command=self.total).grid(row=6, column=1, padx=5, pady=5)

        # total labels for each product
        self.total_label = Label(self, text='Total', bg='red')
        self.total_label.grid(row=6, column=3)
        self.milk_label_total = Label(self, text='Cost', bg='grey')
        self.milk_label_total.grid(row=1, column=3)
        self.cheese_label_total = Label(self, text='Cost', bg='grey')
        self.cheese_label_total.grid(row=2, column=3)
        self.yoghurt_label_total = Label(self, text='Cost', bg='grey')
        self.yoghurt_label_total.grid(row=3, column=3)
        self.butter_label_total = Label(self, text='Cost', bg='grey')
        self.butter_label_total.grid(row=4, column=3)
        self.beef_label_total = Label(self, text='Cost', bg='grey')
        self.beef_label_total.grid(row=5, column=3)

        # input boxes for products
        self.milk_label_input = Entry(self, bg='white')
        self.milk_label_input.grid(row=1, column=2)
        self.cheese_label_input = Entry(self, bg='white')
        self.cheese_label_input.grid(row=2, column=2)
        self.yoghurt_label_input = Entry(self, bg='white')
        self.yoghurt_label_input.grid(row=3, column=2)
        self.butter_label_input = Entry(self, bg='white')
        self.butter_label_input.grid(row=4, column=2)
        self.beef_label_input = Entry(self, bg='white')
        self.beef_label_input.grid(row=5, column=2)

        # tended and change
        tended_label = Label(self, text='Tendered', bg='white')
        tended_label.grid(row=8, column=1, padx=5, pady=5)

        self.tended_input = Entry(self, bg='white')
        self.tended_input.grid(row=8, column=2)

        change_btn = Button(self, text='Change',
                            bg='white', command=self.change)
        change_btn.grid(row=9, column=1)

        self.change_lbl = Label(self, text="Change", bg='white')
        self.change_lbl.grid(row=9, column=3)

    def total(self):
        cheesetotal = self.cheese_label_input.get()
        yoghurttotal = self.yoghurt_label_input.get()
        beeftotal = self.beef_label_input.get()
        buttertotal = self.butter_label_input.get()
        milktotal = self.milk_label_input.get()

        if milktotal != '':
            self.milk_label_total.configure(text="$" + str(int(milktotal) * 3))
            self.total_cost += int(milktotal) * 3
        if cheesetotal != '':
            self.cheese_label_total.configure(
                text="$" + str(int(cheesetotal) * 4))
            self.total_cost += int(cheesetotal) * 4
        if buttertotal != '':
            self.butter_label_total.configure(
                text="$" + str(int(buttertotal) * 3))
            self.total_cost += int(buttertotal) * 3.5
        if beeftotal != '':
            self.beef_label_total.configure(
                text="$" + str(int(beeftotal) * 20))
            self.total_cost += int(beeftotal) * 20
        if yoghurttotal != '':
            self.yoghurt_label_total.configure(
                text="$" + str(int(yoghurttotal) * 2))
            self.total_cost += int(yoghurttotal) * 2
        self.total_label.configure(text="Total: $" + str(self.total_cost))

    def change(self):
        given = self.tended_input.get()
        change = float(given) - float(self.total_cost)
        self.change_lbl.configure(text='$' + str(round(change, 2)) + '0')


class Page2(Page):
    def __init__(self, *args, **kwargs):
        Page.__init__(self, *args, **kwargs)
        oneBtn = Button(self, text="1", bg="green",
                        fg="black").grid(row=1, column=1)
        twoBtn = Button(self, text="2", bg="green",
                        fg="black").grid(row=1, column=2)
        threeBtn = Button(self, text="3", bg="green",
                          fg="black").grid(row=1, column=3)
        fourBtn = Button(self, text="4", bg="green",
                         fg="black").grid(row=2, column=1)
        fiveBtn = Button(self, text="5", bg="green",
                         fg="black").grid(row=2, column=2)
        sixBtn = Button(self, text="6", bg="green",
                        fg="black").grid(row=2, column=3)
        sevemBtn = Button(self, text="7", bg="green",
                          fg="black").grid(row=3, column=1)
        eightBtn = Button(self, text="8", bg="green",
                          fg="black").grid(row=3, column=2)
        nineBtn = Button(self, text="9", bg="green",
                         fg="black").grid(row=3, column=3)
        zeroBtn = Button(self, text="0", bg="green",
                         fg="black").grid(row=4, column=1)
        dotBtn = Button(self, text=".", bg="green",
                        fg="black").grid(row=4, column=2)


class MainView(Frame):
    def __init__(self, *args, **kwargs):
        Frame.__init__(self, *args, **kwargs)
        p1 = Page1(self)
        p2 = Page2(self)

        buttonframe = Frame(self)
        container = Frame(self)
        buttonframe.pack(side="top", fill="x", expand=False)
        container.pack(side="top", fill="both", expand=True)

        p1.place(in_=container, x=0, y=0, relwidth=1, relheight=1)
        p2.place(in_=container, x=0, y=0, relwidth=1, relheight=1)

        b1 = Button(buttonframe, text="Vendor", command=p1.lift)
        b2 = Button(buttonframe, text="Mainframe", command=p2.lift)

        b1.pack(side="left")
        b2.pack(side="left")
        p1.show()


if __name__ == "__main__":
    root = Tk()
    main = MainView(root)
    main.pack(side="top", fill="both", expand=True)
    # main.grid(row=1, column=1, columnspan=5, rowspan=5, padx=5, pady=5?)
    root.wm_geometry("400x400")
    root.mainloop()
