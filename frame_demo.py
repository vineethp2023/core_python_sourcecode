from tkinter import *
root =  Tk()
Label(root,text="hello world").pack()
frame1 = Frame(root)
frame1.pack()
Button(frame1,text='login',fg='red',bg='black').pack()
root.mainloop()
