from time import strftime
from tkinter import *
from datetime import datetime
from PIL import Image,ImageTk
from customer import customerClass
from category import categoryClass
from brand import brandClass
from product import productClass
from billing import billingClass
from finalbill import finalbill
import mysql.connector as c
from tkinter import ttk,messagebox

class IMS:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1350x700+0+0")
        self.root.title("Clothing Billing System")
        self.root.config(bg="white")

        #======functions===================
        def time():

                    string = strftime("%d/%m/%Y %H:%M:%S")
                    lbl.config(text = string)
                    lbl.after(1000, time)
                    
        lbl=Label(self.root,text=" Welcome to Bill Management System ", font = ("arial",16,"bold"),background = "#4d636d", foreground="white")
        lbl.place(x=0,y=70,relwidth=1,height=30)

        #===title===
        title=Label(self.root,text="Bill Management System",font=("times new roman",40,"bold"),bg="#010c48",fg="white",anchor="w",padx=20).place(x=0,y=0,relwidth=1,height=70)
        #===btn_logout===
        btn_logout=Button(self.root,text="Logout",font=("times new roman",15,"bold"),bg="yellow",cursor="hand2").place(x=1150,y=10,height=50,width=150)
        
        time()  

        #=======LeftMenu=======
        LeftMenu=Frame(self.root,bd=2,relief=RIDGE,bg="white").place(x=0,y=102,width=300,height=565)
        self.MenuLogo=Image.open("img4.jpg")
        self.MenuLogo=self.MenuLogo.resize((200,200),Image.Resampling.LANCZOS)
        self.MenuLogo=ImageTk.PhotoImage(self.MenuLogo)
        lbl_menuLogo=Label(LeftMenu,image=self.MenuLogo).place(x=0,y=104,width=300,height=300)
        btn_menu=Label(LeftMenu,text="Menu",font=("times new roman",15,"bold"),bg="#4d636d").place(x=0,y=404,width=300,height=50)
        btn_customer=Button(LeftMenu,text="Customer",command=self.customer,font=("times new roman",15,"bold"),bg="white",cursor="hand2").place(x=0,y=454,width=300,height=50)
        btn_category=Button(LeftMenu,text="Category",command=self.category,font=("times new roman",15,"bold"),bg="white",cursor="hand2").place(x=0,y=504,width=300,height=50)
        btn_brand=Button(LeftMenu,text="Brand",command=self.brand,font=("times new roman",15,"bold"),bg="white",cursor="hand2").place(x=0,y=554,width=300,height=50)
        btn_product=Button(LeftMenu,text="Product",command=self.product,font=("times new roman",15,"bold"),bg="white",cursor="hand2").place(x=0,y=604,width=300,height=50)
        btn_bill=Button(LeftMenu,text="Bill",command=self.finalbill,font=("times new roman",15,"bold"),bg="white",cursor="hand2").place(x=0,y=654,width=300,height=50)
        
        #========Contents==========
        self.lbl_customer=Label(self.root,text="Total Customer \n[ 0 ]",bd=5,relief=RIDGE,bg="white",font=("times new roman",25,"bold"))
        self.lbl_customer.place(x=400,y=120,height=150,width=300)
        self.lblcategory=Label(self.root,text="Total Category \n[ 0 ]",bd=5,relief=RIDGE,bg="white",font=("times new roman",25,"bold"))
        self.lblcategory.place(x=800,y=120,height=150,width=300)
        self.lbl_product=Label(self.root,text="Total Product \n[ 0 ]",bd=5,relief=RIDGE,bg="white",font=("times new roman",25,"bold"))
        self.lbl_product.place(x=400,y=360,height=150,width=300)
        self.lbl_bill=Label(self.root,text="Total Brand \n[ 0 ]",bd=5,relief=RIDGE,bg="white",font=("times new roman",25,"bold"))
        self.lbl_bill.place(x=800,y=360,height=150,width=300)
        
        #=========footer===========
        lbl_footer=Label(self.root,text=" \n Bill Management System \n    \n All rights are reserved ",font=("times new roman",15,"bold"),bd=2,relief=RIDGE,bg="#4d636d").pack(side=BOTTOM,fill=X)
        self.count_customer()
        self.count_product()
        self.count_category()
        self.count_brand()
        #==============================================================
    def customer(self):
        self.new_win=Toplevel(self.root)
        self.new_obj=customerClass(self.new_win)
    def category(self):
        self.new_win=Toplevel(self.root)
        self.new_obj=categoryClass(self.new_win)
    def brand(self):
        self.new_win=Toplevel(self.root)
        self.new_obj=brandClass(self.new_win)
    def product(self):
        self.new_win=Toplevel(self.root)
        self.new_obj=productClass(self.new_win)   
    def billing(self):
        self.new_win=Toplevel(self.root)
        self.new_obj=billingClass(self.new_win)          
    def finalbill(self):
        self.new_win=Toplevel(self.root)
        self.new_obj=finalbill(self.new_win)          

    def count_customer(self):
        con=c.connect(host="localhost",username="root",password="unnati@15",database="ty")         
        cursor=con.cursor()
        try:
            cursor.execute("select * from Customer")
            rows=cursor.fetchall()
            self.lbl_customer.config(text=f'Total Customer\n[{str(len(rows))}]')
        except Exception as ex:
                messagebox.showerror("Error",f"Error due to : {str(ex)}",parent=self.root)

    def count_product(self):
        con=c.connect(host="localhost",username="root",password="unnati@15",database="ty")         
        cursor=con.cursor()
        try:
            cursor.execute("select * from Product")
            rows=cursor.fetchall()
            self.lbl_product.config(text=f'Total Product\n[{str(len(rows))}]')
        except Exception as ex:
                messagebox.showerror("Error",f"Error due to : {str(ex)}",parent=self.root)

    def count_category(self):
        con=c.connect(host="localhost",username="root",password="unnati@15",database="ty")         
        cursor=con.cursor()
        try:
            cursor.execute("select * from Category")
            rows=cursor.fetchall()
            self.lblcategory.config(text=f'Total Category\n[{str(len(rows))}]')
        except Exception as ex:
                messagebox.showerror("Error",f"Error due to : {str(ex)}",parent=self.root)

    def count_brand(self):
        con=c.connect(host="localhost",username="root",password="unnati@15",database="ty")         
        cursor=con.cursor()
        try:
            cursor.execute("select * from Brand")
            rows=cursor.fetchall()
            self.lbl_bill.config(text=f'Total Brand\n[{str(len(rows))}]')
        except Exception as ex:
                messagebox.showerror("Error",f"Error due to : {str(ex)}",parent=self.root)


if __name__=='__main__':
       root=Tk()
       obj=IMS(root)
       root.mainloop()
