#tkinter_playbox_03
# learning about configure and lambda

from tkinter import *

colors = ('red','yellow','aquamarine','cyan','blue','magenta')

#make the window
root= Tk()
root.title('Tkinter Color Button Playbox')

#make a variable
myColorText = StringVar()
myColorText.set('Quit')

#make a frame
rootframe = Frame(root)
rootframe.grid(row=0,column=0)


#event handlers
def buttonPressed(buttoncolor):
    quitbutton.configure(background = buttoncolor)
    newtext = 'Quit-- ' + buttoncolor
    myColorText.set(newtext)

#make buttons
col=0
for color in colors:
    print (color)
    button1 = Button(rootframe, bg = 'blue',command = lambda color=color:buttonPressed(color))
    button1.grid(row = 0, column = col)
    button1.configure(text=color, background = color, activebackground = color, activeforeground = 'white')
    col=col+1
quitbutton = Button(rootframe, textvariable = myColorText, command = quit)
quitbutton.grid(row = 1, column = 0, columnspan = 3, sticky = E+W)

#start the main loop 
root.mainloop()
