from tkinter import *

root=Tk()

label1=Label(root,text="Name")
label2=Label(root,text="Password")
entry1=Entry(root)         #same as input field in web design
entry2=Entry(root)

# placing the fields
label1.grid(row=0)     #by default column is always zero
label2.grid(row=1)

entry1.grid(row=0,column=1)
entry2.grid(row=1,column=1)


root.mainloop()