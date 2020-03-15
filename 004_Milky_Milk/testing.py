from tkinter import *
from functools import partial

window = Tk()
window.title('test')
window.configure(bg="#5c455a")
window.geometry("400x400+100+100")

stock = {'eggs': 2, 'cheese': 3,
         "beef": 4, "yoghurt": 2, "butter": 2, 'milk': 5}

items = [e for e in stock]
costs = [stock[e] for e in stock]

# listbox = Listbox(window)
# listbox.grid(row=1, column=1)

# for e in range(10):
#     listbox.insert(END, str(e))

row = 0
entries = []
amount = []


def get():
    global entries, amount
    for e in range(len(items)):
        amount_input = entries[e].get()
        if amount_input != '':
            amount_output = amount[e].configure(
                text=str(int(amount_input) * costs[e]))


for e in range(len(stock)):
    row += 1
    title_label = Label(
        window, text=items[e] + str(costs[e])).grid(column=1, row=row, pady=5)
    entries.append(Entry(window))
    entries[e].grid(column=2, row=row)
    amount.append(Label(window, text="cost"))
    amount[e].grid(column=3, row=row, padx=5)
test_button = Button(window, command=get, text='get values')
test_button.grid(column=1)


window.mainloop()
