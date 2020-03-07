import tkinter as tk


class Page(tk.Frame):
    def __init__(self, *args, **kwargs):
        tk.Frame.__init__(self, *args, **kwargs)

    def show(self):
        self.lift()


class Page1(Page):
    def __init__(self, *args, **kwargs):
        Page.__init__(self, *args, **kwargs)
        label = tk.Label(self, text="This is page 1")
        label.pack(side="top", fill="both", expand=True)

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
                            command=total).grid(row=6, column=2)

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


class Page2(Page):
    def __init__(self, *args, **kwargs):
        Page.__init__(self, *args, **kwargs)
        label = tk.Label(self, text="This is page 2")
        label.pack(side="top", fill="both", expand=True)


class Page3(Page):
    def __init__(self, *args, **kwargs):
        Page.__init__(self, *args, **kwargs)
        label = tk.Label(self, text="This is page 3")
        label.pack(side="top", fill="both", expand=True)


class MainView(tk.Frame):
    def __init__(self, *args, **kwargs):
        tk.Frame.__init__(self, *args, **kwargs)
        p1 = Page1(self)
        p2 = Page2(self)
        p3 = Page3(self)

        buttonframe = tk.Frame(self)
        container = tk.Frame(self)
        buttonframe.pack(side="top", fill="x", expand=False)
        container.pack(side="top", fill="both", expand=True)

        p1.place(in_=container, x=0, y=0, relwidth=1, relheight=1)
        p2.place(in_=container, x=0, y=0, relwidth=1, relheight=1)
        p3.place(in_=container, x=0, y=0, relwidth=1, relheight=1)

        b1 = tk.Button(buttonframe, text="Page 1", command=p1.lift)
        b2 = tk.Button(buttonframe, text="Page 2", command=p2.lift)
        b3 = tk.Button(buttonframe, text="Page 3", command=p3.lift)

        b1.pack(side="left")
        b2.pack(side="left")
        b3.pack(side="left")

        p1.show()


if __name__ == "__main__":
    root = tk.Tk()
    main = MainView(root)
    main.pack(side="top", fill="both", expand=True)
    root.wm_geometry("400x400")
    root.mainloop()
