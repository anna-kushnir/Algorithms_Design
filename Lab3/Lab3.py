from tkinter import *
from AVL_tree import *

def main_window():
    root.deiconify()
    btn_find = Button(root, text = 'Find', font = 'Consolas 16', height = 3, bg = 'lavender blush', command = find_data)
    btn_find.grid(row = 0,sticky = "EW")
    btn_add = Button(root, text = 'Add', font = 'Consolas 16', height = 3, bg = 'lavender blush', command = add_data)
    btn_add.grid(row = 1, sticky = "EW")
    btn_edit = Button(root, text = 'Edit', font = 'Consolas 16', height = 3, bg = 'lavender blush', command = edit_data)
    btn_edit.grid(row = 2, sticky = "EW")
    btn_delete = Button(root, text = 'Delete', font = 'Consolas 16', height = 3, bg = 'lavender blush', command = delete_data)
    btn_delete.grid(row = 3, sticky = "EW")

def find_data():
    child_find = Toplevel(root)
    root.withdraw()
    child_find.title('Find Data')
    child_find.geometry('500x300')
    child_find.resizable(0, 0)
    child_find['bg'] = 'lavender'
    child_find.columnconfigure(0, minsize = 500)
    lbl = Label(child_find, text = 'Input Key to find:', font = 'Cambria 16', bg = 'lavender')
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

def add_data():
    child_add = Toplevel(root)
    root.withdraw()
    child_add.title('Add Data')
    child_add.geometry('500x210')
    child_add.resizable(0, 0)
    child_add['bg'] = 'lavender'
    child_add.columnconfigure([0, 1], minsize = 250)
    lbl = Label(child_add, text = 'Input new Key and Data:', font = 'Cambria 16', bg = 'lavender')
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
    add_btn.grid(row = 3, column = 0, columnspan = 2, padx = 10, pady = 30, sticky = "E")

    def delete_child():
        child_add.destroy()
        root.deiconify()

    child_add.protocol("WM_DELETE_WINDOW", delete_child)
    return

def edit_data():
    child_edit = Toplevel(root)
    root.withdraw()
    child_edit.title('Edit Data')
    child_edit.geometry('500x210')
    child_edit.resizable(0, 0)
    child_edit['bg'] = 'lavender'

    frm1 = Frame(child_edit, bg = 'lavender')
    frm1.columnconfigure([0, 1], minsize = 250)

    frm2 = Frame(child_edit, bg = 'lavender')
    frm2.columnconfigure([0, 1], minsize = 250)

    frm1.pack()

    def hide_1():
        frm1.pack_forget()
        frm2.pack()

    def hide_2():
        frm2.pack_forget()
        frm1.pack()

    lbl1 = Label(frm1, text = 'Input Key to edit:', font = 'Cambria 16', bg = 'lavender')
    lbl1.grid(row = 0, columnspan = 2, pady = 20)

    lbl_key = Label(frm1, text = 'Key', bg = 'lavender')
    lbl_key.grid(row = 1, columnspan = 2, padx = 5)
    ent_key = Entry(frm1, bg = 'lavender blush')
    ent_key.grid(row = 2, columnspan = 2, padx = 5, pady = 5)

    find_btn = Button(frm1, text = 'Find Data', width = 20, bg = 'lavender blush', command = hide_1)
    find_btn.grid(row = 3, columnspan = 2, padx = 10, pady = 30)


    lbl2 = Label(frm2, text = 'Change Key and/or Data:', font = 'Cambria 16', bg = 'lavender')
    lbl2.grid(row = 0, columnspan = 2, pady = 20)

    lbl_key = Label(frm2, text = 'Key', bg = 'lavender')
    lbl_key.grid(row = 1, column = 0, padx = 5)
    lbl_content = Label(frm2, text = 'Content', bg = 'lavender')
    lbl_content.grid(row = 1, column = 1, padx = 5)

    ent_key_change = Entry(frm2, bg = 'lavender blush')
    ent_key_change.grid(row = 2, column = 0, padx = 5, pady = 5)
    ent_content_change = Entry(frm2, bg = 'lavender blush', width = 30)
    ent_content_change.grid(row = 2, column = 1, padx = 5, pady = 5)

    edit_btn = Button(frm2, text = 'Edit Data', width = 20, bg = 'lavender blush', command = hide_2)
    edit_btn.grid(row = 3, column = 0, columnspan = 2, padx = 10, pady = 30)

    def delete_child():
        child_edit.destroy()
        root.deiconify()

    child_edit.protocol("WM_DELETE_WINDOW", delete_child)
    return

def delete_data():
    child_delete = Toplevel(root)
    root.withdraw()
    child_delete.title('Delete Data')
    child_delete.geometry('500x250')
    child_delete.resizable(0, 0)
    child_delete['bg'] = 'lavender'

    frm1 = Frame(child_delete, bg = 'lavender')
    frm1.columnconfigure([0, 1], minsize = 250)

    frm2 = Frame(child_delete, bg = 'lavender')
    frm2.columnconfigure([0, 1], minsize = 250)

    frm1.pack()

    def hide_1():
        frm1.pack_forget()
        frm2.pack()

    def hide_2():
        frm2.pack_forget()
        frm1.pack()

    lbl1 = Label(frm1, text = 'Input Key to Delete:', font = 'Cambria 16', bg = 'lavender')
    lbl1.grid(row = 0, columnspan = 2, pady = 20)

    lbl_key = Label(frm1, text = 'Key', bg = 'lavender')
    lbl_key.grid(row = 1, columnspan = 2, padx = 5)
    ent_key = Entry(frm1, bg = 'lavender blush')
    ent_key.grid(row = 2, columnspan = 2, padx = 5, pady = 5)

    find_btn = Button(frm1, text = 'Find Data', width = 20, bg = 'lavender blush', command = hide_1)
    find_btn.grid(row = 3, columnspan = 2, padx = 10, pady = 30)


    lbl2 = Label(frm2, text = 'Your Data:', font = 'Cambria 18', bg = 'lavender')
    lbl2.grid(row = 0, columnspan = 2, pady = 20)

    lbl_key = Label(frm2, text = 'Key', bg = 'lavender')
    lbl_key.grid(row = 1, column = 0, padx = 5)
    lbl_content = Label(frm2, text = 'Content', bg = 'lavender')
    lbl_content.grid(row = 1, column = 1, padx = 5)

    ent_key_change = Entry(frm2, bg = 'lavender blush', state = 'disabled', disabledbackground = 'lavender blush')
    ent_key_change.grid(row = 2, column = 0, padx = 5, pady = 5)
    ent_content_change = Entry(frm2, bg = 'lavender blush', width = 30, state = 'disabled', disabledbackground = 'lavender blush')
    ent_content_change.grid(row = 2, column = 1, padx = 5, pady = 5)

    lbl3 = Label(frm2, text = 'Are you sure you want to delete?', font = 'Cambria 14', bg = 'lavender')
    lbl3.grid(row = 3, columnspan = 2, pady = 10)

    yes_btn = Button(frm2, text = 'Yes', width = 10, bg = 'lavender blush', command = hide_2)
    yes_btn.grid(row = 4, column = 0, padx = 10, pady = 5, sticky = "E")
    no_btn = Button(frm2, text = 'No', width = 10, bg = 'lavender blush', command = hide_2)
    no_btn.grid(row = 4, column = 1, padx = 10, pady = 5, sticky = "W")

    def delete_child():
        child_delete.destroy()
        root.deiconify()

    child_delete.protocol("WM_DELETE_WINDOW", delete_child)
    return

if __name__ == "__main__":
    root = Tk()
    root.title('Menu')
    root.minsize(width = 400, height = 200)
    root.resizable(0, 0)
    root['bg'] = 'lavender'
    root.columnconfigure(0, minsize = 400)
    main_window()
    root.mainloop()