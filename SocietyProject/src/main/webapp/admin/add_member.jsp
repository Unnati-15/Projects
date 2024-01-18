<%@ page language="java" contentType="text/html; charset=ISO-8859-1"
    pageEncoding="ISO-8859-1"%>
<%@ taglib prefix="c" uri="http://java.sun.com/jsp/jstl/core" %>
<%@ page isELIgnored="false" %>
<!DOCTYPE html>
<html>
<head>
<meta charset="ISO-8859-1">
<title>Admin:Home</title>
<%@include file="allCss.jsp" %>
</head>
<body>
<%@include file="navbar.jsp" %>

<c:if test ="${not empty succMsg }">
	<p class="text-center text-success">${succMsg}</p>
	<c:remove var="succMsg" scope="session"/>
</c:if>
<c:if test ="${not empty failedMsg }">
	<p class="text-center text-danger">${failedMsg}</p>
	<c:remove var="failedMsg" scope="session"/>
</c:if>
<c:if test ="${empty userobj}">
	<c:redirect url="../login.jsp"/>
</c:if>
<form action="../MemberAdd" method="post">
  <div class="container">
    <h1 style="flaot:center;font-color:Blue;">Add Member</h1>
   
   <label for="name"><b>Name</b></label>
    <input type="text" placeholder="Enter Name..." name="name" required>
   
   
    <label for="email"><b>Email</b></label>
    <input type="text" placeholder="Enter Email..." name="email" required>

    
    <label for="number"><b>Phone Number</b></label>
    <input type="number" placeholder="Enter Number..." name="number" required>
    
    <label for="role"><b>Role</b></label>
    <input type="text" placeholder="Enter Role..." name="role" required>
    
    <p>to view details click here-><a href="view_member.jsp" style="color:dodgerblue">View</a></p>

    <div class="clearfix">
      <button type="button" class="cancelbtn">Cancel</button>
      <button type="submit" class="signupbtn">ADD</button>
    </div>
  </div>
</form>

</body>
</html>