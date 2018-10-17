from tkinter import *

root=Tk()

one=Label(root,text="One",bg="red",fg="white")
one.pack()
two=Label(root,text="Two",bg="green",fg="black")
two.pack(fill=X)   #now label "two" stretches to size of window
three=Label(root,text="Three",bg="blue",fg="white")
three.pack(side=LEFT,fill=Y)


root.mainloop()
