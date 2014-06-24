# poppers_penguins_MVC_06a
#MVC Version 2014 May 28
#Change: Adds the text box

from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from tkinter import scrolledtext
 
 
class MyViewController():

    
    def __init__(self,parent):

        self.reportHeader = "Penguin Type\tPenguin Action\n"+ "="*35 +"\t"+"="*35+"\n"
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
            if len(listString)>0:
                listString = listString + '\t' + element
            else:
                listString = element
        return listString
    def listToListString(self,aList):
        #a temporary method for making lists compatible
        #with listbox till I find something better
        #returns a string we can place in a StringVar
        listString = str() 
        for record in aList:
            elementString = self.spaceToUnderscore(record,20)
            listString = listString + '\n' + elementString
        return listString
    def listToTextString(self,aList):
        #method for making lists compatible
        #with the text box
        #returns a string we can insert in the text box
        listString = self.reportHeader 
        for record in aList:
            elementString = self.elementListToString(record)
            listString = listString + '\n' + elementString
        return listString
            
#delegate for the model            
    def modelDidChangeDelegate(self):
        aList = self.model.getList()
        aListString = self.listToListString(aList)
        self.view.setDataList(aListString)
        self.view.setTextboxText(self.listToTextString(aList))
    
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
# instantiate the text box
        self.selectedLine = 1
        self.dataList_textbox = Text(self.frame)       
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
#Setters and getters for the text widget
    def setTextboxText(self,listString):
        #delete everything in a text box and replace with the text
        self.dataList_textbox.delete("0.0",END)
        self.dataList_textbox.insert('0.0',listString)
    def getTextBoxtext(self):
    #return a string of all the boxes contents
        return self.dataList_textbox.get('0.0',END)
    def getSelectedLine(self): #for use externally as an index. Do not use the property straight
        return self.selectedLine - 1


# Internal behavior for the text box                               
    def mouseSelectTextLine(self, event):
        mousePosition = "@"+str(event.x)+","+ str(event.y) #get the mouse position
        self.selectedIndex = self.dataList_textbox.index(mousePosition) #convert to textbox index
        splitIndex = self.selectedIndex.split('.') #get the row we are on
        selectedLine = splitIndex[0]
        self.highlightTextLine(selectedLine)
 
    def kbSelectTextLine(self,event):
        selected=self.selectedLine
        if event.keysym == "Up":
            selectedLine = str(selected - 1)
        else:
            selectedLine = str(selected + 1)
        self.highlightTextLine(selectedLine)
    
    def highlightTextLine(self,selectedLine):     
        self.selectedLine=int(selectedLine)
        selectedLineStart = selectedLine + ".0" #beginning and end of line
        selectedLineEnd = self.dataList_textbox.index(selectedLine + ".end")
         #highlight the line on the box
        self.dataList_textbox.tag_delete("selectedLine")
        self.dataList_textbox.tag_add("selectedLine",selectedLineStart,selectedLineEnd)
        self.dataList_textbox.tag_config("selectedLine",background = "blue",foreground = "white")
                
      
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
        buttonFrame = ttk.Frame(self.frame)
        buttonFrame.grid(row = 1, column = 0)
        
        status_label = ttk.Label(self.frame, textvariable = self.labelText)
        #status_label.configure(font=('Sans','16','bold'),background = 'blue', foreground = '#eeeeff')
        status_label.grid(row=0,column=0,sticky=NSEW)
 
        add_button = ttk.Button(buttonFrame,command= self.vc.addPressed,text = 'Add')
        add_button.grid(row = 0, column = 0,sticky = NSEW)
        quit_button = ttk.Button(buttonFrame, command = self.vc.quitPressed, text = 'Quit')
        quit_button.grid(row = 0, column = 1,sticky = NSEW)
 
        penguinType_values = ['Adele','Emperor','King','Blackfoot','Humboldt','Galapagos','Macaroni','Tux','Oswald Cobblepot','Flippy Slippy']
        penguinType_combobox = ttk.Combobox(buttonFrame,values = penguinType_values, textvariable = self.penguinType)
        penguinType_combobox.grid(row =1, column = 0,sticky = EW)
 
        penguinAction_values = ['Happy','Sad','Angry','Standing','Swimming','Eating','Sleeping','On Belly','Plotting Evil','Singing','Dancing','Being Cute']
        penguinAction_combobox = ttk.Combobox(buttonFrame, values = penguinAction_values, textvariable = self.penguinAction)
        penguinAction_combobox.grid(row=1, column = 1,sticky = EW)

        listFrame = ttk.Frame(self.frame)
        listFrame.grid(row =2,column = 0)
        
        dataList_yScroll = Scrollbar(listFrame, orient=VERTICAL)
        dataList_yScroll.grid(row=0,column=1,sticky = NS)
    
        dataList_listbox = Listbox(listFrame, listvariable= self.dataList, width = 40)
        dataList_listbox.grid(row=0, column = 0, sticky=NSEW)
#bind the listbox and scrollbar
        dataList_listbox.configure(yscrollcommand = dataList_yScroll.set)
        dataList_yScroll.configure(command=  dataList_listbox.yview)
#set up the text box
        self.dataList_textbox = scrolledtext.ScrolledText(listFrame, tabs= ("10c"))
        self.dataList_textbox.grid(row=1, column = 0, sticky = NSEW);
 #       self.dataList_textbox.insert("0.0","Penguin\tPenguin Action") #test data
#Added event binding to a button release
        self.dataList_textbox.bind('<ButtonRelease>',self.mouseSelectTextLine)
        self.dataList_textbox.bind('<Down>',self.kbSelectTextLine)
        self.dataList_textbox.bind('<Up>',self.kbSelectTextLine)        

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
