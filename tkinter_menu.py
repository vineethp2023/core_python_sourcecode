from tkinter import *
root = Tk()
mymenu = Menu(root)
root.config(menu=mymenu)
submenu = Menu(mymenu)
mymenu.add_cascade(label="File",menu=submenu)
submenu.add_command(label="save")
newmenu = Menu(mymenu)
submenu.add_cascade(label="edit",menu=newmenu)
newmenu.add_command(label="cut/copy")
newmenu.add_command(label="paste")
newmenu.add_command(label="redo")
submenu.add_command(label="undo")
root.mainloop()
