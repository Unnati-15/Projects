<%@ page language="java" contentType="text/html; charset=ISO-8859-1"
    pageEncoding="ISO-8859-1"%>
    <%@ taglib prefix="c" uri="http://java.sun.com/jsp/jstl/core" %>
 <%@ page isELIgnored="false" %>
<!DOCTYPE html>
<html>
<head>
<meta charset="ISO-8859-1">
<title>Home Page</title>
<%@include file="all_component/allCss.jsp"%>
</head>
<body>

<img src="images/soc_navbar.png"  width="100%" height="400">
<br>
<nav class="navbar navbar-expand-lg p-3 mb-2 bg-">
 
  <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarSupportedContent" aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation">
    <span class="navbar-toggler-icon"></span>
  </button>




	<h5>
  <div class="collapse navbar-collapse" id="navbarSupportedContent">
    <ul class="navbar-nav mr-auto">
      <li class="nav-item active">
        <a class="nav-link" href="home.jsp">Home<span class="sr-only"></span></a>
      </li>
       <li class="nav-item active">
        <a class="nav-link" href="add_complaint.jsp">Complaint<span class="sr-only"></span></a>
      </li>
     <li class="nav-item active">
        <a class="nav-link" href="view_bill.jsp">Bill<span class="sr-only"></span></a>
      </li>
      <li class="nav-item active">
        <a class="nav-link" href="view_SR.jsp">Sell/Rent<span class="sr-only"></span></a>
      </li>
      <li class="nav-item active">
        <a class="nav-link" href="view_mom.jsp">Meetings<span class="sr-only"></span></a>
      </li>
     
    </ul>&nbsp;
      &nbsp;
        &nbsp;
        &nbsp; &nbsp;
        &nbsp;
        &nbsp; &nbsp;
        &nbsp;
        &nbsp;&nbsp;
        &nbsp;
        &nbsp;&nbsp;
        &nbsp;
        &nbsp;&nbsp;
        &nbsp;
        &nbsp;&nbsp;
        &nbsp;
        &nbsp;&nbsp;
        &nbsp;
        &nbsp;&nbsp;
        &nbsp;
        &nbsp;&nbsp;
        &nbsp;
        &nbsp;&nbsp;
        &nbsp;
        &nbsp;&nbsp;
        &nbsp;
        &nbsp;&nbsp;
        &nbsp;
        &nbsp;&nbsp;
        &nbsp;
        &nbsp;&nbsp;
        &nbsp;
        &nbsp;&nbsp;
        &nbsp;
        &nbsp;&nbsp;
        &nbsp;
        &nbsp;&nbsp;
        &nbsp;
        &nbsp;&nbsp;
        &nbsp;
        &nbsp;&nbsp;
        &nbsp;
        &nbsp;&nbsp;
        &nbsp;
        &nbsp;&nbsp;
        &nbsp;
        &nbsp;&nbsp;
        &nbsp;
        &nbsp;&nbsp;
        &nbsp;
        &nbsp;&nbsp;
        &nbsp;
        &nbsp;&nbsp;
        &nbsp;
        &nbsp;&nbsp;
        &nbsp;
        &nbsp;&nbsp;
        &nbsp;
        &nbsp;&nbsp;
        &nbsp;
        &nbsp;&nbsp;
        &nbsp;
        &nbsp;&nbsp;
        &nbsp;
        &nbsp;&nbsp;
        &nbsp;
        &nbsp;&nbsp;
        &nbsp;
        &nbsp;&nbsp;
        &nbsp;
        &nbsp;&nbsp;
        &nbsp;
        &nbsp;&nbsp;
        &nbsp;
        &nbsp;&nbsp;
        &nbsp;
        &nbsp;&nbsp;
        &nbsp;
        &nbsp;
&nbsp;
        &nbsp;
        &nbsp;&nbsp;
        &nbsp;
        &nbsp;&nbsp;
        &nbsp;
        &nbsp;&nbsp;
        &nbsp;
        &nbsp;&nbsp;
        &nbsp;
        &nbsp;&nbsp;
        &nbsp;
        &nbsp;&nbsp;
        &nbsp;
        &nbsp;&nbsp;
        &nbsp;
        &nbsp;&nbsp;
        &nbsp;
 
        &nbsp;&nbsp;
        &nbsp;
        &nbsp;&nbsp;
        &nbsp;
        &nbsp;&nbsp;
      &nbsp;&nbsp;
&nbsp;&nbsp;
        &nbsp;&nbsp;
      &nbsp;&nbsp;
        &nbsp;&nbsp;
        &nbsp;&nbsp;
        &nbsp;
        &nbsp;&nbsp;
        &nbsp;
        &nbsp;&nbsp;
        &nbsp;
        &nbsp;&nbsp;
        &nbsp;
        &nbsp;&nbsp;
        &nbsp;
        &nbsp;
        &nbsp;
<c:if test ="${not empty userobj }">
	<h1><a class="btn btn-outline-success">${userobj.email}</a></h1>
</c:if>
        &nbsp;
        &nbsp;
        &nbsp;
       <a href="logout" class="btn btn-outline-danger">Logout</a>
 </div>
 </h5>
</nav>


</body>
</html>