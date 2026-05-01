import tkinter
from tkinter import messagebox

tk = tkinter.Tk()
tk.title("MyApp")
tk.config(background="lightblue")
tk.geometry("400x500")

#labels 
l1 = tkinter.Label(tk, text="Enter Number 1")
l1.place(x=50, y=50)

l2 = tkinter.Label(tk, text="Enter number 2")
l2.place(x=50, y=100)

e1 = tkinter.Entry(tk)
e1.place(x=200, y=50)

e2 = tkinter.Entry(tk)
e2.place(x=200, y=100)

res_label = tkinter.Label(tk, text="Result = ")
res_label.place(x=50, y=300)

def add():
    try:
        result = int(e1.get()) + int(e2.get())
        res_label.config(text="Result = " + str(result))
    except:
        messagebox.showerror("Error, Enter valid numbers.")

def sub():
    try:
       result = int(e1.get()) - int(e2.get())
       res_label.config(text="Result = " + str(result)) 
    except:
        messagebox.showerror("Error, Enter valid numbers.")

def mul():
    try:
       result = int(e1.get()) * int(e2.get())
       res_label.config(text="Result = " + str(result)) 
    except:
        messagebox.showerror("Error, Enter valid numbers.")

def div():
    try:
        if int(e2.get()) == 0:
            messagebox.showerror("Error", "cannot divide by zero.")
        else:
            result = int(e1.get()) / int(e2.get())
            res_label.config(text="Result = " + str(result))

    except:
        messagebox.showerror("Error", "Enter valid numbers")

b1 = tkinter.Button(tk, text="+", width=5, command=add)
b1.place(x=50, y=180)

b2 = tkinter.Button(tk, text="-", width=5, command=sub)
b2.place(x=120, y=180)

b3 = tkinter.Button(tk, text="*", width=5, command=mul)
b3.place(x=190, y=180)

b4 = tkinter.Button(tk, text="/", width=5, command=div)
b4.place(x=260, y=180)

tk.mainloop()