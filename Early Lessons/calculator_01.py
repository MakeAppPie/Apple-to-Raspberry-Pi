#Calculator_app

from tkinter import *

functionTextTuple = ('+','-','/','*','Clear')


#make the window
root= Tk()
root.title('Tkinter Simple Calcualtor')

#make a variable
myColorText = StringVar()
myColorText.set('Quit')
label1Text = StringVar()
label1Text.set('0.0')

#make a frame
rootframe = Frame(root)
rootframe.grid(row=0,column=0)
rootframe.configure(bg='black')


#event handlers
#parse the function between buttons
def buttonPressed(button_function):
    if button_function == '+':
        print ("plus")
    elif button_function == '-':
        print ("minus")
    elif button_function == '/':
        print("divided by")
    elif button_function == '*':
        print('times')
    elif button_function == 'Clear':
        print('Clear')
        label1Text.set('0.0')
    else:
        if label1Text.get()=='0.0':
            label1Text.set(str(button_function))
        else:
            label1Text.set( label1Text.get() + str(button_function))
        

#make buttons
col=0
for function_text in functionTextTuple:
    #print (function_text)
    button1 = Button(rootframe, command  = lambda function_text=function_text:buttonPressed(function_text))
    button1.grid(row = col+1, column = 0,sticky = E+W)
    button1.configure(text=function_text, activebackground = 'blue', activeforeground = 'white')
    button1.configure(relief = FLAT)
    col=col+1

for x in range(1,4):
    for y in range (0,3):
        buttonText = (x+3*y)
        button2 = Button(rootframe, text = buttonText, command =lambda buttonText = buttonText:buttonPressed(buttonText))
        button2.grid(row = y+1 ,column = x)
        
quitbutton = Button(rootframe, textvariable = myColorText, command = quit)
quitbutton.grid(row = 3, column = 4, columnspan = 2, sticky = E+W)


#make labels
label1 = Label(rootframe,textvariable = label1Text)
label1.grid(row=0,column=0, columnspan= 5, sticky = NW+E)
label1.configure(font = ('Courier', '24','bold'), bg='black',fg='white')




#start the main loop 
root.mainloop()
