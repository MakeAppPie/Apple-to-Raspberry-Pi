# poppers_penguins_01
#Basic Object Oriented GUI 
from tkinter import *
from tkinter import ttk
from tkinter import messagebox


class MyViewController():
    def __init__(self,parent):
        self.parent = parent;
        
        
    #Handlers -- target action
    def addPressed(self):
        
        self.parent.labelText.set(self.parent.penguinType.get()+ ' Penguin '+ self.parent.penguinAction.get() + ' Added')
    def quitPressed(self):
        self.view.labelText.set('Quitting')
        answer = messagebox.askokcancel('Ok to Quit','This will quit the program. \n Ok to quit?')
        if answer==True:
            self.destroy()

class MyView(Frame):
  
    def __init__(self,parent):

        self.frame = Frame.__init__(self, parent, background="#5555ff", takefocus = 0)
        self.parent = parent
        self.parent.title("Popper's Penguins")
        
        self.labelText = StringVar()
        self.labelText.set("Popper's Penguins Ready")
        #some UI variables
        self.penguinType = StringVar()
        self.penguinType.set('Penguin Type')
        self.penguinAction = StringVar()
        self.penguinAction.set('Penguin Action')

        self.vc = MyViewController(self)
        self.loadView()
        self.makeStyle()
        
#Handlers -- our pseudo-controller
    def addPressed(self):
        self.labelText.set(self.penguinType.get()+ ' Penguin '+ self.penguinAction.get() + ' Added')
    def quitPressed(self):
        self.labelText.set('Quitting')
        answer = messagebox.askokcancel('Ok to Quit','This will quit the program. \n Ok to quit?')
        if answer==True:
            self.parent.destroy()
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
    def loadView(self):
        #label
        status_label = ttk.Label(self.frame, textvariable = self.labelText)
        #status_label.configure(font=('Sans','16','bold'),background = 'blue', foreground = '#eeeeff')
        status_label.grid(row=0,column=0,columnspan=4,sticky=EW)

        add_button = ttk.Button(self.frame,command= self.addPressed,text = 'Add')
        add_button.grid(row = 2, column = 0)
 

        penguinType_values = ['Adele','Emperor','King','Blackfoot','Humboldt','Galapagos','Macaroni','Tux','Oswald Cobblepot','Flippy Slippy']
        penguinType_combobox = ttk.Combobox(values = penguinType_values, textvariable = self.penguinType)
        penguinType_combobox.grid(row =1, column = 0)

        penguinAction_values = ['Happy','Sad','Angry','Standing','Swimming','Eating','Sleeping','On Belly','Plotting Evil','Singing','Dancing','Being Cute']
        penguinAction_combobox = ttk.Combobox(values = penguinAction_values, textvariable = self.penguinAction)
        penguinAction_combobox.grid(row=1, column = 3)
        
def main(): 
    root = Tk()
    app = MyView(root)
    root.mainloop()  


if __name__ == '__main__':
    main()  
