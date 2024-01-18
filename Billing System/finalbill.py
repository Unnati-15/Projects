from time import strftime
from tkinter import *
from tkinter import ttk,messagebox
from billing import billingClass
import mysql.connector as c
import time
import os
import tempfile


class finalbill:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1350x700+0+0")
        self.root.title("Clothing Billing System")
        self.root.config(bg="white")
        self.cart_list=[]
        self.chk_print=0

        self.var_cust_id=IntVar()
        self.var_cust_name=StringVar()
        self.var_cust_email=StringVar()
        self.var_cust_mobile=StringVar()
        self.var_cust_dob=StringVar()
        self.var_cust_addr=StringVar()
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
        btn_logout=Button(self.root,text="Search Bill",font=("times new roman",15,"bold"),command=self.billing,bg="yellow",cursor="hand2").place(x=1150,y=10,height=50,width=150)
        
        time()  

        #=====Product Frame=====

        ProductFrame1=Frame(self.root,bd=4,relief=RIDGE, bg="white")
        ProductFrame1.place(x=6,y=110,width=410,height=550)

        pTitle=Label(ProductFrame1,text="All Products",font=("goudy old style",20,"bold"),bg="#262626",fg="white").pack(side=TOP,fill=X)
        #=====Product Search Frame=====

        self.var_search=StringVar()
        self.var_searchtxt1=StringVar()
        ProductFrame2=Frame(ProductFrame1,bd=2,relief=RIDGE,bg="white")
        ProductFrame2.place(x=2,y=42,width=398,height=90)

        lbl_search=Label(ProductFrame2,text="Search Product | By Id",font=("times new roman",15,"bold"),bg="white",fg="green").place(x=2,y=5)

        cmb_search=ttk.Combobox(ProductFrame2,textvariable=self.var_search,values=("Select","pid","pname"),state='readonly',justify=CENTER,font=("times new roman",15,"bold"))
        cmb_search.place(x=105,y=47,width=150,height=22)
        cmb_search.current(0)

        
        lbl_search=Label(ProductFrame2,text="Product Id",font=("times new roman",15,"bold"),bg="white").place(x=2,y=45)
        txt_search=Entry(ProductFrame2,textvariable=self.var_searchtxt1,font=("times new roman",15,"bold"),bg="lightyellow").place(x=200,y=10)
        btn_search=Button(ProductFrame2,text="Search",command=self.search,font=("goudy old style",15),bg="#2196f3",fg="white",cursor="hand2").place(x=258,y=45,width=100,height=25)
        
        
        ProductFrame3=Frame(ProductFrame1,bd=3,relief=RIDGE)
        ProductFrame3.place(x=2,y=140,width=398,height=375)

        scrolly=Scrollbar(ProductFrame3,orient=VERTICAL)
        scrollx=Scrollbar(ProductFrame3,orient=HORIZONTAL)

        self.product_Table=ttk.Treeview(ProductFrame3,columns=("pid","name","price","qty","status"),yscrollcommand=scrolly.set,xscrollcommand=scrollx.set)
        scrollx.pack(side=BOTTOM,fill=X)
        scrolly.pack(side=RIGHT,fill=Y)
        scrollx.config(command=self.product_Table.xview)
        scrolly.config(command=self.product_Table.yview)
        self.product_Table.heading("pid",text="PID")
        self.product_Table.heading("name",text="Name")
        self.product_Table.heading("price",text="Price")
        self.product_Table.heading("qty",text="Quantity")
        self.product_Table.heading("status",text="Status")
        self.product_Table["show"]="headings"
        self.product_Table.column("pid",width=40)
        self.product_Table.column("name",width=100)
        self.product_Table.column("price",width=100)
        self.product_Table.column("qty",width=68)
        self.product_Table.column("status",width=70)
        self.product_Table.pack(fill=BOTH,expand=1)
        self.product_Table.bind("<ButtonRelease-1>",self.get_data)
        
        lbl_note=Label(ProductFrame1,text="Note: 'Enter 0 Quantity to remove product from the cart' ", font=("goudy old style",12)  ,bg="white",fg="red",).pack(side=BOTTOM,fill=X)

        #=====Customer Frame=====
        self.var_searchtxt=StringVar()
        self.var_searchby=StringVar()
        CustomerFrame=Frame(self.root,bd=4,relief=RIDGE,bg="white")
        CustomerFrame.place(x=420,y=110,width=530,height=70)

        cTitle=Label(CustomerFrame,text="Customer Details",font=("goudy old style",15),bg="lightgray").pack(side=TOP,fill=X)

        lbl_search=Label(CustomerFrame,text="Contact",font=("times new roman",15,"bold"),bg="white").place(x=2,y=35)
        cmb_search=ttk.Combobox(CustomerFrame,textvariable=self.var_searchby,values=("Select","mobno"),state='readonly',justify=CENTER,font=("times new roman",15,"bold"))
        cmb_search.place(x=100,y=35,width=80)
        cmb_search.current(0)
        txt_search=Entry(CustomerFrame,textvariable=self.var_searchtxt,font=("times new roman",15,"bold"),bg="lightyellow").place(x=180,y=35)
        btn_search=Button(CustomerFrame,text="Search By",command=self.search_cust,font=("times new roman",15,"bold"),bg="#4caf50",fg="white",cursor="hand2").place(x=400,y=35,width=100,height=25)



        Cal_Cart_Frame=Frame(self.root, bd=2, relief=RIDGE, bg="white")
        Cal_Cart_Frame.place(x=420,y=190,width=530,height=360)

         #=====Customer Frame=====

        customer_Frame=Frame(self.root,bd=3,relief=RIDGE)
        customer_Frame.place(x=420,y=210,width=530,height=160)
        self.customerTitle=Label(customer_Frame,text="Customer Details:",font=("goudy old style",18),bg="lightgray")
        self.customerTitle.pack(side=TOP,fill=X)


        scrolly=Scrollbar(customer_Frame,orient=VERTICAL)
        scrollx=Scrollbar(customer_Frame,orient=HORIZONTAL)

        self.CustomerTable=ttk.Treeview(customer_Frame,columns=("id","name","email","mobno","dob","addr"),yscrollcommand=scrolly.set,xscrollcommand=scrollx.set)
        scrollx.pack(side=BOTTOM,fill=X)
        scrolly.pack(side=RIGHT,fill=Y)
        scrollx.config(command=self.CustomerTable.xview)
        scrolly.config(command=self.CustomerTable.yview)
        self.CustomerTable.heading("id",text="Cust Id")
        self.CustomerTable.heading("name",text="Cust Name")
        self.CustomerTable.heading("email",text="Email")
        self.CustomerTable.heading("mobno",text="Mobno")
        self.CustomerTable.heading("dob",text="DOB")
        self.CustomerTable.heading("addr",text="Address")
        self.CustomerTable["show"]="headings"
        self.CustomerTable.column("id",width=90)
        self.CustomerTable.column("name",width=100)
        self.CustomerTable.column("email",width=100)
        self.CustomerTable.column("mobno",width=100)
        self.CustomerTable.column("dob",width=100)
        self.CustomerTable.column("addr",width=100)

        self.CustomerTable.pack(fill=BOTH,expand=1)
        self.CustomerTable.bind("<ButtonRelease-1>",self.get_data_cust)
        self.show_cust()
        
        #=====Cart Frame=====

        cart_Frame=Frame(self.root,bd=3,relief=RIDGE)
        cart_Frame.place(x=420,y=390,width=530,height=160)
        self.cartTitle=Label(cart_Frame,text="Cart Total Product:",font=("goudy old style",18),bg="lightgray")
        self.cartTitle.pack(side=TOP,fill=X)


        scrolly=Scrollbar(cart_Frame,orient=VERTICAL)
        scrollx=Scrollbar(cart_Frame,orient=HORIZONTAL)

        self.CartTable=ttk.Treeview(cart_Frame,columns=("pid","name","price","qty"),yscrollcommand=scrolly.set,xscrollcommand=scrollx.set)
        scrollx.pack(side=BOTTOM,fill=X)
        scrolly.pack(side=RIGHT,fill=Y)
        scrollx.config(command=self.CartTable.xview)
        scrolly.config(command=self.CartTable.yview)
        self.CartTable.heading("pid",text="PID")
        self.CartTable.heading("name",text="Name")
        self.CartTable.heading("price",text="Price")
        self.CartTable.heading("qty",text="Quantity")
        self.CartTable["show"]="headings"
        self.CartTable.column("pid",width=40)
        self.CartTable.column("name",width=90)
        self.CartTable.column("price",width=90)
        self.CartTable.column("qty",width=60)
        self.CartTable.pack(fill=BOTH,expand=1)
        self.CartTable.bind("<ButtonRelease-1>",self.get_data_cart)

        #=====ADD Cart Widgets Frame=====

        self.var_pid=StringVar()
        self.var_pname=StringVar()
        self.var_price=StringVar()
        self.var_qty=StringVar()
        self.var_stock=StringVar()

        Add_CartWidgetsFrame=Frame(self.root,bd=2,relief=RIDGE,bg="white")
        Add_CartWidgetsFrame.place (x=420,y=550,width=530,height=110)

        lbl_p_name=Label(Add_CartWidgetsFrame,text="Product Name",font=("times new roman",15),bg="white").place(x=5,y=5)
        txt_p_name=Entry(Add_CartWidgetsFrame,textvariable=self.var_pname,font=("times new roman",15),bg="lightyellow",state='readonly').place(x=5,y=35,width=190,height=22)

        lbl_p_price=Label(Add_CartWidgetsFrame,text="Price Per Qty",font=("times new roman",15),bg="white").place(x=230,y=5)
        txt_p_price=Entry(Add_CartWidgetsFrame,textvariable=self.var_price,font=("times new roman",15),bg="lightyellow",state='readonly').place(x=230,y=35,width=150,height=22)

        lbl_p_qty=Label(Add_CartWidgetsFrame,text="Quantity",font=("times new roman",15),bg="white").place(x=390,y=5)
        txt_p_qty=Entry(Add_CartWidgetsFrame,textvariable=self.var_qty,font=("times new roman",15),bg="lightyellow").place(x=390,y=35,width=120,height=22)

        self.lbl_inStock=Label(Add_CartWidgetsFrame,text="In Stock",font=("times new roman",15),bg="white")
        self.lbl_inStock.place(x=5,y=70)

        btn_clear_cart=Button(Add_CartWidgetsFrame,text="Clear",command=self.clear_cart,font=("times new roman",15,"bold"),bg="crimson",cursor="hand2").place(x=180,y=70,width=150,height=30)
        btn_add_cart=Button(Add_CartWidgetsFrame,text="Add | Update Cart",command=self.add_update_cart,font=("times new roman",15,"bold"),bg="#4caf50",cursor="hand2").place(x=340,y=70,width=180,height=30)

        #=====Billing Area=====

        billFrame=Frame(self.root,bd=2,relief=RIDGE,bg="white")
        billFrame.place(x=953,y=110,width=480,height=410)

        BTitle=Label(billFrame,text="Customer Bill",font=("goudy old style",20,"bold"),bg="#262626",fg="white").pack(side=TOP,fill=X)
        scrolly=Scrollbar(billFrame,orient=VERTICAL)
        scrolly.pack(side=RIGHT,fill=Y)

        self.txt_bill_area=Text(billFrame,yscrollcommand=scrolly.set)
        self.txt_bill_area.pack(fill=BOTH,expand=1)
        scrolly.config(command=self.txt_bill_area.yview)

        #=====Billing Buttons=====

        billMenuFrame=Frame(self.root,bd=2,relief=RIDGE,bg='white') 
        billMenuFrame.place(x=953,y=520,width=480,height=140)

        self.lbl_amnt=Label(billMenuFrame,text='Bill Amount\n[0]',font=("goudy old style",15,"bold"),bg="#3f51b5",fg="white")
        self.lbl_amnt.place(x=2,y=5,width=150,height=70)

        self.lbl_discount=Label(billMenuFrame,text='Discount\n[5%]',font=("goudy old style",15,"bold"),bg="#8bc34a",fg="white")
        self.lbl_discount.place(x=154,y=5,width=150,height=70)

        self.lbl_net_pay=Label(billMenuFrame,text='Net Pay\n[0]',font=("goudy old style",15,"bold"),bg="#6e7d8b",fg="white")
        self.lbl_net_pay.place(x=306,y=5,width=165,height=70)

        btn_print=Button(billMenuFrame,text='Print',command=self.print_bill,cursor='hand2',font=("goudy old style",15,"bold"),bg="lightgreen",fg="white")
        btn_print.place(x=2,y=80,width=150,height=50)

        btn_clear_all=Button(billMenuFrame,text='Clear All',command=self.clear_all,cursor='hand2',font=("goudy old style",15,"bold"),bg="gray",fg="white")
        btn_clear_all.place(x=154,y=80,width=150,height=50)

        btn_generate=Button(billMenuFrame,text='Generate/Save Bill',command=self.generate_bill,cursor='hand2',font=("goudy old style",15,"bold"),bg="#009689",fg="white")
        btn_generate.place(x=306,y=80,width=165,height=50)

        #=====Footer=====
        footer=Label(self.root,text="Billing System || Developed By Students of BBA CA\n For any Technical Issue Contact: +917757997489",font=("times new roman",11),bg="#4d636d",fg="white",bd=0).pack(side=BOTTOM,fill=X)

        self.show()
        #self.bill_top()
        #=====All Functions=====

    def show(self):
        con=c.connect(host="localhost",username="root",password="unnati@15",database="ty")         
        cursor=con.cursor()
        try:
            cursor.execute("select pid,pname,price,qty,status from Product where status='Active'")
            rows=cursor.fetchall()
            self.product_Table.delete(*self.product_Table.get_children())
            for row in rows:
                self.product_Table.insert('',END,values=row)
        except Exception as ex:
                messagebox.showerror("Error",f"Error due to : {str(ex)}",parent=self.root)

    def show_cust(self):
        con=c.connect(host="localhost",username="root",password="unnati@15",database="ty")         
        cursor=con.cursor()
        try:
            cursor.execute("select * from Customer")
            rows=cursor.fetchall()
            self.CustomerTable.delete(*self.CustomerTable.get_children())
            for row in rows:
                self.CustomerTable.insert('',END,values=row)
        except Exception as ex:
                messagebox.showerror("Error",f"Error due to : {str(ex)}",parent=self.root)

    def search_cust(self):
        con=c.connect(host="localhost",username="root",password="unnati@15",database="ty")         
        cursor=con.cursor()
        try:
            if self.var_searchby.get()=="Select":
                messagebox.showerror("Error","Select Search by option",parent=self.root)
            elif self.var_searchtxt.get()=="":   
                messagebox.showerror("Error","Search input should be required",parent=self.root)
            else:
                cursor.execute("select * from Customer where " + self.var_searchby.get() + "=" +self.var_searchtxt.get() + "")
                rows=cursor.fetchall()
                if  len(rows)!=0:
                    self.CustomerTable.delete(*self.CustomerTable.get_children())
                    for row in rows:
                        self.CustomerTable.insert('',END,values=row)
                else:
                    messagebox.showerror("Error","Not found")
          
        except Exception as ex:
                messagebox.showerror("Error",f"Error due to : {str(ex)}",parent=self.root)
          

    def search(self):
        con=c.connect(host="localhost",username="root",password="unnati@15",database="ty")         
        cursor=con.cursor()
        try:
            if self.var_search.get()=="Select":
                messagebox.showerror("Error","Select Search by option",parent=self.root)
            elif self.var_searchtxt1.get()=="":   
                messagebox.showerror("Error","Search input should be required",parent=self.root)
            else:
                cursor.execute("select * from Product where " + self.var_search.get() + "=" +self.var_searchtxt1.get() + "")
                rows=cursor.fetchall()
                if  len(rows)!=0:
                    self.product_Table.delete(*self.product_Table.get_children())
                    for row in rows:
                        self.product_Table.insert('',END,values=row)
                else:
                    messagebox.showerror("Error","Not found")
          
        except Exception as ex:
                messagebox.showerror("Error",f"Error due to : {str(ex)}",parent=self.root)
     

    def get_data(self,ev):
        f=self.product_Table.focus()
        content=(self.product_Table.item(f))
        row=content['values']
        self.var_pid.set(row[0])
        self.var_pname.set(row[1])
        self.var_price.set(row[2])
        self.lbl_inStock.config(text=f"In Stock [{str(row[3])}]")
        self.var_stock.set(row[3])
        self.var_qty.set('1')

    def get_data_cust(self,ev):
        f=self.CustomerTable.focus()
        content=(self.CustomerTable.item(f))
        row=content['values']
        #print(row)
        self.var_cust_id.set(row[0])
        self.var_cust_name.set(row[1])
        self.var_cust_email.set(row[2])
        self.var_cust_mobile.set(row[3])
        self.var_cust_dob.set(row[4])
        self.var_cust_addr.set(row[5])

    def get_data_cart(self,ev):
        f=self.CartTable.focus()
        content=(self.CartTable.item(f))
        row=content['values']
        self.var_pid.set(row[0])
        self.var_pname.set(row[1])
        self.var_price.set(row[2])
        self.var_qty.set('1')
        self.lbl_inStock.config(text=f"In Stock [{str(row[3])}]")
        self.var_stock.set(row[3])
        


    def add_update_cart(self):
            if self.var_pid.get()=='':
                messagebox. showerror ('Error', "Please select product from the list",parent=self.root)          
            elif self.var_qty.get()=='':
                messagebox.showerror('Error',"Quantity is Required",parent=self.root)
            elif int(self.var_qty. get())>int(self.var_stock.get()):
                messagebox.showerror('Error',"Invalid Quantity",parent=self.root)
            else:
                #price_cal=(int(self.var_qty.get())*float(self.var_price.get()))    
                #price_cal=float(price_cal)
                price_cal=self.var_price.get()
                cart_data=[self.var_pid.get(),self.var_pname.get(),price_cal,self.var_qty.get(),self.var_stock.get()]
                
               
               

        #=====Update Cart=====
            present='no'
            index_=0
            for row in self.cart_list:
                 if self.var_pid.get()==row[0]:
                      present='yes'
                      break
                 index_+1

            if present=='yes':
                op=messagebox.askyesno('Confirm',"Product already present\n Do you want to Update|Remove from the Cart List",parent=self.root)
                if op==True:
                    if self.var_qty.get()=="0":
                      self.cart_list.pop(index_)
                    else:
                      #self.cart_list[index_][2]=price_cal
                      self.cart_list[index_][3]=self.var_qty.get()
                      
            else:
                self.cart_list.append(cart_data)
            self.show_cart()
            self.bill_updates()

    def bill_updates(self):
         self.bill_amt=0
         self.net_pay=0
         self.discount=0
         for row in self.cart_list:
              self.bill_amt=self.bill_amt+(float(row[2])*int(row[3]))
              
              self.discount=(self.bill_amt*5)/100
              self.net_pay=self.bill_amt-self.discount
              self.lbl_amnt.config(text=f'Bill Amount\n{str(self.bill_amt)}')
              self.lbl_net_pay.config(text=f'Net Pay\n{str(self.net_pay)}')
              self.cartTitle.config(text=f"Cart Total Product: [{str(len(self.cart_list))}]")


    def show_cart(self):
        try:
            self.CartTable.delete(*self.CartTable.get_children())
            for row in self.cart_list:
                 self.CartTable.insert('',END,values=row)
        except Exception as ex:
             messagebox.showerror("Error",f"Error due to: {str(ex)}",parent=self.root)


    def generate_bill(self):
         if len(self.cart_list)==0:
            messagebox. showerror ("Error", f"please Add product to the cart!", parent=-self.root)
         else:
              #=====Bil Top=====
              self.bill_top()
              #=====Bill Middle=====
              self.bill_middle()
              #=====Bill Bottom=====
              self.bill_bottom()
              
              fp=open(f'bill/{str(self.invoice)}.txt','w')
              fp.write(self.txt_bill_area.get('1.0',END))
              fp.close()
              messagebox.showinfo('saved',"Bill has been generated/saved in Backend",parent=self.root)
              self.chk_print=1
         
    def bill_top(self):
        self.invoice=int(time.strftime("%H%M%S"))+int(time.strftime ("%d%m%Y"))
        bill_top_temp=f'''
                \t\tBilling System
                It Phone No. +917757997489
                ,Pune-411057
{str ("="*64)}
 Ph no. :{self.var_searchtxt.get ()}
 Bill No. {str(self.invoice)}\t\t\tDate: {str(time.strftime("%d/%m/%Y"))}
{str ("="*64)}
 Product Name\t\t\tQTY\tPrice
{str("="*64)} 
            '''
        self.txt_bill_area.delete('1.0',END)
        self.txt_bill_area.insert('1.0',bill_top_temp)


    def bill_bottom(self):
        bill_bottom_temp=f'''
{str("="*64)}
 Bill Amount\t\t\t\tRs.{self.bill_amt}
 Discount\t\t\t\tRs.{self.discount}
 Net Pay\t\t\t\tRs.{self.net_pay} 
{str("="*64)}\n
            '''
        self.txt_bill_area.insert(END,bill_bottom_temp)


    def bill_middle(self):
        con=c.connect(host="localhost",username="root",password="unnati@15",database="ty")         
        cursor=con.cursor()
        try:
            
            for row in self.cart_list:
                 
                pid=row[0]
                name=row[1]
                qty=int(row[4])-int(row[3]) 
            if int(row[3])==int(row[4]):
                status='Inactive' 
            if int(row[3])!=int(row[4]):
                status='Active'

            price=float(row[2])*int(row[3])
            price=str(price)
            self.txt_bill_area.insert(END,"\n "+name+"It\t\t"+row[3]+"\tRs."+price)
             #=====U   pdate Product Table=====
            cursor.execute("Update Product set qty={},status='{}'where pid={}",(
                qty,
                status,
                pid

             ))
            con.commit()
            con.close()
            self.show()

        except Exception as ex:
            messagebox.showerror("Error",f"Error due to : {str(ex)}",parent=self.root)

    def clear_cart(self):
         self.var_pid.set('')
         self.var_pname.set('')
         self.var_price.set('')
         self.var_qty.set('')
         self.lbl_inStock.config(text=f"In Stock")
         self.var_stock.set('')


    def clear_all (self):
        del self.cart_list[:]
        self.var_searchby.set ('') 
        self.var_searchtxt.set('')
        self.txt_bill_area.delete('1.0',END)
        self.cartTitle.config(text=f"Cart \t Total Product: [0]")
        self.var_search.set('')
        self.clear_cart()
        self.show()
        self.show_cart()

    def print_bill(self):
        if self.chk_print==1:
            messagebox.showinfo('print',"Please wait while printing",parent=self.root)
            new_file=tempfile.mktemp('.txt')
            open(new_file,'w').write(self.txt_bill_area.get('1.0',END))
            os.startfile(new_file,'print')
        else:
            messagebox.showerror('print',"Please generate bill",parent=self.root)
            
    def billing(self):
        self.new_win=Toplevel(self.root)
        self.new_obj=billingClass(self.new_win)  


if __name__=='__main__':
       root=Tk()
       obj=finalbill(root)
       root.mainloop()