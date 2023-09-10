from tkinter import *
class myclass:
    def __init__(self,root_one):
        frame = Frame(root_one)
        frame.pack()
        self.print_btn = Button(frame, text='Click me',command=self.print_hello)
        self.exit_btn = Button(frame,text='Quit',command=frame.quit)
        self.print_btn.pack()
        self.exit_btn.pack(side=LEFT)
    def print_hello(self):
        print('You clicked Me!!Hello')
root = Tk()
myclass_ob = myclass(root)
root.mainloop()