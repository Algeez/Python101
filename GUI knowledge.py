from tkinter import*
from tkinter import ttk
from tkinter import messagebox

######CSV################
import csv
def writecsv(datalist):
    with open('data.csv','a',encoding='utf-8',newline='')as file:
        fw=csv.writer(file)
        fw.writerow(datalist)

def readcsv():
    with open('data.csv','a',encoding='utf-8',newline='')as file:
        fr=csv.reader(file)
        data=list(fr)
    return data



#########################
GUI= Tk()
GUI.title('Program')
GUI.geometry('800x400')

L1= Label(GUI,text='Trading Performance',font=('Angsana New',30),fg='blue')
L1.place(x=50,y=20)

B1 = ttk.Button(GUI,text='Total Money')
B1.pack(ipadx=20,ipady=20)
B1.place(x=30,y=100)

def Button2():
    text='profit 5 million'
    messagebox.showinfo('realized',text) 

FB1= LabelFrame(GUI)
FB1.place(x=30,y=100)
B2 = Button(GUI,text='profit',command= Button2)
B2.pack(ipadx=20,ipady=20)
B2.place(x=30,y=150)

def Button3():
    text='loss 2 milllion'
    messagebox.showinfo('realized',text)
FB3= LabelFrame(GUI)
FB3.place(x=30,y=150)    
B3 = Button(GUI,text='loss',command=Button3)
B3.pack(ipadx=60,ipady=60)
B3.place(x=30,y=200)

#############SECTION RIGHT#############
LF1=ttk.LabelFrame(GUI,text='Information')
LF1.place(x=400,y=50)
v_data= StringVar()
E1 = ttk.Entry(LF1,textvariable=v_data,font=('Angsana New',25))
E1.pack(pady=10,padx=10)

from datetime import datetime

def Savedata():
    t = datetime.now().strftime('%Y%M%D %H%M%S')
    data = v_data.get()
    text = [t,data]
    writecsv(text)
    v_data.set('')

B4=ttk.Button(LF1,text='save',command=Savedata)
B4.pack(ipadx=20,ipady=20)
GUI.mainloop()
