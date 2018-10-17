from tkinter import *


class buttons:
	def __init__(self, master):			#master is main window(or root)
		frame=Frame(master)				#created frame in main window
		frame.pack()

		self.printButton=Button(frame,text="Print Message",command=self.printMessage)
		self.printButton.pack(side=LEFT)

		self.quitButton=Button(frame,text="Quit",command=frame.quit)			#frame.quit is inbuilt that breakes the mainloop i.e. end the main program
		self.quitButton.pack(side=LEFT)

	def printMessage(self):
		print("This works")




root=Tk()

b=buttons(root)       #object

root.mainloop()