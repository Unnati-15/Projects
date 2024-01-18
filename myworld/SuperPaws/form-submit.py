print("HTTP/1.0 200 OK\n")
import cgi
form = cgi.FieldStorage()
fname=form["fname"].value
sname=form["s_name"].value
r1=form["r1"].value
my_class=form["class"].value


print("<br><b>First Name</b>",fname)
print("<br><b>Second Name</b>",sname)
print("<br><b>Sex</b>",r1)
print("<br><b>Class</b>",my_class)
print("<br><br><br><a href=form.html>Back to Form</a>")
