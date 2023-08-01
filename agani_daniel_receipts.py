from tkinter import *

app = Tk()
app.title("Receipts")
# app.geometry("400x400")

itemslist = ""
itemtotals = 0.0


def add():
    getData()
    items.config(text=itemslist)


def getData():
    global itemslist, itemtotals
    try:
        error.config(text="")
        n = str(name.get())
        if n == "":
            raise Exception("Invalid Name")
        if len(n) < 3:
            raise Exception("Name Too Short")
        q = int(quan.get())
        u = float(unit.get())
        final_price = q*u
        itemtotals = itemtotals+final_price
        total.config(text=f"Total: {itemtotals}$")
        final_list = f"{itemslist}{n:<15}|{final_price:>10}$\n"
        itemslist = final_list
    except ValueError:
        error.config(text="Invalid Quantity or Unit Price")
    except Exception as e:
        error.config(text=e)


error = Label(app, text="", fg="red")
error.pack(fill='x')
frame1 = Frame(app, padx=24, pady=24, width=60)
frame1.pack(side='top', fill='x')

# labels
Label(frame1, text="Name").grid(row=0)
Label(frame1, text="Quantity").grid(row=1)
Label(frame1, text="Unit Price").grid(row=2)

items = Label(frame1, text="", height=10, justify='left')
items.grid(row=5, column=0, columnspan=5, rowspan=5)

# inputs
name = Entry(frame1)
name.grid(row=0, column=1)
quan = Entry(frame1)
quan.grid(row=1, column=1)
unit = Entry(frame1)
unit.grid(row=2, column=1)

# button
b = Button(frame1, text="Add Item", command=add)
b.grid(row=3, column=1)
total = Label(app, text="", fg="green", justify='right')
total.pack(fill='x')

app.mainloop()
