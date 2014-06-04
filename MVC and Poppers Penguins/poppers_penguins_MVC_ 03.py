# poppers_penguins_MVC_03
#MVC Version 2014 May 28
#Change: Implements the Model according to the MVC template

from tkinter import *
from tkinter import ttk
from tkinter import messagebox
 
 
class MyViewController():
    def __init__(self,parent):
        self.parent = parent;      
         

        self.view = MyView(self)
        self.model = MyModel(self)
        
    #Handlers -- target action
    def addPressed(self):
        self.view.setLabelText(self.view.getPenguinType()+ ' Penguin '+ self.view.getPenguinAction() + ' Added')
        self.model.addRecordToList(self.view.getPenguinType(),self.view.getPenguinAction())
    def quitPressed(self):
        self.view.setLabelText('Quitting')
        answer = messagebox.askokcancel('Ok to Quit','This will quit the program. \n Ok to quit?')
        if answer==True:            self.parent.destroy()

#Add list to string processing for the scrollbox.
    def spaceToUnderscore(self,aList, width):
        # convert spaces to underscores in list items
        # with a triple underscore between list items
        listString = str()
        for  element in aList:
            elementString = '{:{width}}'.format(element, width=width) 
            elementString = elementString.replace(' ','_')
            listString = listString + '___' + elementString
        return listString
    def elementListToString(self,aList):
        listString = str()
        for  element in aList:
            elementString = element
            listString = listString + '\t' + elementString
        return listString
    def listToListString(self,aList):
        #a temporary method for making lists compatible
        #with listbox till I find something better
        #returns a string we can place in a StringVar
        listString = str() 
        for record in aList:
            elementString = self.spaceToUnderscore(record,20)
 #            elementString = self.elementListToString(record)
             listString = listString + '\n' + elementString
        return listString
            
#delegate for the model            
    def modelDidChangeDelegate(self):
        aList = self.model.getList()
        aListString = self.listToListString(aList)
        self.view.setDataList(aListString)
    
class MyView(Frame):
#Change parent to vc and add a frame 2014 May 26 a  
    def __init__(self,vc):
        self.frame=Frame()
        self.frame.grid(row=0,column=0)
        self.vc = vc
        
        #properties of the view 
        self.labelText = StringVar()
        self.labelText.set("Popper's Penguins Ready")
        self.penguinType = StringVar()
        self.penguinType.set('Penguin Type')
        self.penguinAction = StringVar()
        self.penguinAction.set('Penguin Action')

#Add the control variable
        self.dataList = StringVar()
        self.dataList.set ('')
        
        self.loadView()
 #       self.makeStyle()
         

#Setters and getters for the properties 2014-May 26
    def setLabelText(self,newText):
        self.labelText.set(newText)
    def getLabelText(self):
        return self.labelText.get()
    def setPenguinType(self,newType):
        self.penguinType.set(newType)
    def getPenguinType(self):
        return self.penguinType.get()
    def setPenguinAction(self,newAction):
        self.penguinAction.set(newAction)
    def getPenguinAction(self):
        return self.penguinAction.get()
#Add setters and getter for data list
    def getDataList(self):
        #returns a string
        return self.dataList.get()
    def setDataList(self,listString):
        #needs a list string delimtied by a space
        self.dataList.set(listString)      

#Style Sheet
    def makeStyle(self):
        self.s = ttk.Style()
        self.s.configure('TFrame',background = '#5555ff')
        self.s.configure('TButton',background = 'blue', foreground = '#eeeeff', font = ('Sans','14','bold'), sticky = EW)
        self.s.configure('TLabel',font=('Sans','16','bold'),background = '#5555ff', foreground = '#eeeeff')
        self.s.map('TButton', foreground = [('hover','#5555ff'), ('focus', 'yellow')])
        self.s.map('TButton', background = [('hover', '#eeeeff'),('focus','orange')])
        self.s.configure('TCombobox',background = '#5555ff',foreground ='#3333ff',font = ('Sans',18))
   
#loading the view
#changed the command= to refer to the view controller 2014-May-26
    # self.addPressed now is self.vc.addPressed
    # self.quitPressed now is self.vc.quitPressed
    def loadView(self):
        #label
        status_label = ttk.Label(self.frame, textvariable = self.labelText)
        #status_label.configure(font=('Sans','16','bold'),background = 'blue', foreground = '#eeeeff')
        status_label.grid(row=0,column=0,columnspan=8,sticky=NSEW)
 
        add_button = ttk.Button(self.frame,command= self.vc.addPressed,text = 'Add')
        add_button.grid(row = 2, column = 0)
        quit_button = ttk.Button(self.frame, command = self.vc.quitPressed, text = 'Quit')
        quit_button.grid(row = 2, column = 3)
 
        penguinType_values = ['Adele','Emperor','King','Blackfoot','Humboldt','Galapagos','Macaroni','Tux','Oswald Cobblepot','Flippy Slippy']
        penguinType_combobox = ttk.Combobox(values = penguinType_values, textvariable = self.penguinType)
        penguinType_combobox.grid(row =1, column = 0)
 
        penguinAction_values = ['Happy','Sad','Angry','Standing','Swimming','Eating','Sleeping','On Belly','Plotting Evil','Singing','Dancing','Being Cute']
        penguinAction_combobox = ttk.Combobox(values = penguinAction_values, textvariable = self.penguinAction)
        penguinAction_combobox.grid(row=1, column = 4)

        dataList_listbox = Listbox(self.frame, listvariable= self.dataList, width = 40)
        dataList_listbox.grid(row=5, column = 0, columnspan = 4,rowspan = 4, sticky=NSEW)

#(1)adding the model 2014-May-28 with convenience method
class MyModel():
    def __init__(self,vc):
        self.vc = vc
        self.myList = []
        self.count = 0
#(2)Delegate goes here. Model would call this on internal change
    def modelDidChange(self):
        self.vc.modelDidChangeDelegate()
#Setters and getters for the model   
    def getList(self):
        return self.myList
    def addToList(self,item):
        myItem = item
        myList = self.myList
        myList.append(myItem)
        self.myList=myList
        self.modelDidChange()
    def getItemAtIndex(self,index):
        return myList[index]
#other methods
    def addRecordToList(self,penguin,action):
        self.addToList([penguin,action])
    

         
def main():
    root = Tk()
#(8) Set up the main loop 2014 May 26
    frame = Frame(root, background="#5555ff", takefocus = 0)
    root.title("Popper's Penguins")         
    app = MyViewController(root)
    root.mainloop() 
 
 
if __name__ == '__main__':
    main()  
