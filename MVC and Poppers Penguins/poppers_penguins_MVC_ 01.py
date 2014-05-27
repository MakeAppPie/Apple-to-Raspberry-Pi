# poppers_penguins_MVC_01
#MVC Version 2014 May 26
#implements the View and View Controller according to the MVC template

from tkinter import *
from tkinter import ttk
from tkinter import messagebox
 
 
class MyViewController():
    def __init__(self,parent):
        self.parent = parent;      
         
#(6)added instantiation of view 2014 May 26
        self.view = MyView(self)

#Handlers -- target action
    def addPressed(self):
#(7a) Change getters and setters for the view
        self.view.setLabelText(self.view.getPenguinType()+ ' Penguin '+ self.view.getPenguinAction() + ' Added')
        
    def quitPressed(self):
#(7b) Change getters and setters for the view
        self.view.setLabelText('Quitting')
        answer = messagebox.askokcancel('Ok to Quit','This will quit the program. \n Ok to quit?')
        if answer==True:
            self.parent.destroy()
 
class MyView(Frame):
#(1) Change parent to vc and add a frame 2014 May 26 a  
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
#(2)remove self.vc here as vc calls this, not the othere way around.   2014 May 26
#        self.vc = MyViewController(self)
        self.loadView()
#       self.makeStyle()
         
#Handlers -- our pseudo-controller
#(3)removed from application 2014-May-26
#    def addPressed(self):
#        self.labelText.set(self.penguinType.get()+ ' Penguin '+ self.penguinAction.get() + ' Added')
#    def quitPressed(self):
#        self.labelText.set('Quitting')
#        answer = messagebox.askokcancel('Ok to Quit','This will quit the program. \n Ok to quit?')
#        if answer==True:
#            self.parent.destroy()

#(4)added setters and getters for the properties 2014-May 26
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
#(5)changed the command= to refer to the view controller 2014-May-26
    # self.addPressed now is self.vc.addPressed
    # self.quitPressed now is self.vc.quitPressed
    def loadView(self):
        #label
        status_label = ttk.Label(self.frame, textvariable = self.labelText)
        status_label.grid(row=0,column=0,columnspan=4,sticky=EW)
    #buttons
        add_button = ttk.Button(self.frame,command= self.vc.addPressed,text = 'Add')
        add_button.grid(row = 2, column = 0)
        quit_button = ttk.Button(self.frame, command = self.vc.quitPressed, text = 'Quit')
        quit_button.grid(row = 2, column = 3)
    #combobox
        penguinType_values = ['Adele','Emperor','King','Blackfoot','Humboldt','Galapagos','Macaroni','Tux','Oswald Cobblepot','Flippy Slippy']
        penguinType_combobox = ttk.Combobox(values = penguinType_values, textvariable = self.penguinType)
        penguinType_combobox.grid(row =1, column = 0)
        penguinAction_values = ['Happy','Sad','Angry','Standing','Swimming','Eating','Sleeping','On Belly','Plotting Evil','Singing','Dancing','Being Cute']
        penguinAction_combobox = ttk.Combobox(values = penguinAction_values, textvariable = self.penguinAction)
        penguinAction_combobox.grid(row=1, column = 3)


         
def main():
    root = Tk()
#(8) Set up the main loop 2014 May 26
    root.title("Popper's Penguins")         
    app = MyViewController(root)
    root.mainloop() 
 
 
if __name__ == '__main__':
    main()  
