from tkinter import *
from tkinter import ttk
import tkinter as tk
import random

#Create an instance of Tkinter frame
win = Tk()
count,yl,countt=0,0,0
flag=True
def convertList(list1):  
    str = ''  # initializing the empty string  
  
    for i in list1: #Iterating and adding the list element to the str variable  
        str += i  
  
    return str

def prevent(event):
    global count
    count += 1
    if count==6:
        button.config(state=DISABLED)

#Set the geometry of Tkinter frame
win.geometry("750x250")
win.configure(bg="#FDF5DF")
def wor():
   global countt,flag
   flag=True
   countt+=1
   #q=Toplevel()
   global yl
   a=str(e.get())
   print(a)
   count=0
   for i in a:
        if i == answer[count]:
            l2=Label(q,text=i,font="Calibri 12 bold",foreground="white",background="green",width=1)#exact character match draws a green square
            l2.place(x=20*count,y=50+yl,width=20,height=30)
        elif i in answer:
            flag=False
            l4=Label(q,text=i,font="Calibri 12 bold",foreground="white",background="#f4c430",width=1) #else if character anywhere in word draws yellow
            l4.place(x=20*count,y=50+yl,width=20,height=30)
        else:
            flag=False
            l5=Label(q,text=i,font="Calibri 12 bold",foreground="white",background="grey",width=1)
            l5.place(x=20*count,y=50+yl,width=20,height=30)
        count+=1
   yl+=30
   if(countt==5):
       print(countt)
       l2=Label(q,text="Game Over",font="Calibri 12 bold",foreground="white",background="green",width=40)
       l2.pack()
       l8=Label(q,text="Correct Answer:{}".format(answer),font="Calibri 12 bold",foreground="white",background="green",width=40)
       l8.pack()
       button['state']=tk.DISABLED
       win.after(5000,win.destroy)
   if flag==True:
       l7=Label(q,text="YOU WIN",font="Calibri 12 bold",foreground="white",background="green",width=40)
       l7.pack()
       button['state']=tk.DISABLED
       win.after(5000,win.destroy)

#Create an entry widget
ans=["hello","watch","where"]
answer=random.sample(ans,1)
answer=convertList(answer)
print(answer)


def callback(sv):
    c = sv.get()[0:5]
    sv.set(c)
    if len(sv.get())==5:
        button['state']=tk.NORMAL
    else:
        button['state']=tk.DISABLED

button= ttk.Button(win, text= "Enter", command= wor,state=DISABLED)
button.pack(pady=10)
button.bind("<Button-1>", prevent)
sv = StringVar()
sv.trace("w", lambda name, index, mode, sv=sv: callback(sv))
e = Entry(win, textvariable=sv)
e.pack()


#Create a button to validate the entry widget
q=Toplevel()
q.title("wordle")
q.geometry("500x500")
q.configure(bg="#FDF5DF")
win.mainloop()
