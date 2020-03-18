from tkinter import *


prices = {'cheese': 4,
          "beef": 20, "yoghurt": 2, "butter": 3, 'milk': 5}

items = [e for e in prices]
costs = [prices[e] for e in prices]
entries = []
amount_labels = []
title_labels = []
total = 0


class Page(Frame):
    def __init__(self, *args, **kwargs):
        Frame.__init__(self, *args, **kwargs)

    def show(self):
        self.lift()


class Page1(Page):
    global prices, costs, items, amount_labels, entries

    def __init__(self, *args, **kwargs):
        Page.__init__(self, *args, **kwargs)

        row = 0
        for e in range(len(items)):
            row += 1
            title_labels.append(Label(
                self, text=items[e] + ": $" + str(costs[e])))
            title_labels[e].grid(column=1, row=row, pady=5)
            entries.append(Entry(self))
            entries[e].grid(column=2, row=row)
            amount_labels.append(Label(self, text="0"))
            amount_labels[e].grid(column=3, row=row, padx=5)

        test_button = Button(self, command=self.get, text='cost')
        test_button.grid(column=1)

        self.total_label = Label(self, text="0", bg="red", fg='black')
        self.total_label.grid(column=3, row=6)

        tended_label = Label(self, text='Tendered', bg='white')
        tended_label.grid(row=8, column=1, padx=5, pady=5)

        self.tended_input = Entry(self, bg='white')
        self.tended_input.grid(row=8, column=2)

        change_btn = Button(self, text='Change',
                            bg='white', command=self.change)
        change_btn.grid(row=9, column=1)

        self.change_lbl = Label(self, text="Change", bg='red')
        self.change_lbl.grid(row=9, column=3)

    def change(self):
        given = self.tended_input.get()
        change = float(given) - float(self.total_cost)
        self.change_lbl.configure(text='$' + str(round(change, 2)) + '0')

    def get(self):
        global total
        total = 0
        for e in range(len(entries)):
            amount_input = entries[e].get()
            if amount_input != '':
                sub_total = int(amount_input) * costs[e]
                total += sub_total
                amount_output = amount_labels[e].configure(
                    text=str("$" + str(sub_total) + '.00'))
            self.total_label.configure(text=("$" + str(total) + '.00'))

    def change(self):
        global total
        given = self.tended_input.get()
        change = float(given) - float(total)
        self.change_lbl.configure(text='$' + str(round(change, 2)) + '0')


class Page2(Page):
    global prices, costs, items, amount_labels, entries

    def __init__(self, *args, **kwargs):
        Page.__init__(self, *args, **kwargs)

        self.value_input = Entry(self, bg='white', fg="black")
        self.value_input.grid()
        self.value_label = Label(self, text="value")
        self.value_label.grid(row=1, column=1)
        change_priceBtn = Button(
            self, text="Add Price", command=self.change_price)
        change_priceBtn.grid(row=1, column=0)

        self.change_item = Entry(self, bg="white", fg="black")
        self.change_item.grid(row=0, column=1)

        self.listbox = Listbox(self)
        for item in prices:
            self.listbox.insert(END, item + ": $" + str(prices[item]))
        self.listbox.grid()

    def change_price(self):
        global items, costs, title_labels
        value = self.value_input.get()
        item = self.change_item.get()
        prices[item] = value
        self.listbox.delete(0, END)
        for item in prices:
            self.listbox.insert(END, item + ": $" + str(prices[item]))
        items = [e for e in prices]
        costs = [int(prices[e]) for e in prices]


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
    root.wm_geometry("450x400")
    root.mainloop()
