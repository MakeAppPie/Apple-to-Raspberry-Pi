#Poppers penguins_TEST_03
#Controller initilizing a view take 2
from tkinter import *
from tkinter import messagebox
from tkinter import ttk

class MyController():
    def __init__(self,parent):
        self.parent = parent
        # control Variables/Properties
        self.labelText = StringVar()
        self.labelText.set("Popper's Penguins Ready")
        self.penguinType = StringVar()
        self.penguinType.set('Penguin Type')
        self.penguinAction = StringVar()
        self.penguinAction.set('Penguin Action')

        self.model = MyModel()    # initializes the model
        self.view = MyView(self)  #initializes the view
        
    def quitPressed(self):
        answer = messagebox.askokcancel('Ok to Quit','This will quit the program. \n Ok to quit?')
        if answer==True:
            self.parent.destroy()
    def addPressed(self):
        self.labelText.set(self.penguinType.get()+ ' Penguin '+ self.penguinAction.get() + ' Added')
    
class MyView(Frame):

#Style Sheet
    def makeStyle(self):
        self.s = ttk.Style()
        self.s.configure('TFrame',background = '#5555ff')
        self.s.configure('TButton',background = 'blue', foreground = '#eeeeff', font = ('Sans','14','bold'), sticky = EW)
        self.s.configure('TLabel',font=('Sans','16','bold'),background = '#5555ff', foreground = '#eeeeff')
        self.s.map('TButton', foreground = [('hover','#5555ff'), ('focus', 'yellow')])
        self.s.map('TButton', background = [('hover', '#eeeeff'),('focus','orange')])
        self.s.configure('TCombobox',background = '#5555ff',foreground ='#3333ff',font = ('Sans',18))
  
    
    def loadView(self):
        status_label = ttk.Label(self.frame, textvariable = self.vc.labelText)
        status_label.grid(row=0,column=0,columnspan=4,sticky=EW)
        quit_button = ttk.Button(self.frame, command = self.vc.quitPressed, text = 'Quit')
        quit_button.grid(row = 2, column = 3)
        add_button = ttk.Button(self.frame,command= self.vc.addPressed,text = 'Add')
        add_button.grid(row = 2, column = 0)

        penguinType_values = ['Adele','Emperor','King','Blackfoot','Humboldt','Galapagos','Macaroni','Tux','Oswald Cobblepot','Flippy Slippy']
        penguinType_combobox = ttk.Combobox(values = penguinType_values, textvariable = self.vc.penguinType)
        penguinType_combobox.grid(row =1, column = 0)

        
        penguinAction_values = ['Happy','Sad','Angry','Standing','Swimming','Eating','Sleeping','On Belly','Plotting Evil','Singing','Dancing','Being Cute']
        penguinAction_combobox = ttk.Combobox(values = penguinAction_values, textvariable = self.vc.penguinAction)
        penguinAction_combobox.grid(row=1, column = 3)
        
    def __init__(self,vc):
        self.frame=Frame()
        self.frame.grid(row = 0,column=0)
        self.vc = vc
        self.loadView()
        self.makeStyle()
        
class MyModel():
    def __init__(self):
        self.myList = ['duck','duck','goose']
        self.count = 0
    def getList(self):
        return self.myList
    def initListWithList(self, aList):
        self.myList = aList
    def addToList(self,item):
        myItem = item.get()
        myList = self.myList
        myList.append(myItem)
        self.myList=myList

def main(): 
    root = Tk()
    frame = Frame(root,bg='#0555ff' )
    root.title('Hello Penguins')
    app = MyController(root)
    root.mainloop()  


if __name__ == '__main__':
    main()  
