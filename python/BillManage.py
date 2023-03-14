from tkinter import *
root=Tk()
root.geometry("1000x500")
root.title("Bill Management")
root.resizable(False,False)
Label(text="Bill Management",bg="black",fg="white",font=("calibri",30),width="300",height="2").pack()
#menu card
f=Frame(root,bg="lightgreen",highlightbackground="black",highlightthickness=1,width=300, height=370)
f.place(x=10,y=118)


def Reset():
    entry_Bajji.delete(0,END)
    entry_Tee.delete(0, END)
    entry_Pongall.delete(0, END)
    entry_Susla.delete(0, END)
    entry_upma.delete(0, END)
    entry_ragiball.delete(0, END)
    entry_dosa.delete(0, END)

def Total():
    try:a1=int(Bajji.get())
    except: a1=0

    try:a2=int(Tee.get())
    except: a2=0

    try:a3=int(Pongall.get())
    except: a3=0

    try:a4=int(Susla.get())
    except: a4=0

    try:a5=int(upma.get())
    except: a5=0

    try:a6=int(ragiball.get())
    except: a6=0

    try:a7=int(dosa.get())
    except: a7=0


#def cost of each items
    c1=60*a1
    c2=12*a2
    c3=70*a3
    c4=60*a4
    c5=50*a5
    c6=76*a6
    c7=60*a7
    totalcost=c1+c2+c3+c4+c5+c6+c7
    lbl_total=Label(f2,font=("aria",20,"bold"),text="Total",width=16,fg="lightyellow",bg="black")
    lbl_total.place(x=0,y=50)
    entry_total=Entry(f2,font=("aria",20,"bold"),textvariable=Total_bill,bd=6,width=15,bg="lightgreen")
    entry_total.place(x=20,y=100)

    
    Total_bill="Rs",str("%.2f" %totalcost)
    Total_bill.set(string_bill)

Label(f,text="Menu",font=("Gabriola",40,"bold"),fg="black",bg="lightgreen").place(x=100,y=0)


Label(f,font=("Lucida calligraphy",15,"bold"),text="Bajji...........Rs.60/plate",fg="black",bg= "lightgreen").place(x=10,y=80)
Label(f,font=("Lucida calligraphy",15,"bold"),text="Tee...........Rs.12/plate",fg="black",bg= "lightgreen").place(x=10,y=110)
Label(f,font=("Lucida calligraphy",15,"bold"),text="Pongall.........Rs.70/plate",fg="black",bg= "lightgreen").place(x=10,y=150)
Label(f,font=("Lucida calligraphy",15,"bold"),text="Susla...........Rs.60/plate",fg="black",bg= "lightgreen").place(x=10,y=180)
Label(f,font=("Lucida calligraphy",15,"bold"),text="Upma...........Rs.50/plate",fg="black",bg= "lightgreen").place(x=10,y=210)
Label(f,font=("Lucida calligraphy",15,"bold"),text="Ragi Boll.ia....Rs.76/plate",fg="black",bg= "lightgreen").place(x=10,y=240)
Label(f,font=("Lucida calligraphy",15,"bold"),text="Dosa...........Rs.60/plate",fg="black",bg= "lightgreen").place(x=10,y=280)

#Bill
f2=Frame(root,bg="lightyellow",highlightbackground="black",highlightthickness=1,width=300,height=370)
f2.place(x=690,y=118)

Bill=Label(f2,text="Bill",font=("calibri",20),bg="lightyellow")
Bill.place(x=120,y=10)


f1=Frame(root,bd=5,height=370,width=300,relief=RAISED)
f1.pack()

Bajji =StringVar()
Tee =StringVar()
Pongall =StringVar()
Susla =StringVar()
upma =StringVar()
ragiball =StringVar()
dosa =StringVar()


lbl_Bajji=Label(f1,font=("arial",20,"bold"),text="Bajji",width=12,fg="blue4")
lbl_Tee=Label(f1,font=("arial",20,"bold"),text="Tee",width=12,fg="blue4")
lbl_Pongall=Label(f1,font=("arial",20,"bold"),text="Pongalla",width=12,fg="blue4")
lbl_Susla=Label(f1,font=("arial",20,"bold"),text="susla",width=12,fg="blue4")
lbl_upma=Label(f1,font=("arial",20,"bold"),text="upma",width=12,fg="blue4")
lbl_ragiball=Label(f1,font=("arial",20,"bold"),text="ragiball",width=12,fg="blue4")
lbl_dosa=Label(f1,font=("arial",20,"bold"),text="dosa",width=12,fg="blue4")

lbl_Bajji.grid(row=1,column=0)
lbl_Tee.grid(row=2,column=0)
lbl_Pongall.grid(row=3,column=0)
lbl_Susla.grid(row=4,column=0)
lbl_upma.grid(row=5,column=0)
lbl_ragiball.grid(row=6,column=0)
lbl_dosa.grid(row=7,column=0)



#entry
entry_Bajji=Entry(f1,font=("arial",20,"bold"),textvariable=Bajji,bd=6,width=8,bg="lightpink")
entry_Tee=Entry(f1,font=("arial",20,"bold"),textvariable=Tee,bd=6,width=8,bg="lightpink")
entry_Pongall=Entry(f1,font=("arial",20,"bold"),textvariable=Pongall,bd=6,width=8,bg="lightpink")
entry_Susla=Entry(f1,font=("arial",20,"bold"),textvariable=Susla,bd=6,width=8,bg="lightpink")
entry_upma=Entry(f1,font=("arial",20,"bold"),textvariable=upma,bd=6,width=8,bg="lightpink")
entry_ragiball=Entry(f1,font=("arial",20,"bold"),textvariable=ragiball,bd=6,width=8,bg="lightpink")
entry_dosa=Entry(f1,font=("arial",20,"bold"),textvariable=dosa,bd=6,width=8,bg="lightpink")


entry_Bajji.grid(row=1,column=1)
entry_Tee.grid(row=2,column=1)
entry_Pongall.grid(row=3,column=1)
entry_Susla.grid(row=4,column=1)
entry_upma.grid(row=5,column=1)
entry_ragiball.grid(row=6,column=1)
entry_dosa.grid(row=7,column=1)


btn_Reset=Button(f1,bd=5,fg="black",bg="lightblue",font=("arial",16,"bold"),width=10,text="Reset",command=Reset)
btn_Reset.grid(row=8,column=0)

btn_Total=Button(f1,bd=5,fg="black",bg="lightblue",font=("arial",16,"bold"),width=10,text="Total",command=Total)
btn_Total.grid(row=8,column=1)



root.mainloop()






