from tkinter import *
import numpy as np
import math

#Setup
root = Tk()
root.resizable(False, False)
root.title("Wgt Calculator")
root.geometry("220x280")
root.grid_columnconfigure((0,1), weight=1)
root.configure(background='SlateGray4')

#Frames
topFrame = Frame(root, bg = 'SlateGray4')
bottomFrame = Frame(root, bg = 'SlateGray4')
leftFrame = Frame(root, bg = 'SlateGray4')
rightFrame = Frame(root, bg = 'SlateGray4')

topFrame.pack(side = TOP)
bottomFrame.pack(side=BOTTOM)
leftFrame.pack(side=LEFT)
rightFrame.pack(side = RIGHT)

#Labels
Label1 = Label(leftFrame, text='Distance', bg = 'SlateGray4', fg = 'gray12', font = 'verdana 18 bold', justify = 'left')
Label2 = Label(leftFrame, text = 'Elevation', bg = 'SlateGray4', fg = 'gray12', font = ('verdana 18 bold'), justify = 'left')
Label3 = Label(leftFrame, text = 'Wind', bg = 'SlateGray4', fg = 'gray12', font = ('verdana 18 bold'), justify = 'left')
Label4 = Label(leftFrame, text = 'Direction', bg = 'SlateGray4', fg = 'gray12', font = ('verdana 18 bold'), justify = 'left')
Label5 = Label(leftFrame, text = 'T or F', bg = 'SlateGray4', fg = 'gray12', font = ('verdana 18 bold'), justify = 'left')
Label6 = Label(leftFrame, text = 'Total', bg = 'SlateGray4', fg = 'gray12', font = ('verdana 18 bold'), justify = 'left')

Label1.pack(side = TOP)
Label2.pack(side = TOP)
Label3.pack(side = TOP)
Label4.pack(side = TOP)
Label5.pack(side = TOP)
Label6.pack(side = TOP)

#Entrys
distanceEntry = Entry(rightFrame, width = 7, justify = 'center', bg = 'gray20', font = 'Sone, 17 bold', fg = 'khaki3')
elevationEntry = Entry(rightFrame, width = 7, justify = 'center', bg = 'gray20', font = 'Sone, 17 bold', fg = 'khaki3')
windEntry = Entry(rightFrame, width = 7, justify = 'center', bg = 'gray20', font = 'Sone, 17 bold', fg = 'khaki3')
directionEntry = Entry(rightFrame, width = 7, justify = 'center', bg = 'gray20', font = 'Sone, 17 bold', fg = 'khaki3')
teeorfairwayEntry = Entry(rightFrame, width = 7, justify = 'center', bg = 'gray20', font = 'Sone, 17 bold', fg = 'khaki3')
totalEntry = Entry(rightFrame, width = 7, justify = 'center', bg = 'gray20', font = 'Sone, 17 bold', fg = 'khaki3')
distanceEntry.pack(ipady = 2)
elevationEntry.pack(ipady = 2)
windEntry.pack(ipady = 2)
directionEntry.pack(ipady = 2)
teeorfairwayEntry.pack(ipady = 2)
totalEntry.pack(ipady = 2)

#Button Click Function
def oneclick():
    array1=[distanceEntry.get(),
    elevationEntry.get(),
    windEntry.get(),
    directionEntry.get(),
    teeorfairwayEntry.get()]
    array1numpy = np.array(array1)
    
    distanceint = int(array1numpy[0])
    elevationint = int(array1numpy[1])
    windint = int(array1numpy[2])
    directionint = int(array1numpy[3])
    
    cosine = abs(math.cos(directionint*3.14159265359/30))
    sine = abs(math.sin(directionint*3.14159265359/30))
    if(elevationint>0):
    	elevationtotal = elevationint/3
    else:
    	elevationtotal = elevationint/3.5

    if(array1numpy[4]=='t'):
    	teeorfairway_multi = 1.15
    if(array1numpy[4]=='f'):
    	teeorfairway_multi = 1

    if(windint>0):
    	windtotal = distanceint/180*windint*cosine
    else:
    	windtotal = distanceint/260*windint*cosine
    if(windint>28):
    	windmulti = 1.2
    elif(windint>25):
    	windmulti = 1.15
    elif(windint>22):
    	windmulti = 1.1
    elif(windint>19):
    	windmulti = 1.05
    else:
    	windmulti = 1

    total = (distanceint+elevationtotal+windtotal*teeorfairway_multi*windmulti)
    total_round = round(total, 1)
    totalEntry.delete(0, END)
    totalEntry.insert(0, total_round)

#Buttons
enterButton = Button(bottomFrame, text = 'Enter', bg = 'khaki3' , height = '2', width = '30', command=oneclick, font = 'Sone, 17 bold')
enterButton.pack()


root.mainloop()
