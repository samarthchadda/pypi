from tkinter import *

root=Tk()

def leftClick(event):
	print("Left")

def middleClick(event):
	print("Middle")

def rightClick(event):
	print("Right")


frame=Frame(root,width=300,height=250)      #invisible frame
frame.bind("<Button-1>",leftClick)      #left click
frame.bind("<Button-2>",middleClick)	#middle click
frame.bind("<Button-3>",rightClick)		#right click

frame.pack()



root.mainloop()
