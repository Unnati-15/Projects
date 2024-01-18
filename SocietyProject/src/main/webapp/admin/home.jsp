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

<c:if test ="${empty userobj}">
	<c:redirect url="../login.jsp"/>
</c:if>

<h2>
  <div class="container">
  <div class="jumbotron">
    <h1>Welcome ADMIN!!<a href="add_member.jsp"><button type="button" class="btn btn-primary">GET STARTED</button></a>
</h1>      
 </div>     
</div>
</h2>
</body>
</html>