import tkinter
from tkinter import ttk,messagebox

tk = tkinter.Tk()
tk.title("MyApp")
tk.config(background="lightblue")
tk.geometry("400x500")

"""l1 = tkinter.Label(text="Firstname")
l1.pack()

l2 = tkinter.Label(text="lastname")
l2.pack()"""

l1 = tkinter.Label(text="Firstname")
l1.pack(x=0,y=0)

l2 = tkinter.Label(text="Lastname")
l2.pack(x=0,y=30)



tk.mainloop()

