from tkinter import *
root = Tk()
root.title('Calcuator')
display = Entry(root)
display.grid(row=1,columnspan=6,sticky=W+E)

# Getting user inputs and place it in the text fields
i=0
def get_variable(num):
  global i
  display.insert(i,num)
  i+=1

def get_clearall():
    display.delete(0,END)

def undo():
    entire_string = display.get()
    if len(entire_string):
        new_string = entire_string[:-1]
        get_clearall()
        display.insert(0,new_string)
    else:
        get_clearall()
        display.insert(0,"Error!")

def get_oper(opr):
    global i
    length = len(opr)
    display.insert(i,opr)
    i+=length

# performing processing

def calculate():
    entire_string = display.get()
    try:
        result = eval(entire_string)
        get_clearall()
        display.insert(0,result)
    except Exception:
        get_clearall()
        display.insert(0,'Value Error')

#adding button to the calculator
Button(root,text="1",command=lambda : get_variable(1)).grid(row=2,column=0)
Button(root,text="2",command=lambda : get_variable(2)).grid(row=2,column=1)
Button(root,text="3",command=lambda : get_variable(3)).grid(row=2,column=2)
Button(root,text="4",command=lambda : get_variable(4)).grid(row=3,column=0)
Button(root,text="5",command=lambda : get_variable(5)).grid(row=3,column=1)
Button(root,text="6",command=lambda : get_variable(6)).grid(row=3,column=2)
Button(root,text="7",command=lambda : get_variable(7)).grid(row=4,column=0)
Button(root,text="8",command=lambda : get_variable(8)).grid(row=4,column=1)
Button(root,text="9",command=lambda : get_variable(9)).grid(row=4,column=2)
Button(root,text="0",command=lambda : get_variable(0)).grid(row=5,column=0)
Button(root,text="AC",command=lambda : get_clearall()).grid(row=5,column=1)
Button(root,text="=",command=lambda : calculate()).grid(row=5,column=2)
Button(root,text="->",command=lambda : undo()).grid(row=2,column=3)
Button(root,text="+",command=lambda: get_oper('+')).grid(row=3,column=3)
Button(root,text="-",command=lambda: get_oper('-')).grid(row=4,column=3)
Button(root,text="X",command=lambda: get_oper('*')).grid(row=5,column=3)
Button(root,text="/",command=lambda: get_oper('/')).grid(row=2,column=4)
Button(root,text="%",command=lambda: get_oper('%')).grid(row=3,column=4)
Button(root,text="pi",command=lambda: get_oper('*3.14')).grid(row=4,column=4)
Button(root,text="(",command=lambda: get_oper('(')).grid(row=5,column=4)
Button(root,text=")",command=lambda: get_oper(')')).grid(row=2,column=5)
Button(root,text="exp",command=lambda: get_oper('^')).grid(row=3,column=5)
Button(root,text="x!",command=lambda: get_oper('')).grid(row=4,column=5)
Button(root,text="^2",command=lambda: get_oper('**2')).grid(row=5,column=5)

root.mainloop()


