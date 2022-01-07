from tkinter import *
from tkinter import colorchooser #is a submodule
def click():
    #color=colorchooser.askcolor()
    #print(color)
    #colhex=color[1]
    #print(colhex)
    #window.config(bg=color[1]) #will change background colour
    window.config(bg=colorchooser.askcolor()[1])
window=Tk()
window.geometry('420x420')
button = Button(text='Click',command=click,bg=colorchooser.askcolor()[1])
button.pack()
window.mainloop()