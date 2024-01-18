<%@ page language="java" contentType="text/html; charset=ISO-8859-1"
    pageEncoding="ISO-8859-1"%>
<%@ taglib prefix="c" uri="http://java.sun.com/jsp/jstl/core" %>
<%@ page import="com.admin.servlet.*" %>
<%@ page isELIgnored="false" %>
<%@ page import=" com.entity.Complaint" %>
<%@ page import="com.DAO.ComplaintDAOimp1" %>
<%@ page import="com.DB.DBConnect" %>
<!DOCTYPE html>
<html>
<head>
<meta charset="ISO-8859-1">
<title>User:Complaint</title>
<%@include file="all_component/allCss.jsp" %>
</head>
<body>
<%@include file="home.jsp" %>

<c:if test ="${not empty succMsg }">
	<p class="text-center text-success">${succMsg}</p>
	<c:remove var="succMsg" scope="session"/>
</c:if>
<c:if test ="${not empty failedMsg }">
	<p class="text-center text-danger">${failedMsg}</p>
	<c:remove var="failedMsg" scope="session"/>
</c:if>
<c:if test ="${empty userobj}">
	<c:redirect url="/login.jsp"/>
</c:if>

<form action="ComplaintAdd" method="post">
  <div class="container">
    <h1 style="flaot:center;font-color:Blue;">Add Complaint</h1>
   
   <label for="complaint"><b>Complaint Desc</b></label>
    <input type="text" placeholder="Enter Complaint Desc..." name="complaint" required>
   
    <label for="status"><b>Status</b></label>
    <input type="text" placeholder="Enter Status : Resolved/Unresolved..." name="status" required>

    
    <label for="number"><b>Flat No</b></label>
    <input type="number" placeholder="Enter Flat Number..." name="flat_id" required>
    
    
    
    <p>to view details click here-><a href="view_complaint.jsp" style="color:dodgerblue">View</a></p>

    <div class="clearfix">
      <button type="button" class="cancelbtn">Cancel</button>
      <button type="submit" class="signupbtn">ADD</button>
    </div>
  </div>
</form>

</body>
</html>