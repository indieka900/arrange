from tkinter import *

def display():
    if(x.get()==1):
        print("Agreed")
    else:
        print("Disagreed")

window = Tk() #instntiate an instance of a window
#window.geometry("420x360") for size
window.title("Joseph first GUI program")
icon = PhotoImage(file = "LOGO.png")
window.iconphoto(True,icon)
x = IntVar()
check_button = Checkbutton(window,text="Click to agree ",variable=x,
                           onvalue=1,offvalue=0,command=display,
                           fg="green", bg="black",
                           activeforeground="green", activebackgroun="black",
                           padx=25,pady=10)
check_button.pack()
window.config(background="purple")#you can search in google hex color picker for more color index
window.mainloop()#dispalys our windows