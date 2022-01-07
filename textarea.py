#text widget= functions like a text area,you can enter multiple line
from tkinter import *
def submit():
    inp = text.get("1.0",END)
    print(inp)
window = Tk()
text = Text(window,bg='light green',font=('Ink free',25),height=8,width=20,
            padx=20,pady=20,fg='dark blue')
button = Button(window,text='Submit',command=submit)
button.pack(side = BOTTOM)
text.pack()
window.mainloop()