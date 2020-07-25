from tkinter import *
import calendar

def show():
    year = int(spin2.get())
    mont = int(spin1.get())
    cal = calendar.month(year,mont)
    screen.delete(0.0,END)
    screen.insert(INSERT,cal)

root = Tk()
root.title('Calender')
root.geometry('300x350')
root.configure(background='olive')
Label(root,text='Calender',font='Arial 20 bold').pack(pady=10)
frm1 = Frame(root)
Label(frm1,text='Month',font='arial 12 bold').pack(side=LEFT)
spin1 = Spinbox(frm1,from_=1,to_=12,width=5,font='arial 12')
spin1.pack(side=LEFT,padx=5)
Label(frm1,text='Year',font='arial 12 bold').pack(padx=5,side=LEFT)
spin2 = Spinbox(frm1,from_=1947,to_=2030,width=5,font='arial 12')
spin2.pack(side=LEFT,padx=5)
frm1.pack(pady=10)
Button(text='Show',font='arial 10 bold', command=show).pack(pady=10)
screen = Text(root, width=30,height=10)
screen.pack()

root.mainloop()
