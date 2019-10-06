import tkinter
from tkinter import messagebox
import random

WINDOW_HEIGHT = 1200
WINDOW_WIDTH = 600
BUTTON_HEIGHT = 2
BUTTON_WIDTH = 10

class Task:
    def __init__(self, id, content):
        self.index = id
        if len(content.split(" ")) == 1:
            self.text = content.split(" ")[0]
        elif not content.split(" ")[-1].isdigit():
            self.text = content.split(" ")[:]
        else:
            self.text = content.split(" ")[:-1]

        self.text = ''.join(self.text)
        score = content.split(" ")[-1]
        if score.isdigit():
            self.score = score
        else:
            self.score = 0

class Wish:
    def __init__(self, id, content):
        self.index = id
        if len(content.split(" ")) == 1:
            self.text = content.split(" ")[0]
        elif not content.split(" ")[-1].isdigit():
            self.text = content.split(" ")[:]
        else:
            self.text = content.split(" ")[:-1]

        self.text = ''.join(self.text)
        score = content.split(" ")[-1]
        if score.isdigit():
            self.score = score
        else:
            self.score = 0


class TODO_list:
    def __init__(self):
        #Create root window
        self.root = tkinter.Tk()
        # Change root window background color
        self.root.configure(bg = "white")
        # Change the title
        self.root.title("骆永乐的任务清单商店")
        # Change the window size
        self.root.geometry("1200x600")
        self.task_id = 1
        self.wish_id = 1

        self.total_score = 0
        self.total_wishes_score = 0

        # Create an empty list
        self.tasks_list = []
        self.wishes_list = []
        self._build_window()

    def _build_column_0(self,column):
        window_title = tkinter.Label(self.root, text = "任务清单", bg = "white", justify='center', width=BUTTON_WIDTH, height=BUTTON_HEIGHT)
        window_title.grid(row = 0, column = column)

        self.button_add_task = tkinter.Button(self.root, text = "新建任务", bg = "white", command = self.add_task, width=BUTTON_WIDTH, height=BUTTON_HEIGHT)
        # self.button_add_task.bind('<Return>', self.eventSave)
        # self.button_add_task.bind_all('<Control-s>', self.eventSave)
        self.button_add_task.grid(row = 1, column = column)
        # go create the add_task function (can create an empty function)

        button_del_all = tkinter.Button(self.root, text = "清除所有任务", bg = "white", command = self.del_all, width=BUTTON_WIDTH, height=BUTTON_HEIGHT)
        button_del_all.grid(row = 2, column = column)

        button_del_one = tkinter.Button(self.root, text = "删掉一个任务", bg = "white", command = self.del_one, width=BUTTON_WIDTH, height=BUTTON_HEIGHT)
        button_del_one.bind_all('<Delete>', self.eventDeleteOne)
        button_del_one.grid(row = 3, column = column)

        button_sort_asc = tkinter.Button(self.root, text = "升序排序", bg = "white", command = self.sort_asc, width=BUTTON_WIDTH, height=BUTTON_HEIGHT)
        button_sort_asc.grid(row = 4, column = column)

        button_sort_desc = tkinter.Button(self.root, text = "降序排序", bg = "white", command = self.sort_desc, width=BUTTON_WIDTH, height=BUTTON_HEIGHT)
        button_sort_desc.grid(row = 5, column = column)

        button_choose_random = tkinter.Button(self.root, text = "随机选择", bg = "white", command = self.choose_random, width=BUTTON_WIDTH, height=BUTTON_HEIGHT)
        button_choose_random.grid(row = 6, column = column)

        button_number_of_tasks = tkinter.Button(self.root, text = "任务数量", bg = "white", command = self.show_number_of_tasks, width=BUTTON_WIDTH, height=BUTTON_HEIGHT)
        button_number_of_tasks.grid(row = 7, column = column)

        button_exit = tkinter.Button(self.root, text = "退出", bg = "white", command = exit, width=BUTTON_WIDTH, height=BUTTON_HEIGHT)
        button_exit.bind_all('<Escape>', self.eventEsc)
        button_exit.grid(row = 8, column = column)

        # print(help(button_exit.bind_all()))
    def _build_column_1(self,column):
        num_label = tkinter.Label(self.root, text="序号", width=3, bg="white")
        num_label.grid(row = 1, column = column)

        # num_list = tkinter.Listbox(self.root, width=3, height = 20, )
        # num_list.grid(row = 2, column = 1, rowspan = 12)

        # 显示序号
        self.tasks_index_display = tkinter.Listbox(self.root, width=3, height = 20)
        self.tasks_index_display.grid(row = 2, column = column, rowspan = 12)

    def _build_column_2(self, column):
        self.top_display = tkinter.Label(self.root, width=36, text="任务区", bg="SkyBlue", )
        self.top_display.grid(row=0, column=column)

        self.txt_input = tkinter.Entry(self.root, width=36, bg="SkyBlue", )
        self.txt_input.bind('<Return>', self.eventSave)
        self.txt_input.bind('<ButtonPress>', self.eventDisappear)
        self.txt_input.bind("<FocusOut>", self.eventLeave)
        self.default_text = '输入模版：阅读paper 5'
        self.txt_input.insert(0, self.default_text)
        self.txt_input.grid(row=1, column=column)

        # 显示窗口
        self.tasks_display = tkinter.Listbox(self.root, width=40, height = 20)
        self.tasks_display.grid(row = 2, column = column, rowspan = 7)
        # lb for listbox

    def _build_score_list(self,column):
        score_label = tkinter.Label(self.root, text="对应积分", width=6, height=BUTTON_HEIGHT, padx=10, pady=0, bg="lightCyan")
        score_label.grid(row = 1, column = column)

        # 显示序号
        self.tasks_score_display = tkinter.Listbox(self.root, width=6, height = 20)
        self.tasks_score_display.grid(row = 2, column = column, rowspan = 12)


    # TODO analysis scores
    def _build_score_analysis(self, column):
        self.score_label = tkinter.Label(self.root, text="结余积分", width=8, height=BUTTON_HEIGHT, padx=10, pady=0, bg="Violet")
        self.score_label.grid(row=1, column=column)
        self.score_value = tkinter.Label(self.root, text=self.total_score, width=8, height=BUTTON_HEIGHT, padx=10, pady=0, bg="cornsilk")
        self.score_value.grid(row=2, column=column)

        self.wishes_score_label = tkinter.Label(self.root, text="愿望积分", width=8, height=BUTTON_HEIGHT, padx=10, pady=0,
                                         bg="Violet")
        self.wishes_score_label.grid(row=3, column=column)
        self.wishes_score_value = tkinter.Label(self.root, text=self.total_score, width=8, height=BUTTON_HEIGHT, padx=10,
                                         pady=0, bg="cornsilk")
        self.wishes_score_value.grid(row=4, column=column)

    def _build_column_wish(self, column):
        wish_num_label = tkinter.Label(self.root, text="序号", width=3, bg="white")
        wish_num_label.grid(row = 1, column = column)
        # 显示序号
        self.wishes_index_display = tkinter.Listbox(self.root, width=3, height = 20)
        self.wishes_index_display.grid(row = 2, column = column, rowspan = 12)


    def _build_wish_list(self, column):
        self.wish_top_display = tkinter.Label(self.root, width=36, text="愿望商店", padx=10, pady=0, bg="SkyBlue", )
        self.wish_top_display.grid(row=0, column=column)

        self.wish_input = tkinter.Entry(self.root, width=36, bg="SkyBlue", )
        self.wish_input.bind('<Return>', self.event_wishSave)
        self.wish_input.bind('<ButtonPress>', self.event_wishDisappear)
        self.wish_input.bind("<FocusOut>", self.event_wishLeave)
        self.default_wish_text = '输入模版：看十分钟小说 2'
        self.wish_input.insert(0, self.default_wish_text)
        self.wish_input.grid(row=1, column=column)

        # 显示窗口
        self.wishes_display = tkinter.Listbox(self.root, width=40, height = 20)
        self.wishes_display.grid(row = 2, column = column, rowspan = 7)
        # lb for listbox

    def _build_wishes_score_list(self,column):
        wishes_score_label = tkinter.Label(self.root, text="对应积分", width=6, height=BUTTON_HEIGHT, padx=10, pady=0, bg="lightCyan")
        wishes_score_label.grid(row = 1, column = column)

        # 显示序号
        self.wishes_score_display = tkinter.Listbox(self.root, width=6, height = 20)
        self.wishes_score_display.grid(row = 2, column = column, rowspan = 12)


    def _build_window(self):
        self._build_column_0(0)
        self._build_column_1(1)
        self._build_column_2(2)
        self._build_score_list(3)
        self._build_score_analysis(4)
        self._build_column_wish(5)
        self._build_wish_list(6)
        self._build_wishes_score_list(7)

        # Start the main events loop
        self.root.mainloop()

    def update_listbox(self):
        # Clear the current list to keep from add the same tasks to the list over and over again
        self.clear_listbox()
        self.clear_task_index()
        self.clear_score_index()
        # Populate the Listbox
        for task in self.tasks_list:
            self.tasks_display.insert("end", task.text)
            self.tasks_index_display.insert("end", task.index)
            self.tasks_score_display.insert("end", task.score)

    def clear_listbox(self):
        self.tasks_display.delete(0, "end")

    def clear_task_index(self):
        self.tasks_index_display.delete(0, 'end')

    def clear_score_index(self):
        self.tasks_score_display.delete(0, 'end')

    def add_task(self):
        # Get the task to add
        self.task_content = self.txt_input.get()
        self.tasks_num = len(self.tasks_list)
        print("num:", self.tasks_num)
        self.task_id = self.tasks_num + 1
        self.new_task = Task(self.task_id, self.task_content)
        # Make sure the task is not empty
        if self.new_task.text != "":
            # Append to the list
            self.tasks_list.append(self.new_task)
            self.total_score += int(self.new_task.score)
            self.score_value['text'] = self.total_score
            # Update the listbox
            self.update_listbox()
        else:
            # tkinter.messagebox.showwarning("Warning", "Please enter a task.")
            pass
        self.txt_input.delete(0, "end") # clears the input box after a new task is entered

    def save_to_local(self):
        self.file_name = "tasks.txt"
        f = open(self.file_name, 'w', encoding='utf-8')
        for t in self.tasks_list:
            f.write(str(t.index))
            f.write(" ")
            f.write(t.text)
            f.write(" ")
            f.write(str(t.score))
            f.write("\n")
        f.close()

    def del_all(self):
        confirmed = tkinter.messagebox.askyesno("Please Confirm", "Do you really want to delete all?")
        if confirmed == True:
            # Since we are changing the list, it needs to be global.
            # Clear the tasks list
            self.tasks_list = []
            self.total_score = 0
            self.score_value['text'] = self.total_score
            # Update the listbox
            self.update_listbox()
        self.sort_asc()

    def del_one(self):
        # Get the text of the currently selected item
        task_text = self.tasks_display.get("active")
        for t in self.tasks_list:
            if task_text == t.text:
                self.total_score -= int(t.score)
                self.score_value['text'] = self.total_score
                self.tasks_list.remove(t)
        self.sort_asc()

    # TODO 根据ID进行重新排序！
    def sort_asc(self):
        # sort the list
        tem_list = []
        for i in range(len(self.tasks_list)):
            tem_task = self.tasks_list[i]
            tem_task.index = i+1
            tem_list.append(tem_task)
        self.tasks_list = tem_list

        #update the listbox
        self.update_listbox()

    def sort_desc(self):
        # sort the list
        self.tasks_list.sort()
        # then reverse the list
        self.tasks_list.reverse()
        # update the listbox
        self.update_listbox()

    def choose_random(self):
        # choose a random task
        if self.tasks_list:
            task = random.choice(self.tasks_list)
            # update the display Label
            self.top_display["text"] = task.text
            # self.tasks_index_display["text"] = task.index
        else:
            print("there is no task!")

    def show_number_of_tasks(self):
        # Get the number of tasks
        number_of_tasks = len(self.tasks_list)
        # Create and format the message
        msg = "Number of tasks: %s" % number_of_tasks
        # Display the message
        self.top_display["text"] = (msg)
        return number_of_tasks

    def eventDeleteOne(self, event):
        self.del_one()

    def eventEsc(self, event):
        self.save_to_local()
        exit()

    def eventSave(self, event):
        self.add_task()

    def eventDisappear(self, event):
        print("enter")
        self.txt_input.delete(0, last='end')

    def eventLeave(self, event):
        self.default_text = '输入模版：阅读paper 5'
        self.txt_input.insert(0, self.default_text)

    def add_wish(self):
        # Get the task to add
        self.wish_content = self.wish_input.get()
        self.wishes_num = len(self.wishes_list)
        print("num:", self.wishes_num)
        self.wish_id = self.wishes_num + 1
        self.new_wish = Wish(self.wish_id, self.wish_content)
        # Make sure the task is not empty
        if self.new_wish.text != "":
            # Append to the list
            self.wishes_list.append(self.new_wish)
            self.total_wishes_score += int(self.new_wish.score)
            self.wishes_score_value['text'] = self.total_wishes_score
            # Update the listbox
            self.update_wishes_listbox()
        else:
            # tkinter.messagebox.showwarning("Warning", "Please enter a task.")
            pass
        self.wish_input.delete(0, "end") # clears the input box after a new task is entered

    def event_wishSave(self, event):
        self.add_wish()

    def event_wishDisappear(self, event):
        self.wish_input.delete(0, last='end')

    def event_wishLeave(self, event):
        self.default_wish_text = '输入模版：看十分钟小说 2'
        self.wish_input.insert(0, self.default_wish_text)

    def update_wishes_listbox(self):
        # Clear the current list to keep from add the same tasks to the list over and over again
        self.clear_wishes_listbox()
        self.clear_wishes_index()
        self.clear_wishes_score_index()
        # Populate the Listbox
        for wish in self.wishes_list:
            self.wishes_display.insert("end", wish.text)
            self.wishes_index_display.insert("end", wish.index)
            self.wishes_score_display.insert("end", wish.score)

    def clear_wishes_listbox(self):
        self.wishes_display.delete(0, "end")

    def clear_wishes_index(self):
        self.wishes_index_display.delete(0, 'end')

    def clear_wishes_score_index(self):
        self.wishes_score_display.delete(0, 'end')

def main():
    todo_list = TODO_list()

if __name__ == "__main__":
    main()