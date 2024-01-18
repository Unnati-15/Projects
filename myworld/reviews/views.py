from django.shortcuts import render
import mysql.connector as sql
fn=''
ln=''
em=''
sub=''
# Create your views here.
def reviewaction(request):
    global fn,ln,em,sub
    if request.method=="POST":
        m=sql.connect(host="localhost",user="root",passwd="unnati@15",database='myworld')
        cursor=m.cursor()
        d=request.POST
        for key,value in d.items():
            if key=="firstname":
                fn=value
            if key=="lastname":
                ln=value
            if key=="email":
                em=value
            if key=="subject":
                sub=value
        
        c="insert into users_review Values('{}','{}','{}','{}')".format(fn,ln,em,sub)
        cursor.execute(c)
        m.commit()

    return render(request,'Reviews.html')


