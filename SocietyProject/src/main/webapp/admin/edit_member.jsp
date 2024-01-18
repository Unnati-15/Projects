<%@ page language="java" contentType="text/html; charset=ISO-8859-1"
    pageEncoding="ISO-8859-1"%>
<%@ taglib prefix="c" uri="http://java.sun.com/jsp/jstl/core" %>
<%@ page isELIgnored="false" %>
<%@ page import="javax.servlet.http.HttpServletRequest" %>
<%@ page import=" com.entity.Member" %>
<%@ page import="com.DAO.MemberDAOimp1" %>
<%@ page import="com.DB.DBConnect" %>
<!DOCTYPE html>
<html>
<head>
<meta charset="ISO-8859-1">
<title>Admin:Home</title>
<%@include file="allCss.jsp" %>
</head>
<body>
<%@include file="navbar.jsp" %>

<c:if test ="${empty userobj}">
	<c:redirect url="../login.jsp"/>
</c:if>

<%
int id=Integer.parseInt(request.getParameter("id"));
MemberDAOimp1 dao= new MemberDAOimp1(DBConnect.getConn());
Member m=dao.getMemberById(id);
%>

<form action="../MemberEdit" method="post">
  <div class="container">
    <h1 style="flaot:center;font-color:Blue;">Edit Member</h1>
    <label for="id"><b>Id</b></label>
    <input type="hidden" placeholder="Enter ID..." name="id" value = "<%=m.getMember_id()%>" required>
   
    
   
   <label for="name"><b>Name</b></label>
    <input type="text" placeholder="Enter Name..." name="name" value = "<%=m.getName()%>" required>
   
   
    <label for="email"><b>Email</b></label>
    <input type="text" placeholder="Enter Email..." name="email" value = "<%=m.getEmail()%>" required>

    
    <label for="number"><b>Phone Number</b></label>
    <input type="number" placeholder="Enter Number..." name="number" value = "<%=m.getNumber()%>" required>
    
    <label for="role"><b>Role</b></label>
    <input type="text" placeholder="Enter Role..." name="role" value = "<%=m.getRole()%>" required>
    
    
    <p>to view details click here-><a href="view_member.jsp" style="color:dodgerblue">View</a></p>

    <div class="clearfix">
      <button type="button" class="cancelbtn">Cancel</button>
      <button type="submit" class="signupbtn">Update</button>
    </div>
  </div>
</form>

</body>
</html>