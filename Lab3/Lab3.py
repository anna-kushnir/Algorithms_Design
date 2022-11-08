from tkinter import *
from AVL_tree import *

def main_window():
    root.deiconify()
    btn_find = Button(root, text = 'Find', height = 5, bg = 'lavender blush', command = find_data)
    btn_find.grid(row = 0,sticky = "EW")
    btn_add = Button(root, text = 'Add', height = 5, bg = 'lavender blush', command = add_data)
    btn_add.grid(row = 1, sticky = "EW")
    btn_edit = Button(root, text = 'Edit', height = 5, bg = 'lavender blush')
    btn_edit.grid(row = 2, sticky = "EW")
    btn_delete = Button(root, text = 'Delete', height = 5, bg = 'lavender blush')
    btn_delete.grid(row = 3, sticky = "EW")

def add_data():
    child_add = Toplevel(root)
    root.withdraw()
    child_add.title('Add Data')
    child_add.geometry('500x250')
    child_add.resizable(0, 0)
    child_add['bg'] = 'lavender'
    child_add.columnconfigure([0, 1], minsize = 250)
    lbl = Label(child_add, text = 'Input new data:', font = 'Cambria 18', bg = 'lavender')
    lbl.grid(row = 0, column = 0, columnspan = 2, pady = 20)

    lbl_key = Label(child_add, text = 'Key', bg = 'lavender')
    lbl_key.grid(row = 1, column = 0, padx = 5)
    lbl_content = Label(child_add, text = 'Content', bg = 'lavender')
    lbl_content.grid(row = 1, column = 1, padx = 5)

    ent_key = Entry(child_add, bg = 'lavender blush')
    ent_key.grid(row = 2, column = 0, padx = 5, pady = 5)
    ent_content = Entry(child_add, bg = 'lavender blush', width = 30)
    ent_content.grid(row = 2, column = 1, padx = 5, pady = 5)

    add_btn = Button(child_add, text = 'Add Data', width = 20, bg = 'lavender blush')
    add_btn.grid(row = 3, column = 0, columnspan = 2, padx = 10, pady = 50, sticky = "E")

    def delete_child():
        child_add.destroy()
        root.deiconify()

    child_add.protocol("WM_DELETE_WINDOW", delete_child)
    return

def find_data():
    child_find = Toplevel(root)
    root.withdraw()
    child_find.title('Find Data')
    child_find.geometry('500x300')
    child_find.resizable(0, 0)
    child_find['bg'] = 'lavender'
    child_find.columnconfigure(0, minsize = 500)
    lbl = Label(child_find, text = 'Input key:', font = 'Cambria 18', bg = 'lavender')
    lbl.grid(row = 0, pady = 20)

    lbl_key = Label(child_find, text = 'Key', bg = 'lavender')
    lbl_key.grid(row = 1, padx = 5)
    ent_key = Entry(child_find, bg = 'lavender blush')
    ent_key.grid(row = 2, padx = 5, pady = 5)

    find_btn = Button(child_find, text = 'Find Data', width = 20, bg = 'lavender blush')
    find_btn.grid(row = 3, padx = 10, pady = 30)

    lbl_content = Label(child_find, text = 'Content', bg = 'lavender')
    lbl_content.grid(row = 4, padx = 5)
    ent_content = Entry(child_find, bg = 'lavender blush', width = 30, state = 'disabled', disabledbackground = 'lavender blush')
    ent_content.grid(row = 5, padx = 5, pady = 5)

    def delete_child():
        child_find.destroy()
        root.deiconify()

    child_find.protocol("WM_DELETE_WINDOW", delete_child)
    return

if __name__ == "__main__":
    root = Tk()
    root.title('Menu')
    root.minsize(width = 500, height = 200)
    root.resizable(0, 0)
    root['bg'] = 'lavender'
    root.columnconfigure(0, minsize = 500)
    main_window()
    root.mainloop()