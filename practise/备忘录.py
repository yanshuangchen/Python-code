from tkinter import *
from tkinter import messagebox

def add_task():
    task = entry_task.get()
    if task != "":
        list_tasks.insert(END, task)
        entry_task.delete(0, END)
    else:
        messagebox.showwarning("Warning", "Please enter a task.")

def delete_task():
    try:
        task_index = list_tasks.curselection()[0]
        list_tasks.delete(task_index)
    except:
        messagebox.showwarning("Warning", "Please select a task.")

def complete_task():
    try:
        task_index = list_tasks.curselection()[0]
        list_tasks.itemconfig(task_index, fg="gray")
        list_tasks.selection_clear(0, END)
    except:
        messagebox.showwarning("Warning", "Please select a task.")

# create main window
root = Tk()
root.title("To-Do List")

# create input field
entry_task = Entry(root, width=40)
entry_task.pack(padx=10, pady=10)

# create add button
button_add = Button(root, text="Add Task", command=add_task)
button_add.pack(padx=10, pady=5)

# create delete button
button_delete = Button(root, text="Delete Task", command=delete_task)
button_delete.pack(padx=10, pady=5)

# create complete button
button_complete = Button(root, text="Complete Task", command=complete_task)
button_complete.pack(padx=10, pady=5)

# create task list
list_tasks = Listbox(root, height=15, width=50)
list_tasks.pack(padx=10, pady=10)

root.mainloop()
