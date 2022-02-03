from tkinter import Tk, Entry, Button, Label, END, messagebox
from math import pi, sin, cos
class app(Tk):
    def __init__(self):
        Tk.__init__(self) #constructor
        self.geometry("700x500")
        self.config(bg="lightsteelblue")
        self.title("COLA")
        self.l1=Label(self,text="COLA", font="Arial 15 ",bg="lightsteelblue")
        self.l1.place(x=150,y=10)
        self.l2=Label(self,text="Ingrese elemento",bg="lightsteelblue")
        self.l2.place(x=30,y=40)
        self.c1=Entry(widt=20)
        self.c1.place(x=150, y=40)
        self.b1=Button(text="enqueue", width=10, command=self.doenqueue, bg="thistle")
        self.b1.place(x=20,y=100)
        self.b2=Button(text="dequeue", width=10, command=self.dodequeue, bg="thistle")
        self.b2.place(x=20,y=200)
        self.b3=Button(text="empty", width=10, command=self.doempty, bg="thistle")
        self.b3.place(x=20,y=300)
        self.b4=Button(text="Make Null", width=10, command=self.domakenull, bg="thistle")
        self.b4.place(x=20,y=400)
        self.l1= Label(text="Inicio")
        self.l2= Label(text="Fin")
        self.e1= queue(self)
    def domakenull(self):
        dato=self.e1.makenull()
        self.c1.delete(0,END)
    def doenqueue(self):
        try:
            e=self.c1.get()
            self.e1.enqueue(e)
            self.c1.delete(0, END)
        except Exception as msg:
            messagebox.showerror("ERROR", msg)
    def dodequeue(self):
        try:
            e=self.e1.dequeue()
            self.c1.delete(0, END)
            self.c1.insert(0, e)
        except Exception as msg:
            messagebox.showerror("ERROR", msg)
    def doempty(self):
       messagebox.showinfo("La cola vacia es:",str(self.e1.empty()))
class queue():
    def __init__(self, f):
        self.data=[0]*10
        self.ne=0
        self.inicio=0
        self.forma=f
        a=-pi/2
        paso=2*pi/10
        for i in range(10):
            self.data[i]=Button(width=4, height=2)
            a=a+paso
            x=450+150*cos(a)
            y=300+150*sin(a)
            self.data[i].place(x=x, y=y)
        self.forma.update_idletasks()
        self.etiquetas()
    def enqueue(self,e):
        if(self.ne<10):
            final=(self.inicio+self.ne)%10
            self.data[final].configure(text=e)
            self.ne+=1
            self.etiquetas()
        else:
            raise Exception("Cola llena")
    def dequeue(self):
        if(self.ne>0):
            temp=self.data[self.inicio].configure("text")[-1]
            self.data[self.inicio].configure(text="")
            self.inicio= (self.inicio+1)%10
            self.ne-=1
            self.etiquetas()
            return temp
        else:
            raise Exception("Cola vacía")
    def empty(self):
        return self.ne==0
    def makenull(self):
        self.ne=0
    def etiquetas(self):
        ini=self.inicio
        fin=(self.inicio+self.ne)% 10
        x= self.data[ini].winfo_x()
        y= self.data[ini].winfo_y()-20
        self.forma.l1.place(x=x,y=y)
        x= self.data[fin].winfo_x()+50
        y= self.data[fin].winfo_y()-20
        self.forma.l2.place(x=x,y=y)
app().mainloop()