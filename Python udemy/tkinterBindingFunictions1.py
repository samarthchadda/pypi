from tkinter import *

root=Tk()

def printName(event):        #event is something that occurs like button click,scroll, mouse movement etc
	print("Hello my name is Samarth")

button1=Button(root,text="Print my name")    #root is written to put button in main window
button1.bind("<Button-1>",printName)
button1.pack() 


root.mainloop()