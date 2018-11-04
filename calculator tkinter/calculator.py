from tkinter import *
import parser        #it helps us to solve the mathematical equations


root=Tk()
root.geometry("330x270")
root.title('Calculator')

#adding the input field
display=Entry(root,font=("Courier New",15,'bold'),textvar="cal",width=25,bd=10,bg='powder blue')
display.grid(row=1,columnspan=6,sticky=W+E)    #sticky part denotes that, 'display' spreads from west to east 


#adding the buttons to the calculator
Button(root,text="1",command=lambda:get_variables(1),padx=14,pady=14,bd=4,bg='white').grid(row=2,column=0)
Button(root,text="2",command=lambda:get_variables(2),padx=14,pady=14,bd=4,bg='white').grid(row=2,column=1)
Button(root,text="3",command=lambda:get_variables(3),padx=14,pady=14,bd=4,bg='white').grid(row=2,column=2)

Button(root,text="4",command=lambda:get_variables(4),padx=14,pady=14,bd=4,bg='white').grid(row=3,column=0)
Button(root,text="5",command=lambda:get_variables(5),padx=14,pady=14,bd=4,bg='white').grid(row=3,column=1)
Button(root,text="6",command=lambda:get_variables(6),padx=14,pady=14,bd=4,bg='white').grid(row=3,column=2)

Button(root,text="7",command=lambda:get_variables(7),padx=14,pady=14,bd=4,bg='white').grid(row=4,column=0)
Button(root,text="8",command=lambda:get_variables(8),padx=14,pady=14,bd=4,bg='white').grid(row=4,column=1)
Button(root,text="9",command=lambda:get_variables(9),padx=14,pady=14,bd=4,bg='white').grid(row=4,column=2)

#adding other buttons to the calculator
Button(root,text="AC",command=lambda:clear_all(),padx=14,pady=14,bd=4,bg='white').grid(row=5,column=0)
Button(root,text="0",command=lambda:get_variables(0),padx=14,pady=14,bd=4,bg='white').grid(row=5,column=1)
Button(root,text="=",command=lambda:calculate(),padx=14,pady=14,bd=4,bg='white').grid(row=5,column=2)

Button(root,text="+",command=lambda:get_operation("+"),padx=14,pady=14,bd=4,bg='white').grid(row=2,column=3)
Button(root,text="-",command=lambda:get_operation("-"),padx=14,pady=14,bd=4,bg='white').grid(row=3,column=3)
Button(root,text="*",command=lambda:get_operation("*"),padx=14,pady=14,bd=4,bg='white').grid(row=4,column=3)
Button(root,text="/",command=lambda:get_operation("/"),padx=14,pady=14,bd=4,bg='white').grid(row=5,column=3)

#adding new operations
Button(root,text="pi",command=lambda:get_operation("*3.14"),padx=14,pady=14,bd=4,bg='white').grid(row=2,column=4)
Button(root,text="%",command=lambda:get_operation("%"),padx=14,pady=14,bd=4,bg='white').grid(row=3,column=4)
Button(root,text="(",command=lambda:get_operation("("),padx=14,pady=14,bd=4,bg='white').grid(row=4,column=4)
Button(root,text="exp",command=lambda:get_operation("**"),padx=14,pady=14,bd=4,bg='white').grid(row=5,column=4)

Button(root,text="<-",command=lambda:undo(),padx=14,pady=14,bd=4,bg='white').grid(row=2,column=5)    #<- denotes backspace
Button(root,text="x!",padx=14,pady=14,bd=4,bg='white').grid(row=3,column=5)
Button(root,text=")",command=lambda:get_operation(")"),padx=14,pady=14,bd=4,bg='white').grid(row=4,column=5)
Button(root,text="^2",command=lambda:get_operation("**2"),padx=14,pady=14,bd=4,bg='white').grid(row=5,column=5)





#getting the user input and place it in the textfield
i=0
def get_variables(num):
    global i
    display.insert(i,num)    #check syntax for insert() in tkinter
    i+=1



def get_operation(operator):
    global i
    length=len(operator)
    display.insert(i,operator)
    i+=length

    







     
def clear_all():
    display.delete(0,END)     #delete field from index '0' till the END
    command=lambda:get_variables(1)

def undo():
    entire_string=display.get()    #extracting entire string from the display
    if len(entire_string):
        new_str=entire_string[:-1]       #last element is not included
        clear_all()
        display.insert(0,new_str)
    else:
        clear_all()
        display.insert(0,"Error")
        
        



def calculate():
    entire_string=display.get()
    try:
        a=parser.expr(entire_string).compile()   #parser will accept the entire expression and then it will be compiled
        result=eval(a)    #extract the result
        clear_all()   #first input field will be cleared then we will display the result
        display.insert(0,result)
    except Exception:
        clear_all()
        display.insert(0,"Error")
        
        









root.mainloop()

