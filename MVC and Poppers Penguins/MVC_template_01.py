#MVC_Template_01
#2014 May 23  by Steven Lipton http://makeAppPie.com
#Controller initializing MVC -- simplest version possible.  
from tkinter import *

#
# A A Model-View-Controller template for TKinter. (with example)
# Model: Data Structure. Controller can send messages to it, and model can respond to message. 
# View : User interface elements. Controller can send messages to it. View can call methods from Controller when an event happens.
# Controller: Ties View and Model together. turns UI responses into chages in data.

#
#Controller: Ties View and Model together.
#       --Performs actions based on View events. 
#       --Sends messages to Model and View and gets responses
#       --Has Delegates 

class MyController():
    def __init__(self,parent):
        self.parent = parent
        self.label_text = StringVar() #a cheat way to put all control variable in controller. not exactly MVC
        self.label_text.set('Ready')

        self.model = MyModel(self)    # initialozes the model
        self.view = MyView(self)  #initializes the view

        #initialize objects in view
        self.view.setEntry_text('Add to Label') #a non cheat way to do MVC wiht tkinter control variables

 #Event handlers       
    def quitButtonPressed(self):
        self.parent.destroy()
    def addButtonPressed(self):
        self.label_text.set(self.view.entry_text.get())
        self.model.addToList(self.view.entry_text.get())
    def listChangedDelegate(self):
        #Model internally changes and needs to signal a change
        print(self.model.getList())
        return 'list Changed'

#View : User interface elements.
#       --Controller can send messages to it.
#       --View can call methods from Controller vc when an event happens.
#       --NEVER communicates with Model.
#       --Has setters and getters to communicate with controller

class MyView(Frame):
    def loadView(self):
        quitButton = Button(self.frame,text = 'Quit', command= self.vc.quitButtonPressed).grid(row = 0,column = 0)
        addButton = Button(self.frame,text = "Add", command = self.vc.addButtonPressed).grid(row = 0, column = 1)
        entry = Entry(self.frame,textvariable = self.entry_text).grid(row = 1, column = 0, columnspan = 3, sticky = EW)
        label = Label(self.frame,textvariable = self.vc.label_text).grid(row = 2, column = 0, columnspan = 3, sticky = EW)
    def __init__(self,vc):
        self.frame=Frame()
        self.frame.grid(row = 0,column=0)
        self.vc = vc
        self.entry_text = StringVar()
        self.entry_text.set('nil')
        #print (self.vc.label_text.get())
        self.loadView()
    def getEntry_text(self):
    #returns a string of the entry text
        return self.entry_text.get()
    def setEntry_text(self,text):
    #sets the entry text given a string
        self.entry_text.set(text)
    
#Model: Data Structure.
#   --Controller can send messages to it, and model can respond to message. 
#   --Uses delegates from vc to send messages to the Controll of internal change
#   --NEVER communicates with View
#   --Has setters and getters to communicate with Controller
       
class MyModel():
    def __init__(self,vc):
        self.vc = vc 
        self.myList = ['duck','duck','goose']
        self.count = 0

#example of a delegate. Model would call this on internal change
    def listChanged(self):
        self.vc.listChangedDelegate()

        
    def getList(self):
        return self.myList
    def initListWithList(self, aList):
        self.myList = aList
    def addToList(self,item):
        print("returned")
        myList = self.myList
        myList.append(item)
        self.myList=myList
        quack = self.listChanged()
        

def main(): 
    root = Tk()
    frame = Frame(root,bg='#0555ff' )
    root.title('Hello Penguins')
    app = MyController(root)
    root.mainloop()  


if __name__ == '__main__':
    main()  
