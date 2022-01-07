from tkinter import *
#for nem window
def new():
    new_window = Toplevel() #this new window is linked with the older window
    #new_window = Tk() #This is the dependent window
    window.destroy() #will close the old window
window = Tk()
frame = Frame(window,bg='blue',bd=5,relief=RAISED)
Button(frame,text='W',font=('Consolas',15)).pack(side=TOP)
Button(frame,text='T',font=('Consolas',15)).pack(side=TOP)
Button(frame,text='R',font=('Consolas',15)).pack(side=LEFT)
Button(frame,text='E',font=('Consolas',15)).pack(side=LEFT)
Button(frame,text='S',font=('Consolas',15)).pack(side=LEFT)
Button(frame,text='A',font=('Consolas',15)).pack(side=LEFT)
#frame.place(x=0,y=0)
#creting new window
Button(window,text='New window',command=new).pack()
window.mainloop()