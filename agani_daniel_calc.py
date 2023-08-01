from tkinter import *

tk = Tk()
tk.title('Agani_Daniel')


def add():
    ans = val(ent1) + val(ent2)
    l3.config(text=str(i_f(ans)))


def mult():
    ans = val(ent1) * val(ent2)
    l3.config(text=str(i_f(ans)))


def sub():
    ans = val(ent1) - val(ent2)
    l3.config(text=str(i_f(ans)))


def div():
    ans = val(ent1) / val(ent2, True)
    l3.config(text=str(i_f(ans)))


def mod():
    ans = val(ent1) % val(ent2, True)
    l3.config(text=str(i_f(ans)))


def exp():
    ans = val(ent1) ** val(ent2)
    l3.config(text=str(i_f(ans)))


def ediv():
    ans = val(ent1) // val(ent2, True)
    l3.config(text=str(i_f(ans)))


def val(entry: Entry, div_safety: bool = False):  # validate
    try:
        return float(entry.get())
    except:
        if div_safety:
            return 1
    return 0


def i_f(var):  # int or float
    s = var-int(var)
    if s == 0.0:
        return int(var)
    return (var)


fr = Frame(tk, background='black', height=120, padx=4, pady=4)
fr.pack(side='top', fill='x')
labfr = Frame(fr)
labfr.pack(side='left', fill='y')
l1 = Label(labfr, text="Number 1:", bg='black', fg='white').pack(
    side='top')  # .grid(row=0, column=0)
l2 = Label(labfr, text="Number 2:", bg='black', fg='white').pack(
    side='bottom')  # .grid(row=1, column=0)

ent1 = Entry(fr)
ent1.pack()  # .grid(row=0, column=1)
ent2 = Entry(fr)
ent2.pack()  # .grid(row=1, column=1)

fr2 = Frame(tk, background='Gold',
            padx=10, pady=10, height=100)
fr2.pack(side='bottom', fill='x')

Button(fr2, command=mult, text='*', width=8, height=2).grid(row=0, column=0)
Button(fr2, command=add, text='+', width=8, height=2).grid(row=0, column=1)
Button(fr2, command=sub, text='-', width=8, height=2).grid(row=0, column=2)
Button(fr2, command=div, text='/', width=8, height=2).grid(row=0, column=3)

Button(fr2, command=mod, text='%', width=8, height=2).grid(row=1, column=0)
Button(fr2, command=exp, text='exp', width=8,
       height=2).grid(row=1, column=1)
# Button(fr2,command=sub,text='-').grid(row=1,column=2)
Button(fr2, command=ediv, text='//', width=8, height=2).grid(row=1, column=3)

l3 = Label(tk, height=2)
l3.pack(side='right')

tk.mainloop()
