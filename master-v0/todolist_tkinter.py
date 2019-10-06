import tkinter
from tkinter import messagebox
import random
# To Do List (10/2) - TO DO LIST GUI
# Part 1: Create the GUI elements
# Part 3: Delete All, Sort (ASC), Sort (DES), Choose Random, Number
# Part 4: Add one, delete one
# tkinter is the standard GUI library for Python
# it provides a robust and platform independent windowinf toolkit

WINDOW_HEIGHT = 800
WINDOW_WIDTH = 600

#Create root window
root = tkinter.Tk()
# Change root window background color
root.configure(bg = "white")
# Change the title
root.title("WerkWerkWerk")
# Change the window size
root.geometry("800x600")

# Create an empty list
tasks = []

# For testing purposes, use a default list
# tasks = ["look into Smooch.io specifications", "listen to podcasts", "do hackerrank challenges"]

# Create functions
def update_listbox():
    # Clear the current list to keep from add the same tasks to the list over and over again
    clear_listbox()
    # Populate the Listbox
    for task in tasks:
        lb_tasks.insert("end", task)

def clear_listbox():
    lb_tasks.delete(0, "end")

def add_task():
    # Get the task to add
    task = txt_input.get()
    # Make sure the task is not empty
    if task != "":
        # Append to the list
        tasks.append(task)
        # Update the listbox
        update_listbox()
    else:
        tkinter.messagebox.showwarning("Warning", "Please enter a task.")
    txt_input.delete(0, "end") # clears the input box after a new task is entered

def del_all():
    confirmed = tkinter.messagebox.askyesno("Please Confirm", "Do you really want to delete all?")
    if confirmed == True:
        # Since we are changing the list, it needs to be global.
        global tasks
        # Clear the tasks list
        tasks = []
        # Update the listbox
        update_listbox()

def del_one():
    # Get the text of the currently selected item
    task = lb_tasks.get("active")
    # confirm it is in the list
    print("task:",task)
    if task in tasks:
        tasks.remove(task)
    # update the listbox
    update_listbox()

def sort_asc():
    # sort the list
    tasks.sort()
    #update the listbox
    update_listbox()

def sort_desc():
    # sort the list
    tasks.sort()
    # then reverse the list
    tasks.reverse()
    # update the listbox
    update_listbox()

def choose_random():
    # choose a random task
    task = random.choice(tasks)
    # update the display Label
    lbl_display["text"] = task

def show_number_of_tasks():
    # Get the number of tasks
    number_of_tasks = len(tasks)
    # Create and format the message
    msg = "Number of tasks: %s" % number_of_tasks
    # Display the message
    lbl_display["text"] = (msg)

def eventhandler(event):
    btn_add_task["text"] = "保存一下"

lbl_title = tkinter.Label(root, text = "任务清单", bg = "white", padx=20, pady=20 ,justify='center',width=8,height=2)
lbl_title.grid(row = 0, column = 0)

lbl_display = tkinter.Label(root, width=40, text = "任务区", bg="YellowGreen", )
lbl_display.grid(row = 0, column = 2)

txt_input = tkinter.Entry(root, width = 40 , bg="YellowGreen", )
txt_input.grid(row = 1, column = 2)

btn_add_task = tkinter.Button(root, text = "添加任务", bg = "green", command = add_task, width=10,height=2)
btn_add_task.bind_all('<Control-s>', eventhandler)
btn_add_task.grid(row = 1, column = 0)
# go create the add_task function (can create an empty function)

btn_del_all = tkinter.Button(root, text = "清除所有任务", bg = "white", command = del_all,width=10,height=2)
btn_del_all.grid(row = 2, column = 0)

btn_del_one = tkinter.Button(root, text = "删掉一个任务", bg = "white", command = del_one,width=10,height=2)
btn_del_one.grid(row = 3, column = 0)

btn_sort_asc = tkinter.Button(root, text = "升序排序", bg = "white", command = sort_asc, width=10,height=2)
btn_sort_asc.grid(row = 4, column = 0)

btn_sort_desc = tkinter.Button(root, text = "降序排序", bg = "white", command = sort_desc,width=10,height=2)
btn_sort_desc.grid(row = 5, column = 0)

btn_choose_random = tkinter.Button(root, text = "随机选择", bg = "white", command = choose_random, width=10,height=2)
btn_choose_random.grid(row = 6, column = 0)

btn_number_of_tasks = tkinter.Button(root, text = "任务数量", bg = "white", command = show_number_of_tasks,width=10,height=2 )
btn_number_of_tasks.grid(row = 7, column = 0)

btn_exit = tkinter.Button(root, text = "退出", bg = "white", command = exit, width=10,height=2)
btn_exit .grid(row = 8, column = 0)

num_label = tkinter.Label(root, text="任务序号", width=10, bg="white")
num_label.grid(row = 1, column = 1)

num_list = tkinter.Listbox(root, width=10, height = 20, )
num_list.grid(row = 2, column = 1, rowspan = 7)

lb_tasks = tkinter.Listbox(root, width=40, height = 20)
lb_tasks.grid(row = 2, column = 2, rowspan = 7)
# lb for listbox

# Start the main events loop
root.mainloop()