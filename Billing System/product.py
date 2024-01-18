from time import strftime
from tkinter import *
from PIL import Image,ImageTk
from tkinter import ttk,messagebox
import mysql.connector as c

class productClass:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1100x500+220+130")
        self.root.resizable(False, False)
        self.root.title("Clothing Billing System")
        self.root.config(bg="white")
        self.root.focus_force()

        #=========================
        
        product_frame=Frame(self.root,bd=3,relief=RIDGE)
        product_frame.place(x=10,y=10,width=450,height=480)

        # all variables==============
        self.var_searchby=StringVar()
        self.var_searchtxt=StringVar()

        
        self.var_prod_id=IntVar()
        self.var_cat=StringVar()
        self.var_brand=StringVar()
        self.cat_list=[]
        self.brand_list=[]
        
        self.fetch_cat_brand()
        self.var_prod_name=StringVar()
        self.var_price=IntVar()
        self.var_qty=IntVar()
        self.var_status=StringVar()

        #===title===
        title=Label(product_frame,text="Product Details",font=("times new roman",15,"bold"),bg="#0f4d7d",fg="white").pack(side=TOP,fill=X)

        #=========contents===========
        
        lbl_prod_id=Label(product_frame,text="Product Id",font=("times new roman",15,"bold"),bg="white").place(x=30,y=60)
        lbl_category=Label(product_frame,text="Category",font=("times new roman",15,"bold"),bg="white").place(x=30,y=110)
        lbl_brand=Label(product_frame,text="Brand",font=("times new roman",15,"bold"),bg="white").place(x=30,y=160)
        lbl_prod_name=Label(product_frame,text="Name",font=("times new roman",15,"bold"),bg="white").place(x=30,y=210)
        lbl_price=Label(product_frame,text="Price",font=("times new roman",15,"bold"),bg="white").place(x=30,y=260)
        lbl_qty=Label(product_frame,text="Quantity",font=("times new roman",15,"bold"),bg="white").place(x=30,y=310)
        lbl_status=Label(product_frame,text="Status",font=("times new roman",15,"bold"),bg="white").place(x=30,y=360)
        
         #===============options==========
         
        txt_prod_id=Entry(product_frame,textvariable=self.var_prod_id,font=("times new roman",15,"bold"),bg="white").place(x=150,y=60,width=200)
        cmb_cat=ttk.Combobox(product_frame,textvariable=self.var_cat,values=self.cat_list,state='readonly',justify=CENTER,font=("times new roman",15,"bold"))
        cmb_cat.place(x=150,y=110,width=200)
        cmb_cat.current(0)
        cmb_brand=ttk.Combobox(product_frame,textvariable=self.var_brand,values=self.brand_list,state='readonly',justify=CENTER,font=("times new roman",15,"bold"))
        cmb_brand.place(x=150,y=160,width=200)
        cmb_brand.current(0)

        txt_prod_name=Entry(product_frame,textvariable=self.var_prod_name,font=("times new roman",15,"bold"),bg="white").place(x=150,y=210,width=200)
        txt_price=Entry(product_frame,textvariable=self.var_price,font=("times new roman",15,"bold"),bg="white").place(x=150,y=260,width=200)
        txt_qty=Entry(product_frame,textvariable=self.var_qty,font=("times new roman",15,"bold"),bg="white").place(x=150,y=310,width=200)
       
        cmb_status=ttk.Combobox(product_frame,textvariable=self.var_status,values=("Active","Inactive"),state='readonly',justify=CENTER,font=("times new roman",15,"bold"))
        cmb_status.place(x=150,y=360,width=200)
        cmb_status.current(0)

        #===============buttons====================
        btn_add=Button(product_frame,text="Add",command=self.add,font=("times new roman",15,"bold"),bg="#4caf50",fg="white",cursor="hand2").place(x=10,y=400,width=100,height=40)
        btn_update=Button(product_frame,text="Update",command=self.update,font=("times new roman",15,"bold"),bg="#4caf50",fg="white",cursor="hand2").place(x=120,y=400,width=100,height=40)
        btn_delete=Button(product_frame,text="Delete",command=self.delete,font=("times new roman",15,"bold"),bg="#4caf50",fg="white",cursor="hand2").place(x=230,y=400,width=100,height=40)
        btn_clear=Button(product_frame,text="Clear",command=self.clear,font=("times new roman",15,"bold"),bg="#4caf50",fg="white",cursor="hand2").place(x=340,y=400,width=100,height=40)
       
        #================searchFrame=========

        SearchFrame=LabelFrame(self.root,text="Search Product",bg="white",font=("times new roman",15,"bold"),bd=2,relief=RIDGE)
        SearchFrame.place(x=480,y=10,width=600,height=80)

        #===============options==========
        cmb_search=ttk.Combobox(SearchFrame,textvariable=self.var_searchby,values=("Select","Category","Brand","pname"),state='readonly',justify=CENTER,font=("times new roman",15,"bold"))
        cmb_search.place(x=10,y=10,width=180)
        cmb_search.current(0)

        txt_search=Entry(SearchFrame,textvariable=self.var_searchtxt,font=("times new roman",15,"bold"),bg="lightyellow").place(x=200,y=10)
        btn_search=Button(SearchFrame,text="Search By",command=self.search,font=("times new roman",15,"bold"),bg="#4caf50",fg="white",cursor="hand2").place(x=410,y=9,width=150,height=30)


        #=========Product Details===========
        prod_frame=Frame(self.root,bd=3,relief=RIDGE)
        prod_frame.place(x=480,y=100,width=600,height=390)

        scrolly=Scrollbar(prod_frame,orient=VERTICAL)
        scrollx=Scrollbar(prod_frame,orient=HORIZONTAL)

        self.ProductTable=ttk.Treeview(prod_frame,columns=("pid","category","brand","pname","price","qty","status"),yscrollcommand=scrolly.set,xscrollcommand=scrollx.set)
        scrollx.pack(side=BOTTOM,fill=X)
        scrolly.pack(side=RIGHT,fill=Y)
        scrollx.config(command=self.ProductTable.xview)
        scrolly.config(command=self.ProductTable.yview)
        self.ProductTable.heading("pid",text="Product Id")
        self.ProductTable.heading("category",text="Category")
        self.ProductTable.heading("brand",text="Brand")
        self.ProductTable.heading("pname",text="Product Name")
        self.ProductTable.heading("price",text="Price")
        self.ProductTable.heading("qty",text="Quantity")
        self.ProductTable.heading("status",text="Status")
        self.ProductTable["show"]="headings"
        self.ProductTable.column("pid",width=90)
        self.ProductTable.column("category",width=100)
        self.ProductTable.column("brand",width=100)
        self.ProductTable.column("pname",width=100)
        self.ProductTable.column("price",width=100)
        self.ProductTable.column("qty",width=100)
        self.ProductTable.column("status",width=100)

        self.ProductTable.pack(fill=BOTH,expand=1)
        self.ProductTable.bind("<ButtonRelease-1>",self.get_data)
        self.show()
        #=========================================
    def fetch_cat_brand(self):
        con=c.connect(host="localhost",username="root",password="unnati@15",database="ty")         
        cursor=con.cursor()
        try:
            cursor.execute("Select cname from Category")
            cat=cursor.fetchall()
            self.cat_list.append("Empty")
            if len(cat)>0:
                del self.cat_list[:]
                self.cat_list.append("Select")
                for i in cat:
                    self.cat_list.append(i[0])   

            cursor.execute("Select bname from Brand")
            brand=cursor.fetchall()
            self.brand_list.append("Empty")
            if len(brand)>0:
                del self.brand_list[:]
                self.brand_list.append("Select")
                for i in brand:
                    self.brand_list.append(i[0])

                    
                    
        except Exception as ex:
                messagebox.showerror("Error",f"Error due to : {str(ex)}",parent=self.root)        

         


    def add(self):
        con=c.connect(host="localhost",username="root",password="unnati@15",database="ty")         
        cursor=con.cursor()

        a=self.var_prod_id.get()
        b=self.var_cat.get()
        c1=self.var_brand.get()
        d=self.var_prod_name.get()
        e=self.var_price.get()
        a1=self.var_qty.get()
        b1=self.var_status.get()
        try:
            if self.var_cat.get()=="Select" or self.var_brand.get()=="Select" or self.var_prod_name.get()=="":
                messagebox.showerror("Error","All fields are required",parent=self.root)
            else:    
                cursor.execute("insert into Product (pid,category,brand,pname,price,qty,status) values({}, '{}','{}','{}',{},{},'{}')".format(a,str(b),str(c1),str(d),e,a1,str(b1)))
                con.commit()
                messagebox.showinfo("Success","Product added successfully")
                self.show()
                con.close()
        except Exception as ex:
                messagebox.showerror("Error",f"Error due to : {str(ex)}",parent=self.root)

    def show(self):
        con=c.connect(host="localhost",username="root",password="unnati@15",database="ty")         
        cursor=con.cursor()
        try:
            cursor.execute("select * from Product")
            rows=cursor.fetchall()
            self.ProductTable.delete(*self.ProductTable.get_children())
            for row in rows:
                self.ProductTable.insert('',END,values=row)
        except Exception as ex:
                messagebox.showerror("Error",f"Error due to : {str(ex)}",parent=self.root)
          
    def get_data(self,ev):
        f=self.ProductTable.focus()
        content=(self.ProductTable.item(f))
        row=content['values']
        #print(row)
        self.var_prod_id.set(row[0])
        self.var_cat.set(row[1])
        self.var_brand.set(row[2])
        self.var_prod_name.set(row[3])
        self.var_price.set(row[4])
        self.var_qty.set(row[5])
        self.var_status.set(row[6])

    def update(self):
        con=c.connect(host="localhost",username="root",password="unnati@15",database="ty")         
        cursor=con.cursor()

        b=self.var_cat.get()
        c1=self.var_brand.get()
        d=self.var_prod_name.get()
        e=self.var_price.get()
        a1=self.var_qty.get()
        b1=self.var_status.get()
        a=self.var_prod_id.get()
        try:
            if self.var_prod_id.get()==" ":
                messagebox.showerror("Error","Product id required",parent=self.root)
            else:    
                cursor.execute("update Product set category='{}',brand='{}',pname='{}',price={},qty={},status='{}' where pid={}".format(str(b),str(c1),str(d),e,a1,str(b1),a))
                con.commit()
                messagebox.showinfo("Success","Product updated successfully")
                self.show()
                con.close()
        except Exception as ex:
                messagebox.showerror("Error",f"Error due to : {str(ex)}",parent=self.root)

    def delete(self):
        con=c.connect(host="localhost",username="root",password="unnati@15",database="ty")         
        cursor=con.cursor()

        a=self.var_prod_id.get()
        try:
            if self.var_prod_id.get()==" ":
                messagebox.showerror("Error","Product id required",parent=self.root)
            else:    
                op=messagebox.askyesno("confirm","Do you really want to delete?",parent=self.root)
                if op==True:
                    cursor.execute("delete from Product where pid={}".format(a))
                    con.commit()
                    messagebox.showinfo("Deleted","Product deleted successfully")
                    self.show()
                    con.close()
        except Exception as ex:
                messagebox.showerror("Error",f"Error due to : {str(ex)}",parent=self.root)        

    def clear(self):
        self.var_prod_id.set("")
        self.var_cat.set("Select")
        self.var_brand.set("Select")
        self.var_prod_name.set("")
        self.var_price.set("")
        self.var_qty.set("")
        self.var_status.set("Select")
        self.var_searchtxt.set("")
        self.var_searchby.set("Select")     
        self.show()                    

    def search(self):
        con=c.connect(host="localhost",username="root",password="unnati@15",database="ty")         
        cursor=con.cursor()
        try:
            if self.var_searchby.get()=="Select":
                messagebox.showerror("Error","Select Search by option",parent=self.root)
            elif self.var_searchtxt.get()=="":   
                messagebox.showerror("Error","Search input should be required",parent=self.root)
            else:
                cursor.execute("select * from Product where " + self.var_searchby.get() + " LIKE '%" +self.var_searchtxt.get() + "%'")
                rows=cursor.fetchall()
                if  len(rows)!=0:
                    self.ProductTable.delete(*self.ProductTable.get_children())
                    for row in rows:
                        self.ProductTable.insert('',END,values=row)
                else:
                    messagebox.showerror("Error","Not found")
          
        except Exception as ex:
                messagebox.showerror("Error",f"Error due to : {str(ex)}",parent=self.root)
          

    
          



if __name__=='__main__':
       root=Tk()
       obj=productClass(root)
       root.mainloop()    