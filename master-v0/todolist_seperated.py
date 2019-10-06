import tkinter
from tkinter import messagebox
import random

WINDOW_HEIGHT=1200
WINDOW_WIDTH=600
BUTTON_HEIGHT=2
BUTTON_WIDTH=10


class Item:
    def __init__(self, id, content):
        self.index=id
        if len(content.split(" ")) == 1:
            self.text=content.split(" ")[0]
        elif not content.split(" ")[-1].isdigit():
            self.text=content.split(" ")[:]
        else:
            self.text=content.split(" ")[:-1]
        self.text=''.join(self.text)
        score=content.split(" ")[-1]
        if score.isdigit():
            self.score=score
        else:
            self.score=0


class Project:
    def __init__(self, root, start_column, title):
        self.root=root
        self.title=title
        self.items_list=[]
        self.total_score=0
        try:
            self.read_file()
        except:
            pass
        self._build_window(start_column, start_column+1, start_column+2)
        self.update_listbox()
    
    def read_file(self):
        file_name=self.title+".txt"
        f=open(file_name, 'r', encoding='utf-8')
        sourceInLines=f.readlines()  # 按行读出文件内容
        f.close()
        new=[]  # 定义一个空列表，用来存储结果
        for line in sourceInLines:
            temp1=line.strip('\n')  # 去掉每行最后的换行符'\n'
            temp2=temp1.split(' ')  # 以','为标志，将每行分割成列表
            self.total_score += int(temp2[-1])
            new.append(temp2)  # 将上一步得到的列表添加到new中
        for n in new:
            content=str(n[1]) + " " + str(n[2])
            new_item=Item(n[0],content)
            self.items_list.append(new_item)


    def _build_window(self, c1, c2, c3):
        self._build_index(column=c1)
        self._build_list(c2)
        self._build_score_list(column=c3)
        self._build_score_analysis(5)

    def _build_index(self, column):
        self.num_label=tkinter.Label(self.root, text="序号", width=3, bg="white")
        self.num_label.grid(row=1, column=column)
        # 显示序号
        self.index_display=tkinter.Listbox(self.root, width=3, height=20)
        self.index_display.grid(row=2, column=column, rowspan=12)

    def _build_list(self, column):
        if self.title == "task":
            text="任务清单"
            default_text="输入模板：看一篇paper 5"
        if self.title == "wish":
            text="愿望商店"
            default_text="输入模板：看十分钟小说 2"
        self.top_display=tkinter.Label(self.root, width=36, text=text, padx=10, pady=0, bg="SkyBlue", )
        self.top_display.grid(row=0, column=column)

        self.input=tkinter.Entry(self.root, width=36, bg="SkyBlue", )
        self.input.bind('<Return>', self.event_Save)
        self.input.bind('<ButtonPress>', self.event_Disappear)
        self.input.bind("<FocusOut>", self.event_Leave)

        self.input.insert(0, default_text)
        self.input.grid(row=1, column=column)

        # 显示窗口
        self.display=tkinter.Listbox(self.root, width=40, height=20)
        self.display.bind('<Delete>', self.eventDeleteOne)
        self.display.grid(row=2, column=column, rowspan=7)

        # lb for listbox

    def _build_score_list(self, column):
        self.score_label=tkinter.Label(self.root, text="对应积分", width=4, height=BUTTON_HEIGHT, padx=10, pady=0, bg="lightCyan")
        self.score_label.grid(row=1, column=column)

        # 显示序号
        self.score_display=tkinter.Listbox(self.root, width=6, height=20)
        self.score_display.grid(row=2, column=column, rowspan=12)

    def _build_score_analysis(self, column):
        if self.title == "task":
            default_text="累计积分"
            label_row=1
        if self.title == "wish":
            default_text="愿望积分"
            label_row=3

        self.score_label=tkinter.Label(self.root, text=default_text, width=8, height=BUTTON_HEIGHT, padx=10, pady=0,
                                                bg="Violet")
        self.score_label.grid(row=label_row, column=column)
        self.score_value=tkinter.Label(self.root, text=self.total_score, width=8, height=BUTTON_HEIGHT, padx=10,
                                                pady=0, bg="cornsilk")
        self.score_value.grid(row=label_row+1, column=column)

    def add_item(self):
        # Get the task to add
        self.item_content=self.input.get()
        self.items_num=len(self.items_list)
        print("num:", self.items_num)
        self.item_id=self.items_num + 1
        self.new_item=Item(self.item_id, self.item_content)
        # Make sure the task is not empty
        if self.new_item.text != "":
            # Append to the list
            self.items_list.append(self.new_item)
            self.total_score += int(self.new_item.score)
            self.score_value['text']=self.total_score
            # Update the listbox
            self.update_listbox()
        else:
            # tkinter.messagebox.showwarning("Warning", "Please enter a task.")
            pass
        self.input.delete(0, "end") # clears the input box after a new task is entered

    def eventDeleteOne(self, event):
        self.del_one()

    def event_Save(self, event):
        self.add_item()

    def event_Disappear(self, event):
        self.input.delete(0, last='end')

    def event_Leave(self, event):
        self.default_wish_text='输入模版：看十分钟小说 2'
        self.input.insert(0, self.default_wish_text)

    def clear_listbox(self):
        self.display.delete(0, "end")

    def clear_index(self):
        self.index_display.delete(0, 'end')

    def clear_score_index(self):
        self.score_display.delete(0, 'end')

    def update_listbox(self):
        # Clear the current list to keep from add the same tasks to the list over and over again
        self.clear_listbox()
        self.clear_index()
        self.clear_score_index()
        # Populate the Listbox
        for item in self.items_list:
            self.display.insert("end", item.text)
            self.index_display.insert("end", item.index)
            self.score_display.insert("end", item.score)

    def clear_listbox(self):
        self.display.delete(0, "end")

    def clear_wishes_index(self):
        self.index_display.delete(0, 'end')

    def clear_wishes_score_index(self):
        self.score_display.delete(0, 'end')

    def del_all(self):
        confirmed=tkinter.messagebox.askyesno("Please Confirm", "Do you really want to delete all?")
        if confirmed == True:
            # Since we are changing the list, it needs to be global.
            # Clear the tasks list
            self.tasks_list=[]
            self.total_score=0
            self.score_value['text']=self.total_score
            # Update the listbox
            self.update_listbox()
        self.sort_asc()

    def del_one(self):
        # Get the text of the currently selected item
        text=self.display.get("active")
        for t in self.items_list:
            if text == t.text:
                self.total_score -= int(t.score)
                self.score_value['text']=self.total_score
                self.items_list.remove(t)
        self.sort_asc()

    # TODO 根据ID进行重新排序！
    def sort_asc(self):
        # sort the list
        tem_list=[]
        for i in range(len(self.items_list)):
            tem_task=self.items_list[i]
            tem_task.index=i+1
            tem_list.append(tem_task)
        self.items_list=tem_list

        #update the listbox
        self.update_listbox()

    def save_to_local(self):
        file_name=self.title + ".txt"
        f=open(file_name, 'w', encoding='utf-8')
        for t in self.items_list:
            f.write(str(t.index))
            f.write(" ")
            f.write(t.text)
            f.write(" ")
            f.write(str(t.score))
            f.write("\n")
        f.close()


class TODO_list:
    def __init__(self):
        #Create root window
        self.root=tkinter.Tk()
        # Change root window background color
        self.root.configure(bg="white")
        # Change the title
        self.root.title("骆永乐的任务清单商店")

        # Change the window size
        self.root.geometry("1200x600")
        # Create an empty list
        self.project_list=[]
        self._build_window()

    def _build_window(self):
        self.task_project=Project(self.root, 2, "task")
        self.wish_project=Project(self.root, 7, "wish")
        self.project_list.append(self.task_project)
        self.project_list.append(self.wish_project)
        self.check=tkinter.Label(self.root, text="账单", width=8, height=BUTTON_HEIGHT, padx=10, pady=0,
                                         bg="White")
        self.check.grid(row=0, column=5)
        self.check.bind_all('<Escape>', self.eventEsc)
        # Start the main events loop
        self.root.mainloop()

    def save_to_all(self):
        for p in self.project_list:
            p.save_to_local()

    def eventEsc(self, event):
        self.save_to_all()
        exit()

def main():
    todo_list=TODO_list()

if __name__ == "__main__":
    main()