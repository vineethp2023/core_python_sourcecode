from tkinter import *
root = Tk()
label1 =  Label(root, text='Hai', fg='red', bg='lightgreen')
label1.pack(fill=X)
label2 = Label(root,text= 'hello',fg='blue',bg='red')
label2.pack(side=RIGHT,fill=Y)
root.mainloop()
