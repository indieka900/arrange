from tkinter import *
from tkinter import filedialog
def openFile():
    filepath = filedialog.askopenfilename(title='open file',
                                          filetype=(('text files','.txt'),
                                                    ('all file','*.*')),
                                          )
    #print(filepath)
    file = open(filepath,'r')
    print(file.read())
    file.close()
def saveFile():
    file = filedialog.asksaveasfile(defaultextension='.txt',
                                    filetype=[('text file','.txt'),
                                              ('word file', '.docx'),
                                              ('HTML file', '.html'),
                                              ('all files', '.*')
                                              ])
    if file is None: #To remove exception
        return
    filetxt = str(text.get(1.0,END)) #to enter using a text area
    #filetxt = input('Enter some text here: ') #using the console
    file.write(filetxt)
    file.close()

window=Tk()
#button = Button(window,text='Open',command=openFile)
button = Button(window,text='Save',command=saveFile)
text = Text(window)
text.pack()
button.pack()
window.mainloop()
