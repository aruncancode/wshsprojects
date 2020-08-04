from tkinter import *


prices = {'cheese': 4,
          "beef": 20, "yoghurt": 2, "butter": 3, 'milk': 5, 'pork':5, 'chicken':10, 'toilet paper':100, 'hand sanitiser':5, 'eggs':3}

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

        self.total_label = Label(self, text="total", bg="red", fg='black')
        self.total_label.grid(row=row+1, column=3)

        get_button = Button(self, command=self.get, text='cost')
        get_button.grid(row=row+1,column=1)

        tended_label = Label(self, text='Tendered', bg='white')
        tended_label.grid(row=row+2,column=1, padx=5, pady=5)

        self.tended_input = Entry(self, bg='white')
        self.tended_input.grid(row=row+2,column=2)

        change_btn = Button(self, text='Change',
                            bg='white', command=self.change)
        change_btn.grid(row=row+3,column=1)

        self.change_lbl = Label(self, text="Change", bg='red')
        self.change_lbl.grid(row=row+3,column=3)

    def update_stock(self):
        global title_labels, costs, items
        row = 0
        for e in range(len(items)):
            row += 1
            title_labels[e].configure(text=items[e] + ": $" + str(costs[e]))

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
        value_label = Label(self, text="item").grid(row=1, column=1)
        item_label = Label(self, text='value').grid(row=1, column=0)

        change_priceBtn = Button(
            self, text="Add Price", command=self.change_price)
        change_priceBtn.grid(row=0, column=4)

        self.change_item = Entry(self, bg="white", fg="black")
        self.change_item.grid(row=0, column=1)

        self.listbox = Listbox(self)
        for item in prices:
            self.listbox.insert(END, item + ": $" + str(prices[item]))
        self.listbox.grid()
        
        warning_label = Label(self, text='DO NOT ADD ANY ITEMS', bg='yellow').grid()

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
        Page1.update_stock(Page1)


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
    root.geometry('500x500') 
    main = MainView(root)
    main.pack(side="top", fill="both", expand=True)
    root.resizable(height = None, width = None)
    root.mainloop()
