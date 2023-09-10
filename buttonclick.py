from tkinter import *
root = Tk()
def fun():
    print('Hello! You clicked a button')
btn_1 = Button(root,text='submit',command=fun,bg='yellow',fg='red')
btn_1.pack()
root.mainloop()