from tkinter import *


class App(object):

    def __init__(self, master):
        self.master = master
        self.frame = Frame(master)
        self.frame.grid()
        self.addFrame = Frame(master)
        self.addFrame.grid(row=0, column=0, columnspan=2, sticky='N')
        self.listFrame = Frame(master)
        self.listFrame.grid(row=1, column=0, columnspan=2, sticky='NW')
        self.todoList = []
        self.buttonList = []  #<--- button list is here now
        self.initUI()

    def event_add(self):
        self.add()

    def initUI(self):

        self.entryBox = Entry(self.frame, width = 15)

        self.entryBox.grid(row=0, column=0, sticky='N')

        self.addButton = Button(self.frame, text="<-ADD->", command=self.add)
        self.addButton.bind_all("<Return>", self.add)
        self.addButton.grid(row=0, column=1, sticky='N')


    def removeCheckButton(self, button_no):
        # - CONFUSED HOW TO REMOVE THE SPECIFIC CHECKBUTTON
       # print(button_no, self.buttonList[button_no])
        #self.buttonList[button_no].grid_forget()
        self.buttonList[button_no].destroy()
       # del self.buttonList[button_no]
       # del self.todoList[button_no]


    def add(self):
        entry = self.entryBox.get()
        self.entryBox.delete(0, END)
        self.todoList.append(entry)
        print(self.todoList)
        var1 = IntVar()
        #self.buttonList = [] #<--- not sense having this here
      #  for n in range(len(self.todoList)): #<-- this for also very strange here.
        n = len(self.buttonList)
        lx = Checkbutton(self.listFrame,
                         text=self.todoList[n],
                         variable=self.todoList[n],
                         command=lambda ni=n: self.removeCheckButton(ni))
        lx.grid(row=n, column=0, sticky='NW')
        self.buttonList.append(lx)
         #   print(self.buttonList)


root = Tk()
app = App(root)
root.mainloop()