from tkinter import *
from AVL_tree import *

def add_data(root: Tk):
    root.children.clear()

    lbl = Label(root, text = 'Input new data:', font = 'Cambria 18', bg = 'lavender')
    lbl.grid(row = 0, column = 0, columnspan = 4, pady = 20)

    lbl_key = Label(root, text = 'Key', bg = 'lavender')
    lbl_key.grid(row = 1, column = 0, columnspan = 2, padx = 5)
    lbl_content = Label(root, text = 'Content', bg = 'lavender')
    lbl_content.grid(row = 1, column = 2, columnspan = 2, padx = 5)

    ent_key = Entry(root, bg = 'lavender blush')
    ent_key.grid(row = 2, column = 0, columnspan = 2, padx = 5, pady = 5)
    ent_content = Entry(root, bg = 'lavender blush', width = 30)
    ent_content.grid(row = 2, column = 2, columnspan = 2, padx = 5, pady = 5)

    add_btn = Button(root, text = 'Add Data', width = 20, bg = 'lavender blush')
    add_btn.grid(row = 3, column = 0, columnspan = 4, padx = 10, pady = 50, sticky = "E")
    return

if __name__ == "__main__":
    root = Tk()
    root.title('AVL-tree')
    root.geometry('500x500')
    root.resizable(0, 0)
    root['bg'] = 'lavender'
    root.columnconfigure([0, 1, 2, 3], minsize = 125)

    btn_find = Button(root, text = 'Find')
    btn_find.grid(row = 0, column = 0, sticky = "EW")
    btn_add = Button(root, text = 'Add')
    btn_add.grid(row = 0, column = 1, sticky = "EW")
    btn_edit = Button(root, text = 'Edit')
    btn_edit.grid(row = 0, column = 2, sticky = "EW")
    btn_delete = Button(root, text = 'Delete')
    btn_delete.grid(row = 0, column = 3, sticky = "EW")

    main_frame = Frame(root, bg = 'lavender')
    main_frame.grid(row = 1, columnspan = 4)
    add_data(main_frame)
    
    root.mainloop()