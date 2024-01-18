<%@ page language="java" contentType="text/html; charset=ISO-8859-1"
    pageEncoding="ISO-8859-1"%>
<%@ taglib prefix="c" uri="http://java.sun.com/jsp/jstl/core" %>
<%@ page isELIgnored="false" %>
<!DOCTYPE html>
<html>
<head>
<meta charset="ISO-8859-1">
<title>Admin:Flat</title>
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
<form action="../FlatAdd" method="post">
  <div class="container">
    <h1 style="flaot:center;font-color:Blue;">Add Flat</h1>
   
   <label for="number"><b>Flat ID</b></label>
    <input type="number" placeholder="Enter Flat ID<..." name="flat_id" required>
   
   <label for="desc"><b>Flat Desc</b></label>
    <input type="text" placeholder="Enter Desc..." name="desc" required>
    
    <label for="number"><b>Member ID</b></label>
    <input type="number" placeholder="Enter Member ID<..." name="member_id" required>
    
    <label for="hidden"><b>Status</b></label>
    <input type="hidden" placeholder="Enter Status" name="status">
    
    <p>to view details click here-><a href="view_flat.jsp" style="color:dodgerblue">View</a></p>

    <div class="clearfix">
      <button type="button" class="cancelbtn">Cancel</button>
      <button type="submit" class="signupbtn">ADD</button>
    </div>
  </div>
</form>

</body>
</html>