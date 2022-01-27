from tkinter import *
D=0
def lahendus_diskriminandi_kaudu(event):
    global D
    D=b*b-4*a*c 
    if D > 0:
        x1 = (-b + sqrt(D)) / (2*a)
        x2 = (-b - sqrt(D)) / (2*a)
        print("Дискриминант имеет два корня\n D:\n x1:\n x2:")
    elif D == 0:
        x1=x2=(-b/2*a)
        print("Дискриминант имеет один корень")
    else:
        print("Решения нет")

aken=Tk()
aken.title("Window name")
aken.geometry("700x300")

nupp=Button(aken,text="Решить",font="Arial 20",height=2,width=16,bg="green",fg="black",relief="raised")
nupp.pack(side=RIGHT)
nupp.bind("<Button-1>", lahendus_diskriminandi_kaudu)


lbl1=Label(aken, text = "Решение квадратного уравнения", font="Arial_Bold 20", width=30, fg="green", bg="lightblue",relief=RAISED)  
lbl1.pack()
lbl1=Label(aken,text="x**2",height=2,width=5,font="Arial 15",fg="green",bg="lightblue",relief="solid")
lbl1.place(x=100,y=115)
lbl2=Label(aken,text="x+",height=2,width=5,font="Arial 15",fg="green",bg="lightblue",relief="solid")
lbl2.place(x=240,y=115)
lbl3=Label(aken,text="=0",height=2,width=5,font="Arial 15",fg="green",bg="lightblue",relief="solid")
lbl3.place(x=375,y=115)

a=Entry(aken,text="",width=2,font="Arial_Bold 30",fg="green",bg="lightblue")
a.place(x=30,y=115)
a.bind("<Return>",lahendus_diskriminandi_kaudu)
b=Entry(aken,text="",width=2,font="Arial_Bold 30",fg="green",bg="lightblue")
b.place(x=180,y=115)
b.bind("<Return>",lahendus_diskriminandi_kaudu)
c=Entry(aken,text="",width=2,font="Arial_Bold 30",fg="green",bg="lightblue")
c.place(x=320,y=115)
c.bind("<Return>",lahendus_diskriminandi_kaudu)

nupp1=Label(aken, text = "Решение", font="Arial 25", width=30, fg="black", bg="yellow",relief=RAISED)  
nupp1.pack(side = BOTTOM)
aken.mainloop()