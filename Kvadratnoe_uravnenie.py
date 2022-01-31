from tkinter import *
import matplotlib.pyplot as plt#Y=....
import numpy as np# x=[min,max]
global D , j, graf
D=-1
t="Нет решений!"
graf=False
def lahenda():
    global D , t, graf
    if(a.get()!="" and b.get()!="" and c.get()!=""):
        #if(float (a.get())==0 and float (b.get())==0 and float (c.get())==0):
        a_=int(a.get())
        b_=int(b.get())
        c_=int(c.get())
        D=b_*b_-4*a_*c_
        if D>0:
            x1=round((-1*b_+sqrt(D))/(2*a_),2)
            x2=round((-1*b_-sqrt(D))/(2*a_),2)
            t=(f"X1={x1}, \nX2={x2}")
            graf=True
        elif D==0:
            x1=round((-1*b_)/(2*a_),2)
            t=(f"X1={x1}")
            graf=True
        else:
            t="Корней нет"
            graf=False
        vastus.configure(text=f"D={D}\n{t}")
        a.configure(bg="lightblue")
        b.configure(bg="lightblue")
        c.configure(bg="lightblue")
    else:
        if a.get()=="":
             a.configure(bg="red")
        if b.get()=="":
            b.configure(bg="red")
        if c.get()=="":
            c.configure(bg="red")
    return D,t,graf
def graafik():
    graf,D,t=lahenda()
    if graf==True:
        a_=float(a.get())
        b_=float(b.get())
        c_=float(c.get())
        x0=(-b_)/(2*a_)
        y0=a_*x0*x0+b_*x0+c_
        x1 = np.arange(x0-10, x0+10, 0.5)#min max step [min,max]
        y1=a_*x1*x1+b_*x1+c_
        fig = plt.figure()
        plt.plot(x1, y1,'r-d')
        plt.title('Квадратное уравнение')
        plt.ylabel('y')
        plt.xlabel('x')
        plt.grid(True)
        plt.show()
        text=f"Вершина параболлы ({x0},{y0})"
    else:
        text=f"График нет возможности построить"
    vastus.configure(text=f"D={D}\n{t}\n{text}")
t=0
def veel():
    global t
    if t==0:
        aken.geometry(str(aken.winfo_width())+"x"+str(aken.winfo_height()+200))
        btn_veel.config(text="Уменьшить окно")
        t=1
    else:
        aken.geometry(str(aken.winfo_width())+"x"+str(aken.winfo_height()-200))
        btn_veel.config(text="Увеличить окно")
        t=0
def kala():
    x1 = np.arange(0, 9.5, 0.5)#min max step
    y1=(2/27)*x1*x1-3
    x2 = np.arange(-10, 0.5, 0.5)#min max step
    y2=0.04*x2*x2-3
    x3 = np.arange(-9, -2.5, 0.5)#min max step
    y3=(2/9)*(x3+6)**2+1
    x4 = np.arange(-3, 9.5, 0.5)#min max step
    y4=(-1/12)*(x4-3)**2+6
    x5 = np.arange(5, 9, 0.5)#min max step
    y5=(1/9)*(x5-5)**2+2
    x6 = np.arange(5, 8.5, 0.5)#min max step
    y6=(1/8)*(x6-7)**2+1.5
    x7 = np.arange(-13, -8.5, 0.5)#min max step
    y7=(-0.75)*(x7+11)**2+6
    x8 = np.arange(-15, -12.5, 0.5)#min max step
    y8=(-0.5)*(x8+13)**2+3
    x9 = np.arange(-15, -10, 0.5)#min max step
    y9=[1]*len(x9)
    x10 = np.arange(3, 4, 0.5)#min max step
    y10=[3]*len(x10)
    fig = plt.figure()
    plt.plot(x1, y1,x2,y2,x3,y3,x4,y4,x5,y5,x6,y6,x7,y7,x8,y8,x9,y9,x10,y10)
    plt.title('Кит')
    plt.ylabel('y')
    plt.xlabel('x')
    plt.grid(True)
    plt.show()
def vihmavari(): pass
def konn(): pass
def figura():
    global var
    valik=var.get()
    if valik==1:
        kala()
    elif valik==2:
        vihmavari()
    else:
        konn()
def vihmavari():
    x1 =np.arange(-12,12,0.5)
    y1 =(1/18)+2
aken=Tk()
aken.title("Квадратное уравнение")
aken.geometry("800x300")
f1=Frame(aken,width=800,height=300)
f1.pack(side=TOP)
f2=Frame(aken,width=800,height=300)
f2.pack(side=BOTTOM)

nupp=Button(f1,text="Решить",font="Arial 25",height=2,width=10,bg="green",fg="black",relief="raised",command=lahenda )
nupp.pack(side=RIGHT)
nupp1=Button(f1,text="График",font="Arial 25",height=2,width=10,bg="green",fg="black",relief="raised")
nupp1.pack(side=RIGHT)




lbl=Label(f1, text = "Решение квадратного уравнения", font="Arial_Bold 20", width=30, fg="green", bg="lightblue",relief=RAISED)  
lbl.pack()
vastus=Label(f1, text = "Решение", font="Arial 25", width=30, fg="black", bg="yellow",relief=RAISED)  
vastus.pack(side=BOTTOM)
a=Entry(f1,text="",width=2,font="Arial_Bold 30",fg="green",bg="lightblue")
a.pack(side=LEFT)
a.bind("<Return>",lahenda)
lbl1=Label(f1,text="x**2",height=2,width=5,font="Arial 15",fg="green",bg="lightblue",relief="solid")
lbl1.pack(side=LEFT)
b=Entry(f1,text="",width=2,font="Arial_Bold 30",fg="green",bg="lightblue")
b.pack(side=LEFT)
b.bind("<Return>",lahenda)
lbl2=Label(f1,text="x+",height=2,width=5,font="Arial 15",fg="green",bg="lightblue",relief="solid")
lbl2.pack(side=LEFT)
lbl3=Label(f1,text="=0",height=2,width=5,font="Arial 15",fg="green",bg="lightblue",relief="solid")
lbl3.pack(side=RIGHT)
c=Entry(f1 ,text="",width=2,font="Arial_Bold 30",fg="green",bg="lightblue")
c.pack(side=LEFT)
c.bind("<Return>",lahenda)


btn_veel=Button(f2,text="Увеличить окно", font="Calibri 26",bg="yellow",command=veel)
btn_veel.pack(side=TOP)
var=IntVar()
r1=Radiobutton(f2,text="Кит", variable=var,value=1, font="Calibri 26")
r2=Radiobutton(f2,text="Очки", variable=var,value=2,font="Calibri 26")
r3=Radiobutton(f2,text="Лягуха", variable=var,value=3,font="Calibri 26")
r1.pack()
r2.pack()
r3.pack()


aken.mainloop()
