# -*- coding: utf-8 -*-
"""
Created on Wed Jan  2 23:52:15 2019
GUI for remote amp servo control
@author: Alex
"""

from tkinter import *
import csv

root = Tk()
root.wm_title("Amp Controller")



#Events here, as per standard rules
def deploy():
    volume = volSlider.get()
    gain = gainSlider.get()
    treble = trebleSlider.get()
    middle = midSlider.get()
    bass = bassSlider.get()
    
    message = Toplevel()
    message.title("Values Sent")
    messageLabel = Label(message, text="Volume={0},\nGain={1},\nTreble={2},\nMiddle={3},\nBass={4}".format(volume, gain, treble, middle, bass))
    messageLabel.pack()

def loadButton():
    selection = presetsList.get(ACTIVE)
    with open('savefile.csv',mode='r') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        lineCount = 0
        for row in csv_reader:
            if row['name'] == selection:          
                volSlider.set(row['volume'])
                gainSlider.set(row['gain'])
                trebleSlider.set(row['treble'])
                midSlider.set(row['middle'])
                bassSlider.set(row['bass'])
        csv_file.close()




def saveWindow():
    save = Tk()
    save.wm_title("Save New Preset")
    
    label = Label(save, text="Name:")
    label.pack(side=LEFT)
    
    entryBox = Entry(save)
    entryBox.pack(side=LEFT)
    entryBox.focus_set()
    
    def savePreset():
    
        name = entryBox.get()
        volume = volSlider.get()
        gain = gainSlider.get()
        treble = trebleSlider.get()
        middle = midSlider.get()
        bass = bassSlider.get()
    
        with open('savefile.csv',mode='a',newline='') as csv_file:
            writer = csv.writer(csv_file,delimiter=',',quotechar='"',quoting=csv.QUOTE_MINIMAL)
            writer.writerow([name,volume,gain,treble,middle,bass])
            csv_file.close()
    
        presetsList.delete(0,END)
        with open('savefile.csv',mode='r') as csv_file:
            csv_reader = csv.DictReader(csv_file)
            lineCount = 0
            insert = 0
            for row in csv_reader:
                if lineCount == 0:
                    lineCount += 1
                presetsList.insert(insert, row["name"])
                insert += 1
            csv_file.close()
        
        save.destroy()
    
    ok = Button(save, text="Save", command=savePreset)
    ok.pack()
    
    





#Loading save file
try:
    file = open('savefile.csv','r')
    file.close()
except:
    file = open('savefile.csv','w')
    file.write("Name,Volume,Gain,Treble,Middle,Bass")
    file.close()

with open('savefile.csv',mode='r') as csv_file:
    csv_reader = csv.DictReader(csv_file)
    




#Left side container with sliders
leftBlock = Frame(root)
leftBlock.grid(row=0, column=0, padx=10, pady=5)


#Labels
volLabel = Label(leftBlock, text="Volume")
volLabel.grid(row=1,column=0)

gainLabel = Label(leftBlock, text="Gain")
gainLabel.grid(row=1,column=1)

trebleLabel = Label(leftBlock, text="Treble")
trebleLabel.grid(row=1,column=2)

midLabel = Label(leftBlock, text="Middle")
midLabel.grid(row=1,column=3)

bassLabel = Label(leftBlock,text="Bass")
bassLabel.grid(row=1,column=4)

#Sliders
volSlider = Scale(leftBlock, from_=10, to=1)
volSlider.grid(row=2,column=0)


gainSlider = Scale(leftBlock, from_=10, to=1)
gainSlider.grid(row=2,column=1)


trebleSlider = Scale(leftBlock, from_=10, to=1)
trebleSlider.grid(row=2,column=2)


midSlider = Scale(leftBlock, from_=10, to=1)
midSlider.grid(row=2,column=3)


bassSlider = Scale(leftBlock, from_=10, to=1)
bassSlider.grid(row=2,column=4)


#Right Side
rightBlock = Frame(root)
rightBlock.grid(row=0,column=1,padx=10,pady=5)


#List of presets
presetsList = Listbox(rightBlock)

with open('savefile.csv',mode='r') as csv_file:
    csv_reader = csv.DictReader(csv_file)
    lineCount = 0
    insert = 0
    for row in csv_reader:
        if lineCount == 0:
            lineCount += 1
        presetsList.insert(insert, row["name"])
        insert += 1
    csv_file.close()
presetsList.grid(row=0,column=0, pady=5, padx=10)

#Buttons Block
buttonsBlock = Frame(root)
buttonsBlock.grid(row=1,column=1)
#Buttons
loadBtn = Button(buttonsBlock, text="Load", command=loadButton)
loadBtn.grid(row=0,column=0,padx=20,pady=5)

saveBtn = Button(buttonsBlock, text="Save", command=saveWindow)
saveBtn.grid(row=0,column=1,padx=20,pady=5)

deployBtn = Button(root, text="Deploy", command=deploy)
deployBtn.grid(row=2,column=1,pady=10, ipadx=5,ipady=5)
root.mainloop()