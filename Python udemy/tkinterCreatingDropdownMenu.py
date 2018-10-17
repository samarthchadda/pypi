from tkinter import *


def doNothing():
	print("Hello")


root=Tk()

menubar=Menu(root)
root.config(menu=menubar)       #configuring a menu  (and also automatically put it at top)

submenu=Menu(menubar)       #this menu is in menubar i.e. it is submenu
menubar.add_cascade(label="File",menu=submenu)     #creating a dropdown
submenu.add_command(label="New Project....",command=doNothing)
submenu.add_command(label="New....",command=doNothing)
# submenu.add_command(label="New Project....",command=doNothing)
submenu.add_separator()     #adding a seperator
submenu.add_command(label="Exit....",command=doNothing)


#another menu
editmenu=Menu(menubar)
menubar.add_cascade(label="Edit",menu=editmenu)
editmenu.add_command(label="Redo",command=doNothing)



root.mainloop()