from tkinter import *


class Page(Frame):
    def __init__(self, *args, **kwargs):
        Frame.__init__(self, *args, **kwargs)

    def show(self):
        self.lift()


class Page1(Page):
    def __init__(self, *args, **kwargs):
        Page.__init__(self, *args, **kwargs)
        label = Label(self, text="This is page 1")
        label.pack(side="top", fill="both", expand=True)


class Page2(Page):
    def __init__(self, *args, **kwargs):
        Page.__init__(self, *args, **kwargs)

        title_label = Label(self, text='Milky Milk Vendor',
                            bg='violet').pack(side="top", fill="both", expand=True)
        milk_label = Label(self, text='Milk - $3/L',
                           bg='white').pack(side="top", fill="both", expand=True)
        cheese_label = Label(self, text='Cheese - $4/KG',
                             bg='yellow').pack(side="top", fill="both", expand=True)
        yoghurt_label = Label(self, text='Yoghurt - $2/L',
                              bg='white').pack(side="top", fill="both", expand=True)
        butter_label = Label(self, text='Butter - $3/KG',
                             bg='yellow').pack(side="top", fill="both", expand=True)
        beef_label = Label(self, text='Beef - $20/KG',
                           bg='#2e1c14').pack(side="top", fill="both", expand=True)
        # exe_button = Button(self, text='Total', bg='black',
        #                     command=total).pack(side="top", fill="both", expand=True)

        total_label = Label(self, text='Total', bg='red')
        total_label.pack(side="left", fill="both", expand=True)
        milk_label_total = Label(self, text='Cost', bg='grey')
        milk_label_total.pack(side="left", fill="both", expand=True)
        cheese_label_total = Label(self, text='Cost', bg='grey')
        cheese_label_total.pack(side="left", fill="both", expand=True)
        yoghurt_label_total = Label(self, text='Cost', bg='grey')
        yoghurt_label_total.pack(side="left", fill="both", expand=True)
        butter_label_total = Label(self, text='Cost', bg='grey')
        butter_label_total.pack(side="left", fill="both", expand=True)
        beef_label_total = Label(self, text='Cost', bg='grey')
        beef_label_total.pack(side="left", fill="both", expand=True)

        # input boxes for products
        milk_label_input = Entry(self, bg='white')
        milk_label_input.pack(side="left", fill="both", expand=True)
        cheese_label_input = Entry(self, bg='white')
        cheese_label_input.pack(side="left", fill="both", expand=True)
        yoghurt_label_input = Entry(self, bg='white')
        yoghurt_label_input.pack(side="left", fill="both", expand=True)
        butter_label_input = Entry(self, bg='white')
        butter_label_input.pack(side="left", fill="both", expand=True)
        beef_label_input = Entry(self, bg='white')
        beef_label_input.pack(side="bottom", fill="both", expand=True)


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

        b1 = Button(buttonframe, text="Page 1", command=p1.lift)
        b2 = Button(buttonframe, text="Page 2", command=p2.lift)

        b1.pack(side="left")
        b2.pack(side="left")
        p1.show()


if __name__ == "__main__":
    root = Tk()
    main = MainView(root)
    main.pack(side="top", fill="both", expand=True)
    root.wm_geometry("400x400")
    root.mainloop()
