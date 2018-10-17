from tkinter import *

root=Tk()

label1=Label(root,text="Name")
label2=Label(root,text="Password")
entry1=Entry(root)         #same as input field in web design
entry2=Entry(root)

# placing the fields
label1.grid(row=0,sticky=E)     #places to East i.e. right aligned
label2.grid(row=1,sticky=E)

entry1.grid(row=0,column=1)
entry2.grid(row=1,column=1)

#checkbox
c=Checkbutton(root,text="Keep me logged in")
c.grid(columnspan=2)      	#two columns are merged together

root.mainloop()