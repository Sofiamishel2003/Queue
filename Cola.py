from tkinter import*
from tkinter import ttk, messagebox
class forma(Tk):
    def __init__(self):
        Tk.__init__(self)
        self.geometry("300x330")
        self.config(bg="lightblue")
        self.lb1=Label(self,text="Cola", font="Arial 16 underline", bg="lightblue")
        self.lb1.place(x=85,y=20)
        self.lb2=Label(self,text="Ingrese dato:", bg="lightblue")
        self.lb2.place(x=5,y=80)
        self.c1=Entry(self, width=15)
        self.c1.place(x=80,y=80)
        self.combo=ttk.Combobox(self, width=10)
        self.combo.place(x=180,y=80)
        self.bt=Button(self, width=10, text="HACER",command=self.hacer)
        self.bt.place(x=180,y=120)
        self.combo["values"]=["Enqueue","denqueue","Empty","Makenull"]
        self.init()
        self.mainloop()
    def init(self):
        self.sp=0
        self.data=[0]*10
        for i in range(10):
            self.data[i]=Button(self, width=10,state=DISABLED)
            self.data[i].place(x=50,y=300-i*20)
    def hacer(self):
        if(self.combo.get()=="Enqueue"):
            self.enque()
        if(self.combo.get()=="denqueue"):
            self.deque()
        if(self.combo.get()=="Empty"):
            self.empty()
        if(self.combo.get()=="Makenull"):
            self.maken()
    def enque(self):
        if(self.sp<10):
            n=self.c1.get()
            self.data[self.sp].configure(text=n)
            self.sp+=1
        else:
            messagebox.showinfo("ERROR", "LA COLA ESTA LLENA")
    def deque(self):
        if(self.sp>0):
            self.data[0].configure(text="")
            for i in range(self.sp):
                if(i==9):
                    dato=""
                else:
                    dato=(self.data[i+1].configure("text")[-1])
                self.data[i].configure(text=dato)
            self.sp-=1
        else:
            messagebox.showinfo("ERROR", "LA COLA ESTA VACIA")
    def empty(self):
        if(self.sp==0):
            messagebox.showinfo("CORRECTO", "LA COLA ESTÁ VACIA")
        else:
            messagebox.showinfo("INCORRECTO", "LA COLA NO ESTÁ VACIA")
    def maken(self):
        self.sp=0
        for i in range(10):
            self.data[i].configure(text="")
app=forma()