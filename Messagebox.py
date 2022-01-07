from tkinter import *
from tkinter import messagebox
def click():
    #messagebox.showerror(title='ERROR',message='Something wrong happened')
    #messagebox.showwarning(title='WARNING',message='You are a robot')
    #messagebox.showinfo(title='This is an info message box',message='You are a person')

    #if messagebox.askokcancel(title='proove',message='Are you a human being?'):
        #messagebox.showinfo(title='This is an info message box', message='You are a person')
    #else:
        #messagebox.showwarning(title='WARNING', message='You are a robot')

    #if messagebox.askretrycancel(title='proove',message='Do you want to retry?'):
        #print('Retried succesful')
    #else:
        #print('you haven\'t tried')
    #if messagebox.askyesno(title='yes or no box',message='Do you like coding'):
        #print('Thanks for liking it')
    #else:
        #print('Ooops! you said NO!!')
    #ans = messagebox.askquestion(title='ask question',message='Do you like me')
    #if (ans == 'yes'):
        #print('Thanks for liking me\nI like you too')
    #else:
        #print("Mmmmmh no problem")
    ans =messagebox.askyesnocancel(title='yes no cancel box',message='Do you like codig',
                                   icon='info'# you can change the icon i.e error and warning
                                   )
    if (ans==True):
        print('That is great I like it too')
    elif(ans==False):
        print('Why do you reading my codes')
    else:
        print('You have dogged the question')
window = Tk()
icon = PhotoImage(file = "LOGO.png")
window.iconphoto(True,icon)

button = Button(window,command=click,text='click me')
button.pack()
window.mainloop()