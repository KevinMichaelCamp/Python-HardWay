from tkinter import *
from tkinter import messagebox
from db import Database

db = Database('tasks.db')

# Functions
def populate_list():
    todo_list.delete(0, END)
    for row in db.fetch():
        todo_list.insert(END, row)

def select_task(event):
    try:
        global selected_task
        index = todo_list.curselection()[0]
        selected_task = todo_list.get(index)

        clear_text()
        task_entry.insert(END, selected_task[1])
        category_entry.insert(END, selected_task[2])
        importance_entry.insert(END, selected_task[3])
        date_entry.insert(END, selected_task[4])
    except IndexError:
        pass

def add_task():
    if task_text.get() == '' or category_text.get() == '' or importance_text.get() == '' or date_text.get() == '':
        messagebox.showerror('Required Fields', 'Please include all fields')
        return
    db.insert(task_text.get(), category_text.get(), importance_text.get(), date_text.get())
    todo_list.delete(0, END)
    todo_list.insert(END, (task_text.get(), category_text.get(), importance_text.get(), date_text.get()))
    populate_list()
    clear_text()

def remove_task():
    db.remove(selected_task[0])
    populate_list()
    clear_text()

def update_task():
    db.update(selected_task[0], task_text.get(), category_text.get(), importance_text.get(), date_text.get())
    populate_list()

def clear_text():
    task_entry.delete(0, END)
    category_entry.delete(0, END)
    importance_entry.delete(0, END)
    date_entry.delete(0, END)

# Create Window Object
app = Tk()
app.title('ToDo List')
app.geometry('600x500')

# Task
task_text = StringVar()
task_label = Label(app, text='Task Name', font=('bold', 16), pady=20, padx=20)
task_label.grid(row=0, column=0, sticky=W)
task_entry = Entry(app, textvariable=task_text)
task_entry.grid(row=0, column=1)
task_entry.grid_configure(padx=10)
# Category
category_text = StringVar()
category_label = Label(app, text='Category', font=('bold', 16), padx=10)
category_label.grid(row=0, column=2, sticky=W)
category_entry = Entry(app, textvariable=category_text)
category_entry.grid(row=0, column=3)
category_entry.grid_configure(padx=10)
#Importance
importance_text = StringVar()
importance_label = Label(app, text='Importance', font=('bold', 16), padx=20)
importance_label.grid(row=1, column=0, sticky=W)
importance_entry = Entry(app, textvariable=importance_text)
importance_entry.grid(row=1, column=1)
importance_entry.grid_configure(padx=10)
# Due Date
date_text = StringVar()
date_label = Label(app, text='Due Date', font=('bold', 16), padx=10)
date_label.grid(row=1, column=2, sticky=W)
date_entry = Entry(app, textvariable=date_text)
date_entry.grid(row=1, column=3)
date_entry.grid_configure(padx=10)
# ToDo List
todo_list = Listbox(app, height=15, width=90)
todo_list.grid(row=3, column=0, columnspan=4, rowspan=10, padx=20, pady=20)
# Bind select
todo_list.bind('<<ListboxSelect>>', select_task)
# Scrollbar
scrollbar = Scrollbar(app)
scrollbar.grid(row=3, column=5, rowspan=10)
# Set scroll to Listbox
todo_list.configure(yscrollcommand=scrollbar.set)
scrollbar.configure(command=todo_list.yview)
# Buttons
add_btn = Button(app, text='Add Task', width=12, command=add_task)
add_btn.grid(row=2, column=0, pady=20)

remove_btn = Button(app, text='Remove Task', width=12, command=remove_task)
remove_btn.grid(row=2, column=1)

update_btn = Button(app, text='Update Task', width=12, command=update_task)
update_btn.grid(row=2, column=2)

clear_btn = Button(app, text='Clear Input', width=12, command=clear_text)
clear_btn.grid(row=2, column=3)

# Populate Data
populate_list()
# Start Program
app.mainloop()
