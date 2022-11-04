from tkinter import *
from AVL_tree import *

root = Tk()
root.title('AVL-tree')
root.geometry('500x500')
root.resizable(0, 0)
root['bg'] = 'lavender'

root.columnconfigure(0, minsize = 250)
root.columnconfigure(1, minsize = 250)

lbl = Label(root, text = 'Your Database', font = 'Cambria 18', bg = 'lavender')
lbl.grid(row = 0, column = 0, columnspan = 2, pady = 20)

frm1 = Frame(root, relief = RAISED)
frm1.grid(row = 1, column = 0, padx = 5)
lbl_key = Label(frm1, text = 'Key', bg = 'lavender')
lbl_key.pack()

frm2 = Frame(root, relief = RAISED)
frm2.grid(row = 1, column = 1, padx = 5)
lbl_content = Label(frm2, text = 'Content', bg = 'lavender')
lbl_content.pack()

frm3 = Frame(root, relief = RAISED)
frm3.grid(row = 2, column = 0, padx = 5, pady = 5)
ent_key = Entry(frm3, bg = 'lavender blush')
ent_key.pack()

frm4 = Frame(root, relief = RAISED)
frm4.grid(row = 2, column = 1, padx = 5, pady = 5)
ent_content = Entry(frm4, bg = 'lavender blush', width = 30)
ent_content.pack()

root.mainloop()