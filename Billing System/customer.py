from time import strftime
from tkinter import *
from datetime import datetime
from PIL import Image,ImageTk
from tkinter import ttk,messagebox
import mysql.connector as c

class customerClass:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1100x500+220+130")
        self.root.resizable(False, False)
        self.root.title("Clothing Billing System")
        self.root.config(bg="white")
        self.root.focus_force()
        #=====================
        # all variables==============
        self.var_searchby=StringVar()
        self.var_searchtxt=StringVar()

        self.var_cust_id=IntVar()
        self.var_cust_name=StringVar()
        self.var_cust_email=StringVar()
        self.var_cust_mobile=StringVar()
        self.var_cust_dob=StringVar()
        self.var_cust_addr=StringVar()
        #================searchFrame=========

        SearchFrame=LabelFrame(self.root,text="Search Customer",bg="white",font=("times new roman",15,"bold"),bd=2,relief=RIDGE)
        SearchFrame.place(x=250,y=20,width=600,height=70)

        #===============options==========
        cmb_search=ttk.Combobox(SearchFrame,textvariable=self.var_searchby,values=("Select","Email","Name"),state='readonly',justify=CENTER,font=("times new roman",15,"bold"))
        cmb_search.place(x=10,y=10,width=180)
        cmb_search.current(0)

        txt_search=Entry(SearchFrame,textvariable=self.var_searchtxt,font=("times new roman",15,"bold"),bg="lightyellow").place(x=200,y=10)
        btn_search=Button(SearchFrame,text="Search By",command=self.search,font=("times new roman",15,"bold"),bg="#4caf50",fg="white",cursor="hand2").place(x=410,y=9,width=150,height=30)

        #===title===
        title=Label(self.root,text="Customer Details",font=("times new roman",15,"bold"),bg="#0f4d7d",fg="white").place(x=0,y=100,relwidth=1,height=40)
        #=========contents===========
        lbl_custid=Label(self.root,text="Id",font=("times new roman",15,"bold"),bg="white").place(x=100,y=150)
        lbl_custname=Label(self.root,text="Name",font=("times new roman",15,"bold"),bg="white").place(x=350,y=150)
        lbl_custemail=Label(self.root,text="Email",font=("times new roman",15,"bold"),bg="white").place(x=650,y=150)
        lbl_custmobile=Label(self.root,text="Mob",font=("times new roman",15,"bold"),bg="white").place(x=100,y=190)
        lbl_custdob=Label(self.root,text="DOB",font=("times new roman",15,"bold"),bg="white").place(x=350,y=190)
        lbl_custaddr=Label(self.root,text="Address",font=("times new roman",15,"bold"),bg="white").place(x=650,y=190)
        
        txt_custid=Entry(self.root,textvariable=self.var_cust_id,font=("times new roman",15,"bold"),bg="white").place(x=150,y=150,width=180)
        txt_custname=Entry(self.root,textvariable=self.var_cust_name,font=("times new roman",15,"bold"),bg="white").place(x=450,y=150,width=180)
        txt_custemail=Entry(self.root,textvariable=self.var_cust_email,font=("times new roman",15,"bold"),bg="white").place(x=750,y=150,width=180)
        txt_custmobile=Entry(self.root,textvariable=self.var_cust_mobile,font=("times new roman",15,"bold"),bg="white").place(x=150,y=190,width=180)
        txt_custdob=Entry(self.root,textvariable=self.var_cust_dob,font=("times new roman",15,"bold"),bg="white").place(x=450,y=190,width=180)
        txt_custaddr=Entry(self.root,textvariable=self.var_cust_addr,font=("times new roman",15,"bold"),bg="white").place(x=750,y=190,width=260,height=50)


        #===============buttons====================
        btn_add=Button(self.root,text="Add",command=self.add,font=("times new roman",15,"bold"),bg="#4caf50",fg="white",cursor="hand2").place(x=150,y=250,width=150,height=30)
        btn_update=Button(self.root,text="Update",command=self.update,font=("times new roman",15,"bold"),bg="#4caf50",fg="white",cursor="hand2").place(x=350,y=250,width=150,height=30)
        btn_delete=Button(self.root,text="Delete",command=self.delete,font=("times new roman",15,"bold"),bg="#4caf50",fg="white",cursor="hand2").place(x=550,y=250,width=150,height=30)
        btn_clear=Button(self.root,text="Clear",command=self.clear,font=("times new roman",15,"bold"),bg="#4caf50",fg="white",cursor="hand2").place(x=750,y=250,width=150,height=30)
       
        #=========Customer Details===========
        cust_frame=Frame(self.root,bd=3,relief=RIDGE)
        cust_frame.place(x=0,y=350,relwidth=1,height=150)

        scrolly=Scrollbar(cust_frame,orient=VERTICAL)
        scrollx=Scrollbar(cust_frame,orient=HORIZONTAL)

        self.CustomerTable=ttk.Treeview(cust_frame,columns=("id","name","email","mobno","dob","addr"),yscrollcommand=scrolly.set,xscrollcommand=scrollx.set)
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
        self.CustomerTable.bind("<ButtonRelease-1>",self.get_data)
        self.show()
    #=========================================
   
    def add(self):
        con=c.connect(host="localhost",username="root",password="unnati@15",database="ty")         
        cursor=con.cursor()

        a=self.var_cust_id.get()
        b=self.var_cust_name.get()
        c1=self.var_cust_email.get()
        d=self.var_cust_mobile.get()
        e=self.var_cust_dob.get()
        a1=self.var_cust_addr.get()
        try:
            if self.var_cust_id.get()==" ":
                messagebox.showerror("Error","Customer id required",parent=self.root)
            else:    
                cursor.execute("insert into Customer (id,name,email,mobno,dob,addr) values({}, '{}','{}','{}','{}','{}')".format(a,str(b),str(c1),str(d),str(e),str(a1)))
                con.commit()
                messagebox.showinfo("Success","Customer added successfully")
                self.show()
                con.close()
        except Exception as ex:
                messagebox.showerror("Error",f"Error due to : {str(ex)}",parent=self.root)

    def show(self):
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
          
    def get_data(self,ev):
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

    def update(self):
        con=c.connect(host="localhost",username="root",password="unnati@15",database="ty")         
        cursor=con.cursor()

        b=self.var_cust_name.get()
        c1=self.var_cust_email.get()
        d=self.var_cust_mobile.get()
        e=self.var_cust_dob.get()
        a1=self.var_cust_addr.get()
        a=self.var_cust_id.get()
        try:
            if self.var_cust_id.get()==" ":
                messagebox.showerror("Error","Customer id required",parent=self.root)
            else:    
                cursor.execute("update Customer set name='{}',email='{}',mobno='{}',dob='{}',addr='{}' where id={}".format(str(b),str(c1),str(d),str(e),str(a1),a))
                con.commit()
                messagebox.showinfo("Success","Customer updated successfully")
                self.show()
                con.close()
        except Exception as ex:
                messagebox.showerror("Error",f"Error due to : {str(ex)}",parent=self.root)

    def delete(self):
        con=c.connect(host="localhost",username="root",password="unnati@15",database="ty")         
        cursor=con.cursor()

        a=self.var_cust_id.get()
        try:
            if self.var_cust_id.get()==" ":
                messagebox.showerror("Error","Customer id required",parent=self.root)
            else:    
                op=messagebox.askyesno("confirm","Do you really want to delete?",parent=self.root)
                if op==True:
                    cursor.execute("delete from Customer where id={}".format(a))
                    con.commit()
                    messagebox.showinfo("Deleted","Customer deleted successfully")
                    self.show()
                    con.close()
        except Exception as ex:
                messagebox.showerror("Error",f"Error due to : {str(ex)}",parent=self.root)        

    def clear(self):
        self.var_cust_id.set("")
        self.var_cust_name.set("")
        self.var_cust_email.set("")
        self.var_cust_mobile.set("")
        self.var_cust_dob.set("")
        self.var_cust_addr.set("")
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
                cursor.execute("select * from Customer where " + self.var_searchby.get() + " LIKE '%" +self.var_searchtxt.get() + "%'")
                rows=cursor.fetchall()
                if  len(rows)!=0:
                    self.CustomerTable.delete(*self.CustomerTable.get_children())
                    for row in rows:
                        self.CustomerTable.insert('',END,values=row)
                else:
                    messagebox.showerror("Error","Not found")
          
        except Exception as ex:
                messagebox.showerror("Error",f"Error due to : {str(ex)}",parent=self.root)
          

if __name__=='__main__':
       root=Tk()
       obj=customerClass(root)
       root.mainloop()