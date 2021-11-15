from tkinter import * # Import all definitions from tkinter
from tkcalendar import DateEntry
from tkinter import ttk
from tkinter import messagebox
import mysql.connector



milk = Tk() 
milk.title("Milk Management System")
milk.geometry("1030x600")
title = Label(milk, text="Milk Management System",bd=2,relief="solid",font=("bold", 20),fg="white",bg='black')
title.pack(side=TOP,fill=X)

#====seller variable============
user_var= StringVar()
name_var= StringVar()
date_var= StringVar()
quantity_var= StringVar()
fat_var= StringVar()
amount_var= StringVar()
add_seller_var= StringVar()
name_seller_var=StringVar()
r_name=StringVar()


##===============clear entry=======================
def clear():
    user_var.set("") 
    r_name.set("")
    quantity_var.set("") 
    fat_var.set("") 
    amount_var.set("") 

#===========Insert seller data ==================
        
def seller_data(event):
    
    try:
        db = mysql.connector.connect(host="localhost",user="root",password="admin",database="mms")
        cur=db.cursor()
        ab=("insert into  " + user_var.get() + """ (Date, Quantity, Fat, Amount) values 
            ( '"""+ date_var.get() +"""', '"""+ quantity_var.get() +"""', """+ fat_var.get() +""",
             """+  amount_var.get() +""")""")
        cur.execute(ab)
        db.commit()
        messagebox.showinfo('success','Record is add successfully')
    except mysql.connector.errors.DatabaseError:
        messagebox.showerror('Warning','Your server is not connected')
     
    
    
    clear()
    userent.focus_set()
    
    
    
    

    
#==============insert data==========================
f1= Frame(milk,bd=2, relief='solid' , bg="#98AFC7") 
f1.place(x=10,y=50,width=400, height=390)

header = Label(f1, text="Enter The Data",bd=2,relief="solid",font=("bold", 15),fg="white",bg='black').place(x=0,y=0, width=400)

user = Label(f1, text="User ID:" , font=("bold", 15),fg="black", bg="#98AFC7").place(x=10,y=40)
userent= Entry(f1,relief=RIDGE,font=("bold", 15),textvariable=user_var)
userent.place(x=150, y=40, width=150)

name = Label(f1, text="Name :",font=("bold", 15),fg="black", bg="#98AFC7").place(x=10,y=90)

date = Label(f1, text="Date:",font=("bold", 15),fg="black", bg="#98AFC7").place(x=10,y=140)
date = DateEntry(f1,selectmode='day',textvariable=date_var).place(x=150,y=140)


quantity = Label(f1, text="Quantity:",font=("bold", 15),fg="black", bg="#98AFC7").place(x=10,y=190)
quantityent= Entry(f1,relief=RIDGE,font=("bold", 15),textvariable=quantity_var)
quantityent.place(x=150, y=190, width=100)


fat = Label(f1, text="Fat:",font=("bold", 15),fg="black", bg="#98AFC7").place(x=10,y=240)
fatent= Entry(f1,relief=RIDGE,font=("bold", 15),textvariable=fat_var)
fatent.place(x=150, y=240, width=100)
 

amount = Label(f1, text="Amount:",font=("bold", 15),fg="black", bg="#98AFC7").place(x=10,y=290)
amountent= Entry(f1,relief=RIDGE,font=("bold", 15),textvariable=amount_var)
amountent.place(x=150, y=290, width=100)



but2 = Button(f1, text ="Clear",command=clear ).place(x=10, y=340, width=100)
    
##===========create new seller==================================
def create_seller():
    a=(add_seller_var.get())
    b=(name_seller_var.get())
    
    db = mysql.connector.connect(host="localhost",user="root",password="admin",database="mms")
    cur=db.cursor()
    try:
            ab="CREATE TABLE " + add_seller_var.get() + """
                 (Date VARCHAR(10),Name CHAR(22) DEFAULT ' """+ name_seller_var.get() +""" ',
                 Quantity float,Fat float,Amount float)"""
            cur.execute(ab)
            db.commit()
            
           
            messagebox.showinfo('success','New seller is add successfully')
    except mysql.connector.errors.DatabaseError:
             messagebox.showerror('Warning','User is already exists')
    
    db = mysql.connector.connect(host="localhost",user="root",password="admin",database="mms")
    shu=db.cursor()
    b="Insert into  "+ a +""" (Name) values( '"""+ b +"""')"""
    shu.execute(b)
    db.commit()
    messagebox.showinfo('success','record is add successfully')
        
        

fs= Frame(milk,bd=2, relief='solid' , bg="#98AFC7")
fs.place(x=10,y=450,width=400, height=130)

h3 = Label(fs, text="Add New User",bd=2,relief="solid",font=("bold", 15),fg="white",bg='black').place(x=0,y=0, width=450)

cs = Label(fs, text="User ID:",font=("bold", 15),fg="black", bg="#98AFC7").place(x=10,y=40)
csent= Entry(fs,relief=RIDGE,font=("bold", 15),textvariable=add_seller_var).place(x=90, y=40, width=100)

ns = Label(fs, text="Name:",font=("bold", 15),fg="black", bg="#98AFC7").place(x=200,y=40)
nsent= Entry(fs,relief=RIDGE,font=("bold", 15),textvariable=name_seller_var).place(x=260, y=40, width=130)

buts = Button(fs, text ="ADD SELLER",font=("bold", 10),command=create_seller ).place(x=10, y=90, width=100)





##===========  show selected record to user  =================================
searchent_var = StringVar()
to_var=StringVar()
from_var=StringVar()
#============ it shows seller record and total of record from selected dates===================
def record():
    scroll_y= Scrollbar(f5,orient=VERTICAL)
    tree2= ttk.Treeview(f5,columns=(1,2,3,4),show ='headings',height=10,yscrollcommand=scroll_y.set)
    scroll_y.pack(side=RIGHT,fill=Y)
    tree2.heading(1,text="Date")
    tree2.heading(2,text="Quantity")
    tree2.heading(3,text="Fat")
    tree2.heading(4,text="Amount")

    tree2.column(1,width=100, anchor= CENTER)
    tree2.column(2,width=100, anchor= CENTER)
    tree2.column(3,width=100, anchor= CENTER)
    tree2.column(4,width=100, anchor= CENTER)

    tree2.place(x=10, y=130, width= 560,)
    
    tree3= ttk.Treeview(f5,columns=(1,2,3,4),show ='headings',height=1)
    tree3.heading(1,text="Total")
    tree3.heading(2,text="Quantity")
    tree3.heading(3,text="Fat")
    tree3.heading(4,text="Amount")
    tree3.column(1,width=100, anchor= CENTER)
    tree3.column(2,width=100, anchor= CENTER)
    tree3.column(3,width=100, anchor= CENTER)
    tree3.column(4,width=100, anchor= CENTER)

    tree3.place(x=10, y=410, width= 560,)
    
    db = mysql.connector.connect(host="localhost",user="root",password="admin",database="mms")
    cur=db.cursor()
    ab="(SELECT Date,Quantity,Fat,Amount FROM "+searchent_var.get()+ """ WHERE  date between '"""+ from_var.get() +"""' and '"""+ to_var.get() +"""')"""
    cur.execute(ab)
    rows = cur.fetchall()
    for row in rows:
            tree2.insert("",END, values=row)
    db.commit()
      
        
        #================ total of record ================

        
    man=db.cursor()
    tc="(SELECT count(Date),sum(Quantity),avg(Fat),sum(Amount) FROM "+searchent_var.get()+ """ WHERE  date between '"""+ from_var.get() +"""' and '"""+ to_var.get() +"""')"""
    man.execute(tc)
    i = man.fetchall()
    for a in i:
            tree3.insert("",END, values=a)
    db.commit()
    
    
    
                             




f5= Frame(milk,bd=2, relief='solid') 
f5.place(x=420,y=50,width=600, height=480)

h4 = Label(f5, text="Passbook",bd=2,relief="solid",font=("bold", 15),fg="white",bg='black').place(x=0,y=0, width=600)

fr= Frame(f5,bd=2, relief='solid',bg="#98AFC7") 
fr.place(x=0,y=30,width=596, height=90)

search = Label(fr, text="User ID:",font=("bold", 13),fg="black",bg="#98AFC7").place(x=3,y=5)
searchent= Entry(fr,relief=RIDGE,font=("bold", 13),textvariable=searchent_var).place(x=70, y=5, width=100)

               

               
form = Label(fr, text="From:",font=("bold", 13),fg="black",bg="#98AFC7").place(x=190,y=5)
form = DateEntry(fr,selectmode='day',textvariable=from_var).place(x=238,y=5)

to = Label(fr, text="TO:",font=("bold", 13),fg="black",bg="#98AFC7").place(x=350,y=5)
to = DateEntry(fr,selectmode='day',textvariable=to_var).place(x=380,y=5)

but4 = Button(fr, text ="Seller",font=("bold", 10),command=record).place(x=30, y=40, width=100)





h5 = Label(f5, text="Total",bd=2,relief="solid",font=("bold", 15),fg="white",bg='black').place(x=0,y=370, width=600)
    

#========= set focus ===========================
userent.focus()
def go1(event):
    
    try:

        db = mysql.connector.connect(host="localhost",user="root",password="admin",database="mms")
        man=db.cursor()
        tc="(SELECT default(Name) FROM "+ user_var.get() + """)"""
        man.execute(tc)
        i = man.fetchone()
        
        r_name.set(i[0])
        r=Entry(f1,relief=RIDGE,font=("bold", 15),textvariable=r_name).place(x=150,y=90)
        db.commit()
        
    except mysql.connector.errors.DatabaseError:
             messagebox.showerror('Warning','User is already exists')
    quantityent.focus_set()
    

userent.bind("<Return>",go1)
             

def go2(event):
             fatent.focus_set()

quantityent.bind("<Return>",go2)

def formula(event):
   try:
        a=float(quantityent.get())
        c=float(fatent.get())
        d=a*7*c
        e = float("{0:.2f}".format(d))
        amountent.insert(0,e)
   except:
        messagebox.showerror('Warning','enter the values')
   amountent.focus_set()

fatent.bind('<Return>',formula)


amountent.bind('<Return>',seller_data)

into = Label(milk, text="Shubham Singh Shekhawat(12101783)",bd=2,relief="solid",font=("bold", 20),fg="white",bg='black')
into.place(x=540,y=540)

milk.mainloop()
