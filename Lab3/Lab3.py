from tkinter import *
import tkinter.messagebox
from AVL_tree import *
import os.path

filename = 'database_lab3.txt'

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

    btn_graphic = Button(root, text = 'Graphic representation\n of keys', font = 'Consolas 16', height = 3, bg = 'lavender blush', command = graphic_representation)
    btn_graphic.grid(row = 4, sticky = "EW")

def print_tree_norm(node: Node, lst: list, level: int, height: int, flag = True):
    if flag:
        if node:
            if lst[level] == '':
                lst[level] = str(node.key)
            else:
                lst[level] += '          ' * (height - level) + str(node.key)
            print_tree_norm(node.left, lst, level + 1,  height)
            print_tree_norm(node.right, lst, level + 1, height)
        else:
            if lst[level] == '':
                lst[level] = ' '
            else:
                lst[level] += '          ' * (height - level) + ' '
            print_tree_norm(None, lst, level + 1,  height, False)
            print_tree_norm(None, lst, level + 1, height, False)
    else:
        if lst[level] == '':
            lst[level] = ' '
        else:
            lst[level] += '          ' * (height - level) + ' '


def print_tree(node: Node, level: int):
    st = ''
    if node:
        st += print_tree(node.left, level + 1)
        st += '                    ' * level
        st += '     ' + str(node.key) + '\n'
        st += print_tree(node.right, level + 1)
    return st

def graphic_representation():
    child_graphic = Toplevel(root)
    root.withdraw()
    child_graphic.title('Graphic Representation of Keys')
    child_graphic.geometry('500x500')
    child_graphic['bg'] = 'lavender'

    scroll_ver = Scrollbar(child_graphic, orient='vertical')
    scroll_ver.pack(side = RIGHT, fill = Y)
    scroll_gor = Scrollbar(child_graphic, orient='horizontal')
    scroll_gor.pack(side = BOTTOM, fill = X)
    
    out = Frame(child_graphic, bg = 'lavender')
    out.pack()

    def output_tree():
        lst = []
        for i in range (tree.root.height + 3):
            lst.append('')
        print_tree_norm(tree.root, lst, 0, tree.root.height + 1)
        for line in lst:
            tree_out = Label(out, font = 'Cambria 12', bg = 'lavender')
            tree_out.pack()
            tree_out["text"] = line

    output_tree()

    def delete_child():
        child_graphic.destroy()
        root.deiconify()

    child_graphic.protocol("WM_DELETE_WINDOW", delete_child)
    return

def find_data():
    child_find = Toplevel(root)
    root.withdraw()
    child_find.title('Find Data')
    child_find.geometry('500x300')
    child_find.resizable(0, 0)
    child_find['bg'] = 'lavender'
    child_find.columnconfigure(0, minsize = 500)
    lbl = Label(child_find, text = 'Input Key to Find:', font = 'Cambria 16', bg = 'lavender')
    lbl.grid(row = 0, pady = 20)

    lbl_key = Label(child_find, text = 'Key', bg = 'lavender')
    lbl_key.grid(row = 1, padx = 5)
    ent_key = Entry(child_find, bg = 'lavender blush')
    ent_key.grid(row = 2, padx = 5, pady = 5)

    def find():
        key_str = ent_key.get()
        if not key_str.isnumeric():
            tkinter.messagebox.showinfo(title = 'Incorrect Key', message = 'The entered key must be a number.')
        else:
            key = int(key_str)
            node = tree.find(key)
            if not node:
                ent_content["text"] = ''
                tkinter.messagebox.showinfo(title = 'Search Failed', message = 'The entered key was not found in the database.')
            else:
                ent_content["text"] = node.value

    find_btn = Button(child_find, text = 'Find Data', width = 20, bg = 'lavender blush', command = find)
    find_btn.grid(row = 3, padx = 10, pady = 30)

    lbl_content = Label(child_find, text = 'Content', bg = 'lavender')
    lbl_content.grid(row = 4, padx = 5)
    ent_content = Label(child_find, bg = 'lavender blush', width = 30)
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

    def add():
        key_str = ent_key.get()
        if not key_str.isnumeric():
            tkinter.messagebox.showinfo(title = 'Incorrect Key', message = 'The entered key must be a number.')
        else:
            key = int(key_str)
            value = ent_content.get()
            flag = tree.insert(key, value)
            if not flag:
                tkinter.messagebox.showinfo(title = 'Error Adding', message = 'The entered key already exists in the database.')
            ent_key.delete(0, END)
            ent_content.delete(0, END)

    add_btn = Button(child_add, text = 'Add Data', width = 20, bg = 'lavender blush', command = add)
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

    lbl1 = Label(frm1, text = 'Input Key to Edit:', font = 'Cambria 16', bg = 'lavender')
    lbl1.grid(row = 0, columnspan = 2, pady = 20)

    lbl_key = Label(frm1, text = 'Key', bg = 'lavender')
    lbl_key.grid(row = 1, columnspan = 2, padx = 5)
    ent_key = Entry(frm1, bg = 'lavender blush')
    ent_key.grid(row = 2, columnspan = 2, padx = 5, pady = 5)

    def find():
        key_str = ent_key.get()
        if not key_str.isnumeric():
            tkinter.messagebox.showinfo(title = 'Incorrect Key', message = 'The entered key must be a number.')
        else:
            key = int(key_str)
            node = tree.find(key)
            if not node:
                tkinter.messagebox.showinfo(title = 'Search Failed', message = 'The entered key was not found in the database.')
            else:
                frm1.pack_forget()
                frm2.pack()
                ent_key_change["text"] = node.key
                ent_content_change.insert(0, node.value)

    find_to_edit_btn = Button(frm1, text = 'Find Data', width = 20, bg = 'lavender blush', command = find)
    find_to_edit_btn.grid(row = 3, columnspan = 2, padx = 10, pady = 30)


    lbl2 = Label(frm2, text = 'Change Key and/or Data:', font = 'Cambria 16', bg = 'lavender')
    lbl2.grid(row = 0, columnspan = 2, pady = 20)

    lbl_key = Label(frm2, text = 'Key', bg = 'lavender')
    lbl_key.grid(row = 1, column = 0, padx = 5)
    lbl_content = Label(frm2, text = 'Content', bg = 'lavender')
    lbl_content.grid(row = 1, column = 1, padx = 5)

    ent_key_change = Label(frm2, bg = 'lavender blush', width = 20)
    ent_key_change.grid(row = 2, column = 0, padx = 5, pady = 5)
    ent_content_change = Entry(frm2, bg = 'lavender blush', width = 30)
    ent_content_change.grid(row = 2, column = 1, padx = 5, pady = 5)

    def change():
        key = int(ent_key.get())
        new_value = ent_content_change.get()
        flag = tree.change(key, new_value)
        if not flag:
            tkinter.messagebox.showinfo(title = 'Search Failed', message = 'The entered key was not found in the database.')
        ent_key.delete(0, END)
        ent_content_change.delete(0, END)
        frm2.pack_forget()
        frm1.pack()

    def cancel():
        ent_key.delete(0, END)
        ent_content_change.delete(0, END)
        frm2.pack_forget()
        frm1.pack()

    edit_btn = Button(frm2, text = 'Edit Data', width = 20, bg = 'lavender blush', command = change)
    edit_btn.grid(row = 3, column = 0, padx = 10, pady = 30, sticky = "E")

    cancel_btn = Button(frm2, text = 'Cancel', width = 20, bg = 'lavender blush', command = cancel)
    cancel_btn.grid(row = 3, column = 1, padx = 10, pady = 30, sticky = "W")

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

    lbl1 = Label(frm1, text = 'Input Key to Delete:', font = 'Cambria 16', bg = 'lavender')
    lbl1.grid(row = 0, columnspan = 2, pady = 20)

    lbl_key = Label(frm1, text = 'Key', bg = 'lavender')
    lbl_key.grid(row = 1, columnspan = 2, padx = 5)
    ent_key = Entry(frm1, bg = 'lavender blush')
    ent_key.grid(row = 2, columnspan = 2, padx = 5, pady = 5)

    def find():
        key_str = ent_key.get()
        if not key_str.isnumeric():
            tkinter.messagebox.showinfo(title = 'Incorrect Key', message = 'The entered key must be a number.')
        else:
            key = int(key_str)
            node = tree.find(key)
            if not node:
                tkinter.messagebox.showinfo(title = 'Search Failed', message = 'The entered key was not found in the database.')
            else:
                frm1.pack_forget()
                frm2.pack()
                ent_key_delete["text"] = node.key
                ent_content_delete["text"] = node.value

    find_to_del_btn = Button(frm1, text = 'Find Data', width = 20, bg = 'lavender blush', command = find)
    find_to_del_btn.grid(row = 3, columnspan = 2, padx = 10, pady = 30)


    lbl2 = Label(frm2, text = 'Your Data:', font = 'Cambria 18', bg = 'lavender')
    lbl2.grid(row = 0, columnspan = 2, pady = 20)

    lbl_key = Label(frm2, text = 'Key', bg = 'lavender')
    lbl_key.grid(row = 1, column = 0, padx = 5)
    lbl_content = Label(frm2, text = 'Content', bg = 'lavender')
    lbl_content.grid(row = 1, column = 1, padx = 5)

    ent_key_delete = Label(frm2, bg = 'lavender blush', width = 20)
    ent_key_delete.grid(row = 2, column = 0, padx = 5, pady = 5)
    ent_content_delete = Label(frm2, bg = 'lavender blush', width = 30)
    ent_content_delete.grid(row = 2, column = 1, padx = 5, pady = 5)

    lbl3 = Label(frm2, text = 'Are you sure you want to delete?', font = 'Cambria 14', bg = 'lavender')
    lbl3.grid(row = 3, columnspan = 2, pady = 10)

    def dont_delete():
        ent_key.delete(0, END)
        ent_key_delete["text"] = ''
        ent_content_delete["text"] = ''
        frm2.pack_forget()
        frm1.pack()

    def delete():
        key = int(ent_key.get())
        ent_key.delete(0, END)
        ent_key_delete["text"] = ''
        ent_content_delete["text"] = ''
        tree.delete(key)
        frm2.pack_forget()
        frm1.pack()

    yes_btn = Button(frm2, text = 'Yes', width = 10, bg = 'lavender blush', command = delete)
    yes_btn.grid(row = 4, column = 0, padx = 10, pady = 5, sticky = "E")
    no_btn = Button(frm2, text = 'No', width = 10, bg = 'lavender blush', command = dont_delete)
    no_btn.grid(row = 4, column = 1, padx = 10, pady = 5, sticky = "W")

    def delete_child():
        child_delete.destroy()
        root.deiconify()

    child_delete.protocol("WM_DELETE_WINDOW", delete_child)
    return


def read_file(file, parent: Node = None):
    key = int(file.readline())
    value = file.readline()[:-1]
    height = int(file.readline())
    left_child = int(file.readline())
    right_child = int(file.readline())
    node = Node(key, value, parent, None, None, height)
    if left_child:
        node.left = read_file(file, node)
    if right_child:
        node.right = read_file(file, node)
    return node

def write_file(file, node: Node):
    if not node:
        return
    file.write(str(node.key) + '\n')
    file.write(str(node.value) + '\n')
    file.write(str(node.height) + '\n')
    if node.left:
        file.write('1\n')
    else:
        file.write('0\n')
    if node.right:
        file.write('1\n')
    else:
        file.write('0\n')
    if node.left:
        write_file(file, node.left)
    if node.right:
        write_file(file, node.right)
    return

if __name__ == "__main__":
    root = Tk()
    root.title('Menu')
    root.minsize(width = 400, height = 200)
    root.resizable(0, 0)
    root['bg'] = 'lavender'
    root.columnconfigure(0, minsize = 400)
    main_window()

    tree = AVLTree()
    if os.path.isfile(filename):
        file = open(filename, 'rt')
        tree.root = read_file(file)
        file.close()

    def save_tree():
        file_write = open(filename, 'wt')
        write_file(file_write, tree.root)
        file_write.close()
        root.destroy()

    root.protocol("WM_DELETE_WINDOW", save_tree)
    root.mainloop()