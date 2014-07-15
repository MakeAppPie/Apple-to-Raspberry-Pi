##!/usr/bin/python
#
#Run a clock for a specified time with a specified interval

from tkinter import *
import threading
import _thread
from datetime import datetime, timedelta
from time import sleep


# a flag to determine if the processing loop stops
exitFlag = 1

# The thread class subclassed--
#overwrite __init__() with name and data for the thread
#Overwrite run() with the code to run in the thread
class MyThread (threading.Thread):
    def __init__(self,threadID,name,delay,counter):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.counter = counter
        self.delay = delay
    def run(self):
        print ("Starting " + self.name)
        #print_count(self.delay, self.counter)
        print_timeCount(self.delay,self.counter)
        print ("Exiting " + self.name)

def print_timeCount(interval,counter):
    countDown = counter  
    global exitFlag    
    period = timedelta(seconds=interval)
    nextTime = datetime.now() + period
    print('Timer start') #for debugging
    print(str(countDown))
    timeString.set(str(countDown))
    while countDown > 0 and exitFlag:
        if nextTime <= datetime.now():
             nextTime += period
             countDown -= interval
             print(str(countDown))
             timeString.set(str(countDown))
    exitFlag = 1 #end of loop and function


def print_count(delay,counter):
    while counter and exitFlag :
        time.sleep(delay)
        print(str(counter) )
        timeString.set(str(counter))
        counter -= 1
      
def startClock():
    #print_count(1,10)
    global thread1
    thread1=MyThread(2,"thread1",10)
    thread1.start()
    
def stopClock():
    global exitFlag
    global thread1
    if thread1.isAlive():
        exitFlag = 0
        
#make the view, which is a single button to stop the thread
#make the window
root=Tk()
root.title('My Clock')
#make the frame
frame = Frame(root)
frame.grid(row=0, column=0)

#make the button
startbutton = Button(frame,text = "Start Clock", command = startClock)
startbutton.grid(row=1,column=0,sticky=NSEW)
stopButton = Button( frame, text = "Stop Clock", command = stopClock)
stopButton.grid(row=1,column=1,sticky=NSEW)
timeString = StringVar()
timeString.set("A timer with interrupts")

timeLabel = Label(frame,textvariable = timeString)
timeLabel.grid(row = 0,column=0,sticky=NSEW)

mainloop()
