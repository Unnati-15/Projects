<%@ page language="java" contentType="text/html; charset=ISO-8859-1"
    pageEncoding="ISO-8859-1"%>
<%@ taglib prefix="c" uri="http://java.sun.com/jsp/jstl/core" %>
<%@ page import="com.admin.servlet.*" %>
<%@ page isELIgnored="false" %>
<%@ page import=" com.entity.Mom" %>
<%@ page import="com.DAO.MomDAOimp1" %>
<%@ page import="com.DB.DBConnect" %>


<!DOCTYPE html>
<html>
<head>
<meta charset="ISO-8859-1">
<title>Admin:Mom</title>
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
	<c:redirect url="/login.jsp"/>
</c:if>

<form action="../MomAdd" method="post">
  <div class="container">
    <h1 style="flaot:center;font-color:Blue;">Add Minutes of Meeting</h1>
   
   <label for="text"><b>Content</b></label>
    <input type="text" placeholder="Enter Content..." name="content" required>
    
    <label for="text"><b>Date</b></label>
    <input type="text" placeholder="Enter Date..." name="date" required>
    
    <p>to view details click here-><a href="view_mom.jsp" style="color:dodgerblue">View</a></p>

    <div class="clearfix">
      <button type="button" class="cancelbtn">Cancel</button>
      <button type="submit" class="signupbtn">ADD</button>
    </div>
  </div>
</form>

</body>
</html>