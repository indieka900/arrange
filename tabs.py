from tkinter import *
#from tkinter import ttk
from tkinter.ttk import *
import time
def start():
    GB = 500
    download = 0
    speed = 1
    while(download<GB):
        time.sleep(0.05)
        #bar["value"]+=(speed/GB)*100
        download+=speed
        percent.set(str(int((download/GB)*100))+'%')
        text.set(str(download)+'/'+str(GB)+' GB completed')
        window.update_idletasks()
window= Tk()
percent = StringVar()
text = StringVar()
'''notebook = ttk.Notebook(window) #widget that manages collections of windows/displays
tab1 = Frame(notebook) #new frame for tab 1
tab2 = Frame(notebook) #new frame for tab 2
notebook.add(tab1,text='Tab1')
notebook.add(tab2,text='Tab2')
Label(tab1,text='Welcome this is Tab1',width=50,height=25).pack()
Label(tab2,text='Goodbye this is Tab2',width=50,height=25).pack()
notebook.pack(expand=True,fill='both')#expand = exands to fill any space not otherwise used

'''
#grid = geometry manager that organizes widgets in a table-like stracture in aparent
'''Label(window,text='Enter your info: ',font = ('Times New Roman',15,'underline','bold')).grid(row=0,column=0,columnspan=2)
firstnamelabel = Label(window,text='First name: ').grid(row=1,column=0)
firstnameEntry = Entry(window).grid(row=1,column=1)
secondnamelabel = Label(window,text='Last name: ').grid(row=2,column=0)
secondnameEntry = Entry(window).grid(row=2,column=1)
emaillabel = Label(window,text='Email: ').grid(row=3,column=0)
emailEntry = Entry(window).grid(row=3,column=1)
Button(window,text='Submit').grid(row=4,column=0,columnspan=2)
'''
#for progress bar
'''bar = Progressbar(window,orient=HORIZONTAL,length=300)
bar.pack(pady=10)
percentLabel = Label(window,textvariable=percent).pack()
taskLabel = Label(window,textvariable=text).pack()
Button(window,text='Download',command=start).pack()
'''
#canvas = widget that is used to draw graphs,plots,images is a window
canvas=Canvas(window,height=500,width=500)
#canvas.create_line(0,0,500,500,fill= 'red',width=5)
canvas.create_line(0,500,500,50,fill= 'green',width=5)
#canvas.create_rectangle(50,50,250,250,fill= 'purple',width=5)
points = [0,500,500,500,500,35,]
canvas.create_polygon(points,fill='pink',outline='black',width=5)
canvas.create_arc(10,10,300,300,fill='green',extent=180,width=5)
canvas.create_arc(10,10,300,300,fill='yellow',extent=180,start=180,width=5)

canvas.create_oval(100,100,200,200,fill='blue',width=10)
canvas.pack()
window.mainloop()