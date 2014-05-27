#MVC_Template_01
#2014 May 23  by Steven Lipton http://makeAppPie.com
#Controller initializing MVC -- simplest version possible.  
from tkinter import *

#
# A A Model-View-Controller framework for TKinter.
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
        self.model = MyModel(self)    # initializes the model
        self.view = MyView(self)  #initializes the view
        #initialize objects in view
        self.view.setEntry_text('Add to Label') #a non cheat way to do MVC wiht tkinter control variables
        self.view.setLabel_text('Ready')
 #event handlers       
    def quitButtonPressed(self):
        self.parent.destroy()
    def addButtonPressed(self):
        self.view.setLabel_text(self.view.entry_text.get())
        self.model.addToList(self.view.entry_text.get())
    def listChangedDelegate(self):
        #model internally chages and needs to signal a change
        print(self.model.getList())
       

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
        label = Label(self.frame,textvariable = self.label_text).grid(row = 2, column = 0, columnspan = 3, sticky = EW)
    def __init__(self,vc):
        self.frame=Frame()
        self.frame.grid(row = 0,column=0)
        self.vc = vc
        self.entry_text = StringVar()
        self.entry_text.set('nil')
        self.label_text = StringVar()
        self.label_text.set('nil')
        self.loadView()
    def getEntry_text(self):
    #returns a string of the entry text
        return self.entry_text.get()
    def setEntry_text(self,text):
    #sets the entry text given a string
        self.entry_text.set(text)
    def getLabel_text():
    #returns a string of the Label text
        return self.label_text.get()
    def setLabel_text(self,text):
    #sets the label text given a string
        self.label_text.set(text)

    
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
#Delegates-- Model would call this on internal change
    def listChanged(self):
        self.vc.listChangedDelegate()
#setters and getters        
    def getList(self):
        return self.myList
    def initListWithList(self, aList):
        self.myList = aList
    def addToList(self,item):
        print("returned")
        myList = self.myList
        myList.append(item)
        self.myList=myList
        self.listChanged()
        

def main(): 
    root = Tk()
    frame = Frame(root,bg='#0555ff' )
    root.title('Hello Penguins')
    app = MyController(root)
    root.mainloop()  


if __name__ == '__main__':
    main()  
