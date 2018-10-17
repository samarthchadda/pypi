from tkinter import *

root=Tk()

topFrame=Frame(root)
topFrame.pack()
bottomFrame=Frame(root)
bottomFrame.pack(side=BOTTOM)

#WIDGETS
button1=Button(topFrame,text="Button 1",fg="red")    #fg parameter is optional
button2=Button(topFrame,text="Button 2",fg="blue")
button3=Button(topFrame,text="Button 3",fg="green")
button4=Button(bottomFrame,text="Button 4",fg="purple")
# now buttons have been created only, to display it we write the following

button1.pack(side=LEFT)    #pack it as left as possible
button2.pack(side=LEFT)
button3.pack(side=LEFT)
button4.pack()



root.mainloop()
