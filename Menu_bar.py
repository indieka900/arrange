from tkinter import *
from tkinter import messagebox
def openFile():
    #print("The file has been opened")
    messagebox.showerror(title='ERROR',message='Something wrong happened')
def save_as():
    print("The option doesnot exists")
def saveFile():
    print("Your file has been saved")
def copyFile():
    messagebox.askquestion(title='Copy',message='select file to copy')
def cutFile():
    messagebox.askquestion(title='Cut',message='select file to cut')
def pasteFile():
    messagebox.askquestion(title='Paste',message='file copied')
def findFile():
    messagebox.showerror(title='ERROR',message='Something wrong happened')
def usageFile():
    messagebox.showerror(title='ERROR',message='Something wrong happened')
window = Tk()
menubar = Menu(window)
window.config(menu=menubar)
fileMenu = Menu(menubar,tearoff=0)
editMenu = Menu(menubar,tearoff=0)
menubar.add_cascade(label='File',menu=fileMenu)
menubar.add_cascade(label='Edit',menu=editMenu)
fileMenu.add_command(label='Open',command=openFile)
fileMenu.add_separator()
fileMenu.add_command(label='Save as',command=save_as)
fileMenu.add_command(label='Save',command=saveFile)
fileMenu.add_separator()
fileMenu.add_command(label='Exit',command=quit)
#editmenu
editMenu.add_command(label='Copy',command=copyFile)
editMenu.add_command(label='Cut',command=cutFile)
editMenu.add_command(label='Paste',command=pasteFile)
editMenu.add_separator()
editMenu.add_command(label='Find',command=findFile)
editMenu.add_command(label='Find usage',command=usageFile)
editMenu.add_separator()
editMenu.add_command(label='Exit',command=quit)
window.mainloop()