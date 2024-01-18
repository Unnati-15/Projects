from time import strftime
from tkinter import *
from PIL import Image,ImageTk
from tkinter import ttk,messagebox
import mysql.connector as c

class categoryClass:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1100x500+220+130")
        self.root.resizable(False, False)
        self.root.title("Clothing Billing System")
        self.root.config(bg="white")
        self.root.focus_force()
        #===============variables================
        self.var_cat_id=IntVar()
        self.var_name=StringVar()
        #==============title====================
        lbl_title=Label(self.root,text="Manage Product Category",font=("times new roman ",30),bg="#184a45",fg="white",bd=3,relief=RIDGE).pack(side=TOP,fill=X)
        
        lbl_id=Label(self.root,text="Enter Category Id",font=("times new roman ",18),bg="white").place(x=25,y=100)
        txt_id=Entry(self.root,textvariable=self.var_cat_id,font=("times new roman ",18),bg="lightyellow").place(x=250,y=100,width=150)

        lbl_name=Label(self.root,text="Enter Category Name",font=("times new roman ",18),bg="white").place(x=25,y=140)
        txt_name=Entry(self.root,textvariable=self.var_name,font=("times new roman ",18),bg="lightyellow").place(x=270,y=140,width=180)

        btn_add=Button(self.root,text="ADD",command=self.add,font=("times new roman ",15),bg="#4caf50",fg="white",cursor="hand2").place(x=360,y=180,width=150,height=30)
        btn_delete=Button(self.root,text="DELETE",command=self.delete,font=("times new roman ",15),bg="#4caf50",fg="white",cursor="hand2").place(x=520,y=180,width=150,height=30)
        #=========Category Details===========
        cat_frame=Frame(self.root,bd=3,relief=RIDGE)
        cat_frame.place(x=700,y=100,width=380,height=100)

        scrolly=Scrollbar(cat_frame,orient=VERTICAL)
        scrollx=Scrollbar(cat_frame,orient=HORIZONTAL)

        self.CategoryTable=ttk.Treeview(cat_frame,columns=("cid","cname"),yscrollcommand=scrolly.set,xscrollcommand=scrollx.set)
        scrollx.pack(side=BOTTOM,fill=X)
        scrolly.pack(side=RIGHT,fill=Y)
        scrollx.config(command=self.CategoryTable.xview)
        scrolly.config(command=self.CategoryTable.yview)
        self.CategoryTable.heading("cid",text="Category Id")
        self.CategoryTable.heading("cname",text="Category Name")
        self.CategoryTable["show"]="headings"
        self.CategoryTable.column("cid",width=90)
        self.CategoryTable.column("cname",width=100)

        self.CategoryTable.pack(fill=BOTH,expand=1)
        self.CategoryTable.bind("<ButtonRelease-1>",self.get_data)
        self.show()
    #=================Images======================
        self.img1=Image.open("img4.jpg")
        self.img1=self.img1.resize((500,250),Image.Resampling.LANCZOS)
        self.img1=ImageTk.PhotoImage(self.img1)
        self.lbl_img1=Label(self.root,image=self.img1,bd=2,relief=RAISED).place(x=50,y=220)

        self.img2=Image.open("img5.jpg")
        self.img2=self.img2.resize((500,250),Image.Resampling.LANCZOS)
        self.img2=ImageTk.PhotoImage(self.img2)
        self.lbl_img2=Label(self.root,image=self.img2,bd=2,relief=RAISED).place(x=580,y=220)
    #=================functions======================
    def add(self):
        con=c.connect(host="localhost",username="root",password="unnati@15",database="ty")         
        cursor=con.cursor()

        a=self.var_cat_id.get()
        b=self.var_name.get()
        try:
            if self.var_cat_id.get()==" ":
                messagebox.showerror("Error","Category id required",parent=self.root)
            else:    
                cursor.execute("insert into Category (cid,cname) values({}, '{}')".format(a,str(b)))
                con.commit()
                messagebox.showinfo("Success","Category added successfully")
                self.show()
                con.close()
        except Exception as ex:
                messagebox.showerror("Error",f"Error due to : {str(ex)}",parent=self.root)    

    def show(self):
        con=c.connect(host="localhost",username="root",password="unnati@15",database="ty")         
        cursor=con.cursor()
        try:
            cursor.execute("select * from Category")
            rows=cursor.fetchall()
            self.CategoryTable.delete(*self.CategoryTable.get_children())
            for row in rows:
                self.CategoryTable.insert('',END,values=row)
        except Exception as ex:
                messagebox.showerror("Error",f"Error due to : {str(ex)}",parent=self.root)
          
    def get_data(self,ev):
        f=self.CategoryTable.focus()
        content=(self.CategoryTable.item(f))
        row=content['values']
        #print(row)
        self.var_cat_id.set(row[0])
        self.var_name.set(row[1])

    def delete(self):
        con=c.connect(host="localhost",username="root",password="unnati@15",database="ty")         
        cursor=con.cursor()

        a=self.var_cat_id.get()
        try:
            if self.var_cat_id.get()==" ":
                messagebox.showerror("Error","Category id required",parent=self.root)
            else:    
                op=messagebox.askyesno("confirm","Do you really want to delete?",parent=self.root)
                if op==True:
                    cursor.execute("delete from Category where cid={}".format(a))
                    con.commit()
                    messagebox.showinfo("Deleted","Category deleted successfully")
                    self.show()
                    con.close()
        except Exception as ex:
                messagebox.showerror("Error",f"Error due to : {str(ex)}",parent=self.root)     

if __name__=='__main__':
       root=Tk()
       obj=categoryClass(root)
       root.mainloop()        