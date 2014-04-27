#Power_Panel_02
#code By Steven Lipton

from tkinter import *

#make the window
root=Tk()
root.title('Power Panel #2')

#make the frame
frame = Frame(root)
frame.grid(row=0, column=0)

#make our variables
voltage_value = DoubleVar()
time_value = DoubleVar()
#onOff_button_title = StringVar()

#set initial values for the variables
voltage_value.set(120.0)
time_value.set(2400.0)
#onOff_button_title.set('Off')

#event Handlers
def onOffButtonPressed():
    if onOff_button_title.get() == 'Off':
        onOff_button_title.set('On')
    else:
        onOff_button_title.set('Off')
 
#render button
onOff_button_title = StringVar()        
onOff_button_title.set('Off')
onOff_button = Button(frame, command = onOffButtonPressed)
onOff_button.grid(row = 2, column = 4, rowspan=2, columnspan = 2,sticky = SW + NE)
onOff_button.configure(background = 'blue')
onOff_button.configure(textvariable = onOff_button_title)

#new code for image lesson

#make another button
bitmap_Button = Button(frame)
bitmap_Button.grid(row=2, column = 3)
bitmap_Button.configure(text = 'info')

image_button = Button(frame)
image_button.grid(row=2 column = 4)


#render Labels
voltage_label = Label(frame, text = 'Voltage')
voltage_label.grid(row = 1,column = 0, sticky = E)

time_label = Label(frame, text = 'Time')
time_label.grid(row = 0, column = 0, sticky = E)

time_value_label = Label(frame, textvariable = time_value, justify = LEFT)
time_value_label.grid(row =0, column= 1, sticky = W)


#render text fields
voltage_value_entry = Entry(frame, textvariable = voltage_value)
voltage_value_entry.grid(row=1, column = 1)



#start the main loop
mainloop()
