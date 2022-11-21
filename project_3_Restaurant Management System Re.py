from tkinter import *
import datetime
import random
root=Tk()
root.title("Restaurant Manager")
root.geometry("1500x1100")
cdate=datetime.datetime.today().strftime("%D  %H-%M ")

l1=Label(root,font=("arial",70,"italic"),text="SAI RESTAURANT",bg="powderblue").pack()
date=Label(root,font=("arial",30,"italic"),bg="powderblue",text=cdate).place(x=370,y=150)
coffprice=StringVar()
teaprice=StringVar()
coldprice=StringVar()
juiceprice=StringVar()
ct=StringVar()
cgst1=StringVar()
sgst1=StringVar()
tc=StringVar()
var=StringVar()

def func():
    coff=coffprice.get()
    if(coff==" "):
        coffcost=0
    else:
        coffcost=30*int(coff)
        
    print(coffcost)
    
    tea=teaprice.get()
    
    
    if(tea==""):
        teacost=0
    else:
        teacost=10*int(tea)
        
    print(teacost)
    
    cold=coldprice.get()
    if(cold==""):
        coldcost=0
    else:
        coldcost=50*int(cold)
        
    print(coldcost)
    
    juice=juiceprice.get()
    if(juice==""):
        juicecost=0
    else:
        juicecost=50*int(juice)
        
    print(juicecost)
    
    
    random1=random.randint(1, 100)
    var1=str( random1)
    var.set(var1)
    
  

        
    
    total = teacost+coldcost+juicecost+coffcost
    print(total)
    ct.set(str(total))
    cgst=total*18/100
    cgst1.set(str(cgst))
    sgst=total*10/100
    sgst1.set(str(sgst))
    total2=total+cgst+sgst
    
    tc.set(str(total2))
#for exit of window
def destroy1():
    root.destroy() 
    
def res():
    coffprice.set("")
    teaprice.set("")
    coldprice.set("")
    juiceprice.set("")
    ct.set("")
    cgst1.set("")
    sgst1.set("")
    tc.set("")
    var.set("")
    
    
def text1():
    
   txtpayslip.insert(END,"Cost of meal\t\t"+ct.get()+"\n\n")
   txtpayslip.insert(END,"SGST:\t\t"+sgst1.get()+"\n\n")
   txtpayslip.insert(END,"CGST:\t\t"+cgst1.get()+"\n\n")
   txtpayslip.insert(END,"Total cost :\t\t"+tc.get())
   
   import sqlite3 as s
   conn=s.connect("info1.db")
   with conn:
       cursor=conn.cursor()
       cursor.execute("create table if not exists customer(cost_of_meal text,sgst text,cgst text,totalcost text)")
       cursor.execute("insert into customer(cost_of_meal,sgst,cgst,totalcost)values(?,?,?,?)",(ct.get(),sgst1.get(),cgst1.get(),tc.get()))
   conn.commit()
   

   
   
        
#menu
coffee=Label(root,font=("arial",20,"bold"),fg="black",text="Coffee",bg="green",width=10,height=1,bd=6,padx=4).place(x=30,y=250)
coffe_Entry=Entry(root,font=("arial",20,"bold"),fg="black",width=15,bd=6,text=coffprice).place(x=250,y=250)

Tea=Label(root,font=("arial",20,"bold"),fg="black",text="Tea",bg="green",width=10,height=1,bd=6,padx=4).place(x=30,y=350)
Tea_Entry=Entry(root,font=("arial",20,"bold"),fg="black",width=15,bd=6,text=teaprice).place(x=250,y=350)


cold_drink=Label(root,font=("arial",20,"bold"),fg="black",text="Cold drink",bg="green",width=10,height=1,bd=6,padx=4).place(x=30,y=450)
cold_entry=Entry(root,font=("arial",20,"bold"),fg="black",width=15,bd=6,text=coldprice).place(x=250,y=450)


Juices=Label(root,font=("arial",20,"bold"),fg="black",text="Juices",bg="green",width=10,height=1,bd=6,padx=4).place(x=30,y=550)
Juices_entry=Entry(root,font=("arial",20,"bold"),fg="black",width=15,bd=6,text=juiceprice).place(x=250,y=550)

#Top line
Reference=Label(root,font=("arial",20,"bold"),fg="black",text="Reference",bg="green",width=10,height=1,bd=6,padx=4).place(x=550,y=250)
Ref_Entry=Entry(root,font=("arial",20,"bold"),fg="black",width=15,bd=6,text=var).place(x=770,y=250)

Cost_of_meal=Label(root,font=("arial",20,"bold"),fg="black",text="Cost of Meal",bg="green",width=10,height=1,bd=6,padx=4).place(x=550,y=350)
cost_Entry=Entry(root,font=("arial",20,"bold"),fg="black",width=15,bd=6,text=ct).place(x=770,y=350)


sgst=Label(root,font=("arial",20,"bold"),fg="black",text="SGST",bg="green",width=10,height=1,bd=6,padx=4).place(x=550,y=450)
sgst_Entry=Entry(root,font=("arial",20,"bold"),fg="black",width=15,bd=6,text=sgst1).place(x=770,y=450)

cgst=Label(root,font=("arial",20,"bold"),fg="black",text="CGST",bg="green",width=10,height=1,bd=6,padx=4).place(x=550,y=550)
cgst_Entry=Entry(root,font=("arial",20,"bold"),fg="black",width=15,bd=6,text=cgst1).place(x=770,y=550)

Total=Label(root,font=("arial",20,"bold"),fg="black",text="TOTAL COST",bg="green",width=10,height=1,bd=6,padx=4).place(x=830,y=650)
total_Entry=Entry(root,font=("arial",20,"bold"),fg="black",width=15,bd=6,text=tc).place(x=1050,y=650)

#Print area

txtpayslip=Text(root,font=("arial",20,"bold"),height=12,width=34)
txtpayslip.place(x=1020,y=230)
l=Label(root,font=("arial",30,"bold"),width=15,text="PAYSLIP").place(x=1020,y=180)




#buttons
btnttl=Button(root,font=('arial',25,'bold'),text="TOTAL",bd=10,padx=30,bg="orange",fg="blue",command=func).place(x=5,y=620)
btn_reset=Button(root,font=('arial',25,'bold'),text="RESET",bd=10,padx=30,bg="orange",fg="blue",command=res).place(x=200,y=620)
btn_exit=Button(root,font=('arial',25,'bold'),text="EXIT",bd=10,padx=30,bg="orange",fg="blue",command=destroy1,width=6).place(x=410,y=620)
btn_print=Button(root,font=('arial',25,'bold'),text="PRINT SLIP",bd=10,padx=30,bg="orange",fg="blue",command=text1,width=6).place(x=610,y=620)


root.mainloop()