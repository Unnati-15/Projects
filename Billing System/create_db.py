import mysql.connector as c

def create_db():
        con=c.connect(host="localhost",username="root",password="unnati@15",database="ty")         
        cursor=con.cursor()
        cursor.execute("create table if not exists Customer(id integer primary key ,name varchar(20),email varchar(20),mobno varchar(20),dob varcha(20),addr varchar(20))")
        con.commit()
        print("Customer Created")
        
        cursor.execute("create table if not exists Category(cid integer primary key ,cname varchar(20))")
        con.commit()
        print("Category Created")

        cursor.execute("create table if not exists Brand(bid int primary key,bname varchar(20))")
        con.commit()
        print("Brand Created")

        cursor.execute("create table if not exists Product(pid int primary key,category varchar(20),brand varchar(20),pname varchar(20),price int,qty int,status varchar(10))")
        con.commit()
        print("Product Created")
        
create_db()