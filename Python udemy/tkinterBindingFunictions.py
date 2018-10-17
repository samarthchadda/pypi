from tkinter import *

root=Tk()

def printName():
	print("Hello my name is Samarth")

button1=Button(root,text="Print my name",command=printName)    #root is written to put button in main window
button1.pack() 


root.mainloop()